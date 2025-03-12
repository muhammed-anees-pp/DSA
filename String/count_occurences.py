"""
Write a function to count occurrences of a specific character in a string.
"""
## Without inbuilt
def count_char(str, char):
    count = 0
    for ch in str:
        if char == ch:
            count += 1
    return count
    
## With inbuilt
def count_character(str, char):
    return str.count(char)
    
# Example test case
print(count_char("hello", "l"))
print(count_character("hello", "l"))