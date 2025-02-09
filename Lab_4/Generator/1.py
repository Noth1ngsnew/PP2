def squares(n):
    list = []
    for i in range(n):
        s = (i+1)**2
        list.append(s)

    return list


N = int(input("Enter number: "))
square_list = squares(N)

for square in square_list:
    print(square, end=" ")