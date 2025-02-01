def unique_list(nums):
    n = {}
    for i in nums:
        n[i] = n.get(i, 0) + 1
    for key, value in n.items():
        if value == 1:
            print(key, end=" ")


numbers = input("Numbers: ")
nums_list = list(map(int, numbers.split()))
unique_list(nums_list)