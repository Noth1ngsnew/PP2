def naoborot(str):
    n = str.split()
    n.reverse()
    for i in range(len(n)):
        print(n[i], end = " ")
    

string = input("Sentence: ")
naoborot(string)