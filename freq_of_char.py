def freq_of_char(s):
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1

        else:
            freq[char] = 1
            # return char
    return freq

print(freq_of_char('swiss'))