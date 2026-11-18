# CLI File Organizer

A Python command-line tool that automatically sorts cluttered directories (like your Downloads folder!) into clean, categorized subfolders based on file extensions.

## Features
* **Zero External Dependencies:** Built entirely with Python's standard library (`pathlib`, `shutil`, `argparse`).
* **Smart Categorization:** Automatically groups files into `Images`, `Documents`, `Archives`, `Installers`, and `Other`.
* **Safe Execution:** Skips existing subdirectories and hidden system files to prevent accidental folder nesting.
* **Flexible CLI:** Supports custom target paths, shorthand flags, and home directory expansion (`~`).

## Requirements
* Python 3.6 or higher

## Usage

Clone the repository and navigate into the project folder:
```bash
git clone https://github.com
cd cli-file-organizer
```

### Organize a specific folder
```bash
python organizer.py --path ~/Downloads
```
*(You can also use the `-p` shorthand flag: `python organizer.py -p ~/Downloads`)*

### Organize the current directory
Running the script without arguments defaults to your current working directory:
```bash
python organizer.py
```

### View the help menu
```bash
python organizer.py --help
```

## Example Output
```text
\$ python organizer.py --path ~/Downloads
Moved: resume_final.pdf -> Documents/
Moved: vacation_photo.jpg -> Images/
Moved: project_archive.zip -> Archives/
Moved: setup_wizard.dmg -> Installers/
```

## Future Improvements
* Add a `--dry-run` flag to preview file movements before executing them.
* Support custom category mappings via a JSON configuration file.
* Add an `--undo` feature using a local log file.
