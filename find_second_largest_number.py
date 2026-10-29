def find_second_largest_number(s):
    second = float("-inf")
    largest = float("-inf")
    for s in s:
        if s > largest:
            second = largest
            largest = s
        elif s > second and s !=  largest:
            second = s
    return second

print(find_second_largest_number([10,20,10,30,40,50]))