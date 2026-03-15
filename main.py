from os import path
import pathlib
import shutil

def get_downloads_path():
    downloads_path = pathlib.Path.home() / "Downloads"
    if path.exists(downloads_path):
        return downloads_path
    return None

def list_files(path):
    if path is not None:
        files = [f for f in path.iterdir() if f.is_file()]
        return files
    return None

def get_extensions(files):
    extensions=[]
    for f in files:
        if f.suffix not in extensions:
            extensions.append(f.suffix)
    return extensions

def make_folders(path,extensions):
    folders = []
    for folder_name in extensions:
        folder = path / folder_name
        folder.mkdir(parents=False, exist_ok=True)
        folders.append(folder)
    return folders


def main():
    try:
        path = get_downloads_path()
        print(f"Downloads path: {path}")
        files = list_files(path)
        print(f"Files in downloads: {files}")
        extensions = get_extensions(files)
        print(f"Unique extensions in downloads: {extensions}")
        input("Press Enter to continue...")
        folders = make_folders(path, extensions)
        print(f"Folders made: {folders}")
        input("Press Enter to continue...")
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
    input("Press Enter to exit...")