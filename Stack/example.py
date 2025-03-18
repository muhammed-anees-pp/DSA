class Stack:
    def __init__(self):
        self.stack = []
    
    # Add elements
    def push(self, x):
        self.stack.append(x)
    
    # Check the array is empty or not
    def is_empty(self):
        return len(self.stack) == 0
    
    # Pop or remove last element
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return "Stack is empty"
    
    # Top element
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return "Stack is empty"
    
    # Display
    def display(self):
        print("Stack: ", self.stack)


# Example test case
st = Stack()
st.push(10)
st.push(20)
st.push(30)
st.display()
print("Top element: ", st.peek())
st.pop()
st.display()