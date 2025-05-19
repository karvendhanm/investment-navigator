from logger import logger
from pathlib import Path
from typing import List


def get_file_paths(directory: str, extension: str) -> List[str]:
    """
    Find all the absolute file paths of a specific extension inside the given directory.
    logging errors to a file with the origination line number.

    :param directory: The path to the directory to search for.
    :param extension: The file extension to filter by (e.g., ".txt").
    :return: A list of absolute file paths for the matching extension.
             Returns an empty if the directory is not found or access is denied.
    :raises TypeError: if directory or extension is not a string.
    """
    if not isinstance(directory, str):
        raise TypeError("directory must be a string")
    if not isinstance(extension, str):
        raise TypeError("extension must be a string")

    path = Path(directory)
    files: List[str] = []
    try:
        for item in path.iterdir():
            if item.is_file() and item.suffix.lower() == extension.lower():
                files.append(str(item.resolve()))
    except PermissionError:
        logger.error(f"Permission denied to access directory: {directory}.")
    except FileNotFoundError:
        logger.error(f"Directory not found: {directory}.")
    return files


if __name__ == "__main__":
    print(get_file_paths('./data', '.pdf'))

