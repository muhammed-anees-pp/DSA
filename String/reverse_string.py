"""
Write a function to reverse a given string.
"""
## Without inbuilt method
def reverse_str(s):
    reverse = ""
    for char in s:
        reverse = char + reverse
    
    return reverse


## With inbuilt method
def reverse_string(s):
    return s[::-1]


# Example Usage:
print(reverse_str("Hello"))
print(reverse_string("Hello world"))