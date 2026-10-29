"""
Problem statement
Given a string s, find the length of the longest substring without repeating characters.

A substring is a contiguous sequence of characters.

Example 1


text
Input:  s = "abcabcbb"
Output: 3
Explanation: "abc" is the longest substring
             without repeating characters.
Example 2


text
Input:  s = "bbbbb"
Output: 1
Explanation: "b" is the longest substring.
Example 3


text
Input:  s = "pwwkew"
Output: 3
Explanation: "wke" is the longest substring.

"""

def lengthOfLongeststring(s:str) -> int:
    last_seen = {}
    left = 0
    max_length = 0

    for right, char in enumerate(s):
        if char in last_seen and last_seen[char] >= left:
            left = last_seen[char] + 1

        last_seen[char] = right
        max_length = max(max_length, right - left + 1)

    return max_length

print(lengthOfLongeststring("pwwkew"))