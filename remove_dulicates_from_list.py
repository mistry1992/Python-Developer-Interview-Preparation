def remove_duplicates(s):
    list = []
    for element in s:
        if element not in list:
            list.append(element)
    return list

print(remove_duplicates([20,20,30,30,40]))