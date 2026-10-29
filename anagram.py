s1 = "silent"
s2 = "listen"

check_anagram = ["Yes" if sorted(s1) == sorted(s2) else "No"]
print(check_anagram)