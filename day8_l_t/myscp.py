import os

def main():
    folder_path = input("Enter the folder name: ").split()
    for folders in folder_path:
        try:
            fileslist = os.listdir(folders)
            print(f"list of files in folder: {folder_path}")
            for file in fileslist:
                print(file)
        except FileNotFoundError:
            print (f"No files in folder: {folder_path}")
        except PermissionError:
             print (f"Permission denied for folder: {folder_path}")
if __name__ == "__main__":
    main()