def reverse_list(n):
    result=[]
    for i in range(n,-1,-1):
        result.append(i)
    return result

n=int(input("Enter number:"))
k=reverse_list(n)
print(k)