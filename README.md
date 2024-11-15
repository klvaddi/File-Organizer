# File-Organizer
Automatically organize files in any specified directory based on file type and date of creation.

## To Run
To install the required package, run the following command in the command line:

```bash
pip3 install watchdog
```

Navigate to the project directory and run the organizer.py script. Pass in a valid directory path relative to your root directory as an argument. Example:
```bash
python3 organizer.py desktop
```

While the script is running, any modifications made to your specified directory (such as adding a file) will result in organizing all files within that directory.
The organization directories are created as follows: File Type -> Year -> Month  

Terminate the script with `Ctrl + C`

## What I learned
- File and directory management via Python
- Use of libraries like shutil, pathlib, and watchdog
- Categories of various file extensions
- Accounting for compatibility on multiple systems
- Modular design strategies in Python
