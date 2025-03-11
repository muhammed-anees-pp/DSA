"""
Write a function to find the first non-repeating character in a string.
"""
## Without inbuilt method
def non_repeating(str):
    for i in range(len(str)):
        find_duplicate = False
        for j in range(len(str)):
            if i != j and str[i] == str[j]:
                find_duplicate = True
                break
        if not find_duplicate:
            return str[i]

## With inbuilt method
from collections import Counter

def non_repeating_inbuilt(str):
    char_count = Counter(str)
    for char in str:
        if char_count[char] == 1:
            return char
    return None

# Example test case
print(non_repeating("swiss"))
print(non_repeating("racecar"))

print(non_repeating_inbuilt("swiss"))
print(non_repeating_inbuilt("racecar"))
