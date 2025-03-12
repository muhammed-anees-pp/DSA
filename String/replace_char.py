"""
Write a function to replace all occurrences of a given character in a string.
"""
## Without inbuilt
def replace_char(str, old, new):
    result = ""
    for char in str:
        if char == old:
            result += new
        else:
            result += char
    return result


## With inbuilt
def replace_characters(str, old, new):
    return str.replace(old, new)


# Example test case
print(replace_char("banana", "a", "o"))
print(replace_characters("apple", "p", "q"))