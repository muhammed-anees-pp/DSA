"""
Write a function to convert a string to uppercase.
"""
## Without inbuilt
def str_to_upper(str):
    result = ""
    for char in str:
        if 'a' <= char <= 'z':
            result += chr(ord(char) - 32)
        else:
            result += char
    return result

## With inbuilt
def to_uppercase(str):
    return str.upper()

# Example test case
print(str_to_upper("hello"))
print(to_uppercase("hello"))