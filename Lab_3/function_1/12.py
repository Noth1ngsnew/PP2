def histogram(nums):
    symbol = '*'
    for i in nums:
        print(i * symbol)
        
numbers = input("Numbers: ")
nums_list = list(map(int, numbers.split()))
histogram(nums_list)