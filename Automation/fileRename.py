import os
from pathlib import Path


def renameFolder(path, pattern):
    file_path = Path(path)

    for count, filename in enumerate(os.listdir(file_path)):
        # if count < 3:
        #     continue
        name, ext = os.path.splitext(filename)
        new_name = f"{pattern}_{count+1}{ext}"

        old_path = os.path.join(file_path, filename)
        new_path = os.path.join(file_path, new_name)

        os.rename(old_path, new_path)

    print("file renamed successfully!")




path = input("Enter the path of to the folder: ")
pattern = input("Input pattern of the files name: ")

renameFolder(path, pattern)
print("images have been renamed")