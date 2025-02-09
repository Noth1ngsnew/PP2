def squares(n,k):
    list = []
    for i in range(n,k+1):
        s = i**2
        list.append(s)

    return list


n = int(input("Enter number: "))
k = int(input("Enter number: "))
square_list = squares(n,k)

for square in square_list:
    print(square, end=" ")