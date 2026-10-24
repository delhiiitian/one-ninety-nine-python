"""6.4 Paths with pathlib.

Real-world comparison: a postal address. "India / Maharashtra / Pune /
MG Road" narrows down step by step. A path does the same for files:
folder / subfolder / file name. pathlib builds addresses that work on
Windows, macOS and Linux alike.
"""

from pathlib import Path

here = Path(__file__).parent
notes = here / "data" / "notes.txt"          # / joins path parts

print("Full path:", notes.resolve())
print("File name:", notes.name)
print("Name without extension:", notes.stem)
print("Extension:", notes.suffix)
print("Parent folder:", notes.parent.name)
print("Exists?", notes.exists())
print("Is a file?", notes.is_file())
print("Size in bytes:", notes.stat().st_size)

# Swap the extension or the file name.
print("As .md:", notes.with_suffix(".md").name)
print("Sibling:", notes.with_name("todo.txt").name)

# Quick read and write without open().
out = here / "output"
out.mkdir(exist_ok=True)
memo = out / "memo.txt"
memo.write_text("Meeting at 4 pm\n", encoding="utf-8")
print("Memo says:", memo.read_text(encoding="utf-8").strip())

# Home folder and current folder.
print("Your home folder:", Path.home())
print("Current folder:", Path.cwd())
