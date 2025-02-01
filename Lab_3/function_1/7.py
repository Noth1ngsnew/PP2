def has_33(nums):
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
            print(True)
            return
    print(False)

numbers = input("Numbers: ")
nums_list = list(map(int, numbers.split()))
has_33(nums_list)