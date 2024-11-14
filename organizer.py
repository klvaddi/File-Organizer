import sys
from pathlib import Path
from time import sleep
from watchdog.observers import Observer
from event_handler import EventHandler

if __name__ == '__main__':
    # Process the directory to be organized
    if len(sys.argv) > 1:
        source_dir = Path.home() / sys.argv[1]
        if not source_dir.is_dir():
            print("Error: Invalid argument. Please provide a valid directory within /Users/loki/")
            sys.exit(1)
    else:
        print("Error: Missing argument. Please provide a valid directory within /Users/loki/")
        sys.exit(1)

    # Set up the observer to check for any changes (such as adding a file) in the source directory
    event_handler = EventHandler(source_dir)

    observer = Observer()
    observer.schedule(event_handler, f'{source_dir}', recursive=True)
    observer.start()

    try:
        while True:
            sleep(60)
    except KeyboardInterrupt:
        observer.stop()
    
    observer.join()