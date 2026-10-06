"""check-doc-snippets.py — the `doc-snippets` gate: every documented Python block is real under strict Pyright.

Each ```python block in README.md and docs/**/*.md is written to its own file in a temporary directory, and all of them
are checked in one strict Pyright run. A block with no `# Pyright error:` comment must have no error. A block with such
comments must fail on exactly the code line above each one, with the rule its comment group ends with, and nowhere else.

Usage: uv run --locked python scripts/check-doc-snippets.py   (from any directory; it checks the repository it lives in)
Exit:  0 when every block holds; 1 naming each block that does not; Pyright's own failure propagates as a crash.
"""

import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BLOCK = re.compile(r"^```python\n(.*?)^```$", re.S | re.M)
MARK = "# Pyright error:"
RULE = re.compile(r"\((report\w+)\)\s*$")


def expected(lines: list[str]) -> set[tuple[int, str]]:
    """The (line, rule) pairs a block's `# Pyright error:` comment groups promise, the line being the code above."""
    found: set[tuple[int, str]] = set()
    for index, line in enumerate(lines):
        if not line.strip().startswith(MARK):
            continue
        code = index - 1
        while lines[code].strip().startswith("#"):
            code -= 1
        end = index
        while end + 1 < len(lines) and lines[end + 1].strip().startswith("#") and MARK not in lines[end + 1]:
            end += 1
        rule = RULE.search(lines[end])
        found.add((code + 1, rule.group(1) if rule else "no rule named"))
    return found


def main() -> int:
    """Check every block and report each one whose Pyright errors differ from its marks."""
    sources = [ROOT / "README.md", *sorted((ROOT / "docs").rglob("*.md"))]
    blocks: dict[str, tuple[str, set[tuple[int, str]]]] = {}
    with tempfile.TemporaryDirectory() as tmp:
        for source in sources:
            for number, match in enumerate(BLOCK.finditer(source.read_text(encoding="utf-8")), 1):
                name = f"snippet_{len(blocks)}.py"
                (Path(tmp) / name).write_text(match.group(1), encoding="utf-8")
                blocks[name] = (f"{source.relative_to(ROOT)} block {number}", expected(match.group(1).split("\n")))
        if not blocks:
            print("doc-snippets: no python blocks")
            return 0
        command = [sys.executable, "-m", "pyright", "--outputjson", *(str(Path(tmp) / name) for name in blocks)]
        run = subprocess.run(command, cwd=ROOT, capture_output=True, text=True, check=False)
    if run.returncode not in (0, 1):
        raise SystemExit(f"doc-snippets: pyright exited {run.returncode}: {run.stderr.strip()}")
    actual: dict[str, set[tuple[int, str]]] = {name: set() for name in blocks}
    for diagnostic in json.loads(run.stdout)["generalDiagnostics"]:
        if diagnostic["severity"] == "error":
            line = diagnostic["range"]["start"]["line"] + 1
            actual[Path(diagnostic["file"]).name].add((line, diagnostic.get("rule", "no rule named")))
    failing = [name for name in blocks if actual[name] != blocks[name][1]]
    for name in failing:
        label, want = blocks[name]
        print(f"doc-snippets: {label}: marked {sorted(want)}, Pyright reported {sorted(actual[name])}", file=sys.stderr)
    print(f"doc-snippets: {len(blocks)} python blocks checked, {len(failing)} failing")
    return 1 if failing else 0


if __name__ == "__main__":
    sys.exit(main())
