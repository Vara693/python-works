import os
import shutil

folder_path = r"Enter_path_here"
for file in os.listdir(folder_path):
    if file.endswith(".jpg") or file.endswith(".png"):
        shutil.move(f"{folder_path}/{file}", f"{folder_path}/images/{file}")
    elif file.endswith(".mp4"):
        shutil.move(f"{folder_path}/{file}", f"{folder_path}/videos/{file}")


print("files moved successfully")
