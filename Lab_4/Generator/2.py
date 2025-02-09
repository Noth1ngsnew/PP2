def check_even(n):
    result=[]
    for i in range(n):
        if i%2==0:
            result.append(i)
    return result

n=int(input("Enter number:"))
k=check_even(n)
print(k)