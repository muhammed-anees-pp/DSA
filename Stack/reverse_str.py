"""
Reverse a string using stack
"""
# Method 1
def reverse_string(s):
    stack = []  
    
    # Push characters onto the stack
    for char in s:
        stack.append(char)  
    
    reversed_str = ""
    
    # Pop characters from the stack
    while stack:
        reversed_str += stack.pop()
    
    return reversed_str

# Example Usage
string = "hello"
print(reverse_string(string))  # Output: "olleh"


# Method 2
def reverse_str(str):    
    return str[::-1]

print(reverse_str("malayalam"))
print(reverse_str("anees"))