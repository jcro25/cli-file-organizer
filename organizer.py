import argparse
import shutil
from pathlib import Path

FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".svg"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".csv"],
    "Archives": [".zip", ".tar", ".gz", ".rar"],
    "Installers": [".exe", ".dmg", ".pkg", ".deb"],
}


def get_category(extension: str) -> str:
    """Return the folder name matching the file extension."""
    for category, extensions in FILE_CATEGORIES.items():
        if extension.lower() in extensions:
            return category
    return "Other"


def organize_directory(target_path: str) -> None:
    """Sort files in the target directory into categorized subfolders."""
    directory = Path(target_path).expanduser().resolve()

    if not directory.exists() or not directory.is_dir():
        print(f"Error: '{target_path}' is not a valid directory.")
        return

    for item in directory.iterdir():
        if item.is_dir() or item.name.startswith("."):
            continue

        category = get_category(item.suffix)
        destination_folder = directory / category
        destination_folder.mkdir(exist_ok=True)

        try:
            shutil.move(str(item), str(destination_folder / item.name))
            print(f"Moved: {item.name} -> {category}/")
        except Exception as e:
            print(f"Could not move {item.name}: {e}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Organize files in a directory into categorized subfolders."
    )
    parser.add_argument(
        "-p",
        "--path",
        type=str,
        default=".",
        help="Path to the target directory (defaults to current folder)",
    )

    args = parser.parse_args()
    organize_directory(args.path)


if __name__ == "__main__":
    main()
