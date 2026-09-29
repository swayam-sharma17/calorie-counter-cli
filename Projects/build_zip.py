from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED

ROOT = Path(__file__).resolve().parent
ZIP_PATH = ROOT.parent / "project_submission.zip"

with ZipFile(ZIP_PATH, "w", ZIP_DEFLATED) as archive:
    for path in ROOT.rglob("*"):
        if path.is_file() and path.name != "project_submission.zip":
            archive.write(path, path.relative_to(ROOT))

print(f"Created: {ZIP_PATH}")
