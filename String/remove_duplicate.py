"""
Write a function to remove duplicate characters from a string.
"""
## Without inbuilt method
def duplicate_remove(str):
    seen = set()
    result = ""
    for char in str:
        if char not in seen:
            result += char
            seen.add(char)
    return result

## With built in method
def remove_duplicates(str):
    return "".join(dict.fromkeys(str))


# Example Usage:
print(duplicate_remove("malayalam"))
print(remove_duplicates("malayalam"))
