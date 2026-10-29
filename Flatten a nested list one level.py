nested = [[1,2],[2,3],[4,5]]

list = [item for items in nested for item in items ]

print(list)