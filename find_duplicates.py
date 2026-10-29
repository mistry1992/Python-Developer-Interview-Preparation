def find_duplicates(s):
    seen = set()
    list = []

    for element in s:
        if element in seen:
            if element not in list:
                list.append(element)
        else:
            seen.add(element)
    return list

print(find_duplicates([1, 2, 3, 2, 4, 1, 5]))