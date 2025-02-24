import os

path = "C:/Users/Sulpak/Desktop/Blender/Ponchik.blend1"

if os.path.exists(path):
    os.remove(path)
else:
    print("The file does not exist")
