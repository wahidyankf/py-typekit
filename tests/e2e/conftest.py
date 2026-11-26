"""Session fixtures for the end-to-end behaviour run: the built wheel, installed into a fresh virtual environment."""

import os
import shutil
import subprocess
import sys
import tempfile
from collections.abc import Callable, Iterator
from dataclasses import dataclass
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[2]
UNIT_TESTS = REPO_ROOT / "tests"
SCRATCH_PARENT = Path("/var/tmp")


@dataclass(frozen=True)
class WheelEnvironment:
    """The interpreter of the environment that holds the installed wheel, and a directory outside the repository."""

    python: Path
    run_dir: Path


def _child_environment() -> dict[str, str]:
    """The process environment, minus the variables that point a child at this repository's venv."""

    environment = {key: value for key, value in os.environ.items() if key not in {"VIRTUAL_ENV", "PYTHONPATH"}}
    environment["PYTHONDONTWRITEBYTECODE"] = "1"

    return environment


def _run(command: list[str], cwd: Path) -> subprocess.CompletedProcess[str]:
    """Run a command to completion, failing the test with its output when it does not exit 0."""

    completed = subprocess.run(
        command,
        cwd=cwd,
        env=_child_environment(),
        capture_output=True,
        text=True,
        check=False,
        timeout=600,
    )
    if completed.returncode != 0:
        pytest.fail(f"{' '.join(command[:2])} exited {completed.returncode}:\n{completed.stdout}{completed.stderr}")

    return completed


@pytest.fixture(scope="session")
def wheel_environment() -> Iterator[WheelEnvironment]:
    """Build the wheel, install it into a fresh virtual environment, and check that typekit imports from there."""

    scratch = Path(tempfile.mkdtemp(prefix="typekit-e2e-", dir=SCRATCH_PARENT))
    try:
        run_dir = scratch / "run"
        run_dir.mkdir()
        dist = scratch / "dist"
        _run(["uv", "build", "--wheel", "--out-dir", str(dist)], REPO_ROOT)
        wheel = next(dist.glob("*.whl"))

        requirements = scratch / "requirements.txt"
        _run(
            [
                "uv",
                "export",
                "--locked",
                "--only-group",
                "dev",
                "--no-hashes",
                "--no-emit-project",
                "--output-file",
                str(requirements),
            ],
            REPO_ROOT,
        )

        venv = scratch / "venv"
        _run(["uv", "venv", "--python", sys.executable, str(venv)], scratch)
        python = venv / "bin" / "python"
        _run(["uv", "pip", "install", "--python", str(python), "-r", str(requirements), str(wheel)], scratch)

        probe = _run([str(python), "-I", "-c", "import typekit; print(typekit.__file__)"], run_dir).stdout.strip()
        if not Path(probe).resolve().is_relative_to(venv.resolve()):
            pytest.fail(f"typekit imported from {probe}, not from the installed wheel in {venv}")

        yield WheelEnvironment(python=python, run_dir=run_dir)
    finally:
        shutil.rmtree(scratch, ignore_errors=True)


@pytest.fixture(scope="session")
def run_in_wheel(wheel_environment: WheelEnvironment) -> Callable[[str], None]:
    """Run one unit binding, named relative to tests/, with the installed wheel's interpreter."""

    def run(binding: str) -> None:
        _run(
            [
                str(wheel_environment.python),
                "-I",
                "-m",
                "pytest",
                "-p",
                "no:cacheprovider",
                "-q",
                str(UNIT_TESTS / binding),
            ],
            wheel_environment.run_dir,
        )

    return run
