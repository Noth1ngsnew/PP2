f = open("C:/Users/Sulpak/Downloads/Code/Lab_6/Directories and Files/myfile.txt","w")
txt = [123457, "hello", "byebye", False ]
text = ""
for i in txt:
    text += str(i)+"\n"
f.write(text)
f.close()