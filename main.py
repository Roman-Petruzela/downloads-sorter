import pathlib
import shutil

def get_downloads_path():
    downloads_path = pathlib.Path.home() / "Downloads"
    if downloads_path.exists():
        return downloads_path
    return None

def list_files(folder_path):
    if folder_path is not None:
        files = [f for f in folder_path.iterdir() if not (f.is_dir() and f.name.startswith("."))]
        return files
    return []

def get_extensions(files):
    extensions = []
    for f in files:
        if f.is_dir() and "folders" not in extensions:
            extensions.append("folders")
        if not f.suffix:
            continue
        if f.suffix not in extensions:
            extensions.append(f.suffix)
    return extensions

def make_folders(folder_path, extensions):
    folders = []
    for folder_name in extensions:
        folder = folder_path / folder_name
        folder.mkdir(parents=False, exist_ok=True)
        folders.append(folder)
    return folders

def move_files(files, folder_path):
    moved = 0
    for f in files:
        if f.is_dir():
            target_folder = folder_path / "folders"
            target = target_folder / f.name
            if target_folder.exists() and not target.exists():
                shutil.move(str(f), str(target))
                moved += 1
            continue
        ext = f.suffix
        if not ext:
            continue
        target_folder = folder_path / ext
        if target_folder.exists():
            target_file = target_folder / f.name
            if target_file.exists():
                continue
            shutil.move(str(f), str(target_file))
            moved += 1
    return moved

def main():
    try:
        downloads_path = get_downloads_path()
        print(f"Downloads path: {downloads_path}")
        if downloads_path is None:
            print("Downloads folder was not found.")
            return
        files = list_files(downloads_path)
        print(f"Files in downloads: {files}")
        extensions = get_extensions(files)
        print(f"Unique extensions in downloads: {extensions}")
        input("Press Enter to continue...")
        folders = make_folders(downloads_path, extensions)
        print(f"Folders made: {folders}")
        input("Press Enter to continue...")
        moved = move_files(files, downloads_path)
        print(f"Files moved: {moved}")
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
    input("Press Enter to exit...")