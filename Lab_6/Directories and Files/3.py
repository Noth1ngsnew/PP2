import os 

path = "C:/Users/Sulpak/Desktop/Blender"

existence = os.access(path, os.F_OK)
if existence == True:
    file_name = os.path.basename(path)
    dir_name = os.path.dirname(path)
    print("File name:",file_name)
    print("Directory portion:",dir_name)
else:
    print("Path doesn't exist")
    