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