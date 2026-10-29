def move_zero(nums):
    result = [x for x in nums if x != 0]
    zeros = [x for x in nums if x == 0]

    return  result + zeros


nums = [0, 1, 0, 3, 12]
print(move_zero(nums))