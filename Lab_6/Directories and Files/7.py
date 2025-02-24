f = open("C:/Users/Sulpak/Downloads/Code/Lab_6/Directories and Files/myfile.txt","r")
txt = f.read()
f.close()

p = open("C:/Users/Sulpak/Downloads/Code/Lab_6/Directories and Files/betafile.txt",'w')
p.write(txt)
p.close()