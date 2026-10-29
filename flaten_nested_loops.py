# arr = [1, [2, [3, 4], 5], 6]
def flatten_arr(arr):
    return [x for sub in arr for x in (flatten_arr(sub) if isinstance(sub, list) else [sub])]

print(flatten_arr([1, [2, [3, 4], 5], 6]))