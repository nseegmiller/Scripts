import os
import sys

def delete_json_and_empty_dirs(root_path):
    """
    Recursively navigates through all subdirectories in the given root path,
    deletes .json files, and removes empty directories.

    Args:
        root_path (str): The root directory path to process.
    """
    for dirpath, dirnames, filenames in os.walk(root_path, topdown=False):
        # Delete .json files in the current directory
        for file in filenames:
            if file.endswith(".json") or file.endswith(".dll") or file.endswith(".glb"):
                file_path = os.path.join(dirpath, file)
                try:
                    os.remove(file_path)
                    print(f"Deleted file: {file_path}")
                except Exception as e:
                    print(f"Error deleting file {file_path}: {e}")

        # Remove empty directories
        if not os.listdir(dirpath):
            try:
                os.rmdir(dirpath)
                print(f"Removed empty directory: {dirpath}")
            except Exception as e:
                print(f"Error removing directory {dirpath}: {e}")

def main():
    # Ensure the script is called with the correct number of arguments
    if len(sys.argv) != 2:
        print("Usage: python delete_json_and_empty_dirs.py <root_path>")
        sys.exit(1)

    root_path = sys.argv[1]

    # Check if the provided path exists and is a directory
    if not os.path.isdir(root_path):
        print(f"Error: The provided path '{root_path}' is not a valid directory.")
        sys.exit(1)

    # Start processing the directory
    delete_json_and_empty_dirs(root_path)

if __name__ == "__main__":
    main()