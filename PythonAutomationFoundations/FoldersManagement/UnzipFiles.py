from pathlib import Path
import zipfile

root_dir = Path('.') # . is the same directory
destination_path = Path('destination')

for path in root_dir.glob("*.zip"):
  with zipfile.ZipFile(path, 'r') as zf:
    final_path = destination_path / Path(path.stem)
    zf.extractall(path=final_path)