import os

def list_files(folder_path):
    files = []
    try:
        # Get files on PATH, and write (Folder) on the folders
        for file in os.listdir(folder_path+"/"):
            if os.path.isdir(folder_path+"/"+file):
                file=file+" (Folder)"
            files.append(file)

        # Return the list of files
        return files

    except FileNotFoundError:
        return f"Folder not found: {folder_path}"
    except PermissionError:
        return f"Permission denied: {folder_path}"

def go_back(folder_path):
    return os.path.dirname(folder_path)

# Replace 'folder_path_here' with the actual path of the folder you want to list files from.
#folder_path_here = "C:\Benaj\Desktop"
#list_files_in_folder(folder_path_here)
