"""Integration check for scripts/format-staged.sh: the formatters run without a ruff or prettier on PATH."""

import hashlib
import os
import shutil
import subprocess
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
FORMAT_STAGED = REPO_ROOT / "scripts" / "format-staged.sh"
UNFORMATTED_PYTHON = "x=1\n"
UNFORMATTED_JSON = '{"a":1}\n'


def test_format_staged_formats_python_and_json_with_only_uv_and_npx_on_path(tmp_path: Path) -> None:
    """A job whose PATH holds no ruff or prettier still formats a Python and a JSON file through the locked tools."""

    uv = shutil.which("uv")
    npx = shutil.which("npx")
    assert uv is not None, "uv must be installed to run the locked formatters"
    assert npx is not None, "npx must be installed to run the locked prettier"

    uv_dir = tmp_path / "uv-bin"
    uv_dir.mkdir()
    (uv_dir / "uv").symlink_to(uv)

    python_file = tmp_path / "module.py"
    python_file.write_text(UNFORMATTED_PYTHON, encoding="utf-8")
    json_file = tmp_path / "settings.json"
    json_file.write_text(UNFORMATTED_JSON, encoding="utf-8")

    environment = {key: value for key, value in os.environ.items() if key not in {"VIRTUAL_ENV", "PYTHONPATH"}}
    environment["PATH"] = os.pathsep.join([str(uv_dir), str(Path(npx).parent), "/usr/bin", "/bin"])

    completed = subprocess.run(
        ["bash", str(FORMAT_STAGED), str(python_file), str(json_file)],
        cwd=REPO_ROOT,
        env=environment,
        capture_output=True,
        text=True,
        check=False,
        timeout=600,
    )

    assert completed.returncode == 0, (
        f"format-staged exited {completed.returncode}:\n{completed.stdout}{completed.stderr}"
    )
    assert python_file.read_text(encoding="utf-8") == "x = 1\n"
    assert json_file.read_text(encoding="utf-8") != UNFORMATTED_JSON


def _tree_digests(root: Path) -> dict[str, str]:
    """Map every file and symlink under root, by relative POSIX path, to a digest of its contents or target."""
    digests: dict[str, str] = {}
    for path in sorted(root.rglob("*")):
        relative = path.relative_to(root).as_posix()
        if path.is_symlink():
            digests[relative] = "symlink:" + os.readlink(path)
        elif path.is_file():
            digests[relative] = hashlib.sha256(path.read_bytes()).hexdigest()
    return digests


def test_format_staged_writes_only_the_selected_file_inside_an_index_snapshot(tmp_path: Path) -> None:
    """A formatter run in a clean index snapshot changes only the selected file and creates nothing else.

    RHINO's local apply path formats a full `git checkout-index -a` snapshot and refuses any path the mutator creates
    or changes outside the selected paths, ignored paths included. The snapshot has no .venv or node_modules, so the
    formatter must not leave a project environment or any other artifact inside the tree.
    """

    uv = shutil.which("uv")
    npx = shutil.which("npx")
    assert uv is not None, "uv must be installed to run the locked formatters"
    assert npx is not None, "npx must be installed to run the locked prettier"

    uv_dir = tmp_path / "uv-bin"
    uv_dir.mkdir()
    (uv_dir / "uv").symlink_to(uv)

    snapshot = tmp_path / "snapshot"
    subprocess.run(
        ["git", "-C", str(REPO_ROOT), "checkout-index", "-a", f"--prefix={snapshot}{os.sep}"],
        check=True,
        capture_output=True,
        text=True,
        timeout=600,
    )
    # The index copy of the script can lag the working tree until it is staged, so the script under test is the
    # working-tree file, copied over the index copy.
    shutil.copy2(FORMAT_STAGED, snapshot / "scripts" / "format-staged.sh")

    selected = "formatted_target.py"
    (snapshot / selected).write_text(UNFORMATTED_PYTHON, encoding="utf-8")
    before = _tree_digests(snapshot)

    environment = {key: value for key, value in os.environ.items() if key not in {"VIRTUAL_ENV", "PYTHONPATH"}}
    environment["PATH"] = os.pathsep.join([str(uv_dir), str(Path(npx).parent), "/usr/bin", "/bin"])

    completed = subprocess.run(
        ["bash", "scripts/format-staged.sh", selected],
        cwd=snapshot,
        env=environment,
        capture_output=True,
        text=True,
        check=False,
        timeout=600,
    )

    assert completed.returncode == 0, (
        f"format-staged exited {completed.returncode}:\n{completed.stdout}{completed.stderr}"
    )
    after = _tree_digests(snapshot)
    changed = {path for path in before.keys() | after.keys() if before.get(path) != after.get(path)}
    unexpected = sorted(changed - {selected})
    assert not unexpected, f"paths outside the selected file changed or appeared: {unexpected[:20]}"
    assert changed == {selected}, f"the selected file did not change: {sorted(changed)}"
    assert (snapshot / selected).read_text(encoding="utf-8") == "x = 1\n"
