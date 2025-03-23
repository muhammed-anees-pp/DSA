"""
Queue to stack
"""

class Stack:
    def __init__(self):
        """
        Initialize two empty queues.
        que1: This queue will always store the stack elements.
        que2: This queue is used as a temporary storage when pushing new elements.
        """
        self.que1 = []
        self.que2 = []
        
    def push(self, data):
        """
        Push an element onto the stack.
        - First, add the new element to que2.
        - Move all elements from que1 to que2 to maintain stack order (LIFO).
        - Swap que1 and que2, so que1 always holds the latest stack elements.
        """
        self.que2.append(data)  # Add new element to que2
        
        # Move all elements from que1 to que2
        while len(self.que1) > 0:
            self.que2.append(self.que1.pop(0))
        
        # Swap the queues, so que1 becomes the main queue
        self.que1, self.que2 = self.que2, self.que1  # Now que1 has elements in stack order
    
    def pop(self):
        """
        Remove and return the top element of the stack.
        - If que1 is empty, print "Empty".
        - Otherwise, remove the first element from que1 (which is the last pushed element).
        """
        if self.que1:
            return self.que1.pop(0)  # Remove and return the first element
        else:
            print("Empty")  # Stack is empty
            return None
    
    def display(self):
        """
        Display the current elements of the stack.
        - If que1 is empty, print "Empty".
        - Otherwise, print the contents of que1.
        """
        if self.que1:
            print("Stack:", self.que1)
        else:
            print("Empty")  # No elements in the stack

# Test the stack operations
s = Stack()

s.display()  # Output: Empty (stack is empty)

s.pop()  # Output: Empty (since stack has no elements)

s.push(10)
s.push(20)
s.push(30)

s.display()  # Output: Stack: [30, 20, 10] (LIFO order maintained)

s.pop()  # Removes 30 (last inserted element)

s.display()  # Output: Stack: [20, 10]

s.push(40)

s.display()  # Output: Stack: [40, 20, 10]
