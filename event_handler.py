import shutil
from pathlib import Path
from datetime import datetime
from extensions import extension_paths
from watchdog.events import FileSystemEventHandler

# Adds year and month directories to destination path
def addDate(file: Path, destination_path: Path):
    # Find the time of file creation depending on OS
    if hasattr(file.stat(), 'st_birthtime'):
        creation_time = file.stat().st_birthtime 
    else:
        creation_time = file.stat().st_ctime
    
    # Extract the year and month
    creation_date = datetime.fromtimestamp(creation_time)
    year = str(creation_date.year)
    month = creation_date.strftime("%B")

    # Create directories with year and month if they do not already exist
    dated_path = destination_path / year / month
    dated_path.mkdir(parents=True, exist_ok=True)
    return dated_path

# Renames file if it already exists in the destination directory
def renameFile(file: Path, destination_path: Path):
    new_name = destination_path / file.name
    i = 1

    while new_name.exists():
        new_name = destination_path / f'{file.stem}_{i}{file.suffix}'
        i += 1
    
    return new_name


class EventHandler(FileSystemEventHandler):
    def __init__(self, source_dir: Path):
        self.source_dir = source_dir.resolve()
    
    # This function will execute when there is a change in the source directory
    def on_modified(self, event):
        # Move each file in the source directory to its appropraite destination
        for entry in self.source_dir.iterdir():
            if entry.is_file() and entry.suffix.lower() in extension_paths:
                destination_path = self.source_dir / extension_paths[entry.suffix.lower()]
                destination_path = addDate(entry, destination_path)
                destination_path = renameFile(entry, destination_path)
                shutil.move(entry, destination_path)  