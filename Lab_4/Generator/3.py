def DivisibleBy3and4(n):
    result=[]
    for i in range(n):
        if i%3==0 and i%4==0:
            result.append(i)
    return result

n=int(input("Enter number:"))
k=DivisibleBy3and4(n)
print(k)