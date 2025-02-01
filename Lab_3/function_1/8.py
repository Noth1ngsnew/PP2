def spy_game(nums):
    n = []
    for i in range(len(nums)):
        if nums[i] == 0 or nums[i] == 7:
            n.append(nums[i])
    
    if n[0] == 0 and n[1] == 0 and n[2]==7:
        print(True)
    else:
        print(False)


        

numbers = input("Numbers: ")
nums_list = list(map(int, numbers.split()))
spy_game(nums_list)