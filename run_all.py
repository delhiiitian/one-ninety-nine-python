"""Run every example in the book and report which ones pass.

Usage:  python run_all.py
Each chapter file is run as its own program. A file passes when it
finishes with exit code 0 within the time limit. Project test suites
are run with unittest.
"""

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).parent
SAMPLE_INPUT = "Ada\nPune\n3\n"      # answers for files that call input()
TIMEOUT = 60


def run(cmd, cwd):
    try:
        result = subprocess.run(cmd, cwd=cwd, input=SAMPLE_INPUT, text=True,
                                capture_output=True, timeout=TIMEOUT)
        return result.returncode == 0, result.stdout + result.stderr
    except subprocess.TimeoutExpired:
        return False, "timed out"


def main():
    failures = []
    examples = sorted(ROOT.glob("ch0*/[0-9][0-9]_*.py"))
    for path in examples:
        ok, output = run([sys.executable, path.name], cwd=path.parent)
        print(f"{'PASS' if ok else 'FAIL'}  {path.relative_to(ROOT)}")
        if not ok:
            failures.append((path, output))

    projects = sorted(p for p in (ROOT / "projects").iterdir() if (p / "tests").is_dir())
    for project in projects:
        ok, output = run([sys.executable, "-m", "unittest", "discover", "-s", "tests", "-t", "."],
                         cwd=project)
        print(f"{'PASS' if ok else 'FAIL'}  {project.relative_to(ROOT)} (tests)")
        if not ok:
            failures.append((project, output))

    print(f"\n{len(examples) + len(projects) - len(failures)} passed, {len(failures)} failed")
    for path, output in failures:
        print(f"\n--- {path.relative_to(ROOT)} ---\n{output[-2000:]}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
