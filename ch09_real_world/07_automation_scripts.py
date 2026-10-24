"""9.7 Automating boring tasks.

Real-world comparison: a dishwasher. Washing one plate by hand is
quick; washing 500 every day is not. A short script does the same
dull job on hundreds of files in a second, without mistakes.

This script creates a messy "Downloads" folder of demo files, then
renames them with dates and sorts them into folders by type.
"""

import shutil
from datetime import date
from pathlib import Path

downloads = Path(__file__).parent / "output" / "Downloads"
if downloads.exists():
    shutil.rmtree(downloads)
downloads.mkdir(parents=True)

messy = ["IMG 001.JPG", "Invoice  Oct.PDF", "song final(1).mp3",
         "notes.TXT", "holiday photo.jpeg", "report draft.docx"]
for name in messy:
    (downloads / name).write_text("demo", encoding="utf-8")

CATEGORIES = {
    "images": {".jpg", ".jpeg", ".png"},
    "documents": {".pdf", ".docx", ".txt"},
    "music": {".mp3", ".wav"},
}


def category_for(suffix):
    for folder, suffixes in CATEGORIES.items():
        if suffix in suffixes:
            return folder
    return "other"


def clean_name(stem):
    # lower case, spaces and brackets to single underscores
    cleaned = "".join(c if c.isalnum() else "_" for c in stem.lower())
    return "_".join(part for part in cleaned.split("_") if part)


today = date(2026, 10, 24).isoformat()
moved = 0
for file in sorted(downloads.iterdir()):
    if not file.is_file():
        continue
    suffix = file.suffix.lower()
    target_dir = downloads / category_for(suffix)
    target_dir.mkdir(exist_ok=True)
    new_name = f"{today}_{clean_name(file.stem)}{suffix}"
    file.rename(target_dir / new_name)
    print(f"{file.name:22} -> {target_dir.name}/{new_name}")
    moved += 1

print(f"Organised {moved} files.")
