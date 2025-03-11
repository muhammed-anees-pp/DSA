"""
Reverse a string using recursion.
"""
def reverse_string(str):
    if len(str) == 0:
        return ""
    
    return str[-1] + reverse_string(str[:-1])
    
    
# Example test case
s="Hello"
print(reverse_string(s))