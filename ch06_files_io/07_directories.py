"""6.7 Working with folders.

Real-world comparison: tidying a wardrobe. You look at what is inside,
make new drawers (folders), and move things into the right drawer.
"""

import shutil
from pathlib import Path

base = Path(__file__).parent / "output" / "wardrobe"
if base.exists():
    shutil.rmtree(base)               # start fresh each run
base.mkdir(parents=True)

# Create some files to work with.
for name in ["shirt.txt", "jeans.txt", "photo.jpg", "song.mp3", "scarf.txt"]:
    (base / name).write_text("demo", encoding="utf-8")

print("Everything in the folder:")
for item in sorted(base.iterdir()):
    print("  ", item.name)

# Find files by pattern.
print("Only .txt files:", sorted(p.name for p in base.glob("*.txt")))

# Make sub-folders and move files by type.
for item in list(base.iterdir()):
    if item.is_file():
        drawer = base / item.suffix.lstrip(".")
        drawer.mkdir(exist_ok=True)
        item.rename(drawer / item.name)

print("After tidying:")
for item in sorted(base.rglob("*")):          # rglob looks in sub-folders too
    depth = len(item.relative_to(base).parts) - 1
    print("  " + "    " * depth + item.name)

# Copy and delete.
shutil.copy(base / "txt" / "shirt.txt", base / "txt" / "shirt_copy.txt")
(base / "mp3" / "song.mp3").unlink()
print("txt drawer now:", sorted(p.name for p in (base / "txt").iterdir()))
