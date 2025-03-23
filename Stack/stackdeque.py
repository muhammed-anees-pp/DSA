"""
Stack using deque
"""


from collections import deque  # Importing deque from collections module

class StackQueue:
    def __init__(self):
        # Initialize an empty deque (double-ended queue) to use as a stack
        self.stack = deque()
    
    def push(self, data):
        # Adds an element to the top of the stack
        self.stack.append(data)
    
    def is_empty(self):
        # Returns True if the stack is empty, otherwise False
        return len(self.stack) == 0
    
    def peek(self):
        # Returns the top element without removing it
        if not self.is_empty():
            return self.stack[-1]  # Access the last element in the stack
        return "Empty"  # If stack is empty, return "Empty"
    
    def pop(self):
        # Removes and returns the top element of the stack
        if not self.is_empty():
            return self.stack.pop()  # Removes the last element (LIFO)
        return "Empty"  # If stack is empty, return "Empty"
    
    def display(self):
        # Prints the elements in the stack
        if not self.is_empty():
            print("Stack: ", list(self.stack))  # Convert deque to list for better readability
        else:
            print("Empty")  # If stack is empty, print "Empty"

# Creating an instance of StackQueue
sq = StackQueue()

# Pushing elements onto the stack
sq.push(10)
sq.push(20)
sq.push(30)
sq.push(40)

# Displaying stack contents
sq.display()  # Output: Stack: [10, 20, 30, 40]

# Getting the top element of the stack
print(sq.peek())  # Output: 40

# Removing the top element from the stack
sq.pop()

# Displaying stack after popping
sq.display()  # Output: Stack: [10, 20, 30]
