import os

def list_files_and_folders(folder_path):
    files = []
    folders = []
    status = "none"
    try:
        # Get files and folders on PATH
        #for file_or_folder in os.listdir(folder_path+"/"):
        #    if os.path.isdir(folder_path+"/"+file_or_folder):
        #        folders.append(file_or_folder)

        items = os.listdir(folder_path+"/")

        files = [item for item in items if not os.path.isdir(folder_path+"/"+item)]
        folders = [item for item in items if os.path.isdir(folder_path+"/"+item)]

        # Return the list of files
        status = "ok"
        return status,files,folders

    except FileNotFoundError:
        status = "not-found"
        return status,files,folders
    except PermissionError:
        status = "denied"
        return status,files,folders

def go_back(folder_path):
    return os.path.dirname(folder_path)

# Replace 'folder_path_here' with the actual path of the folder you want to list files from.
#folder_path_here = "C:\Benaj\Desktop"
#list_files_in_folder(folder_path_here)
