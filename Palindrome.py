def check_palindrome(s):
    result = ""
    for char in s:
        result = char + result
    return s == result

word = input("Enter you input:")
if check_palindrome(word):
    print("Palindrome")
else:
    print("Not a Palindrome")