"""
Stack using linked list
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.count = 0
    
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self.count += 1
    
    def pop(self):
        if not self.top:
            return "Stack is empty"
        
        popped_data = self.top.data
        self.top = self.top.next
        self.count -= 1
        return popped_data
    
    def size(self):
        return self.count
    
    def display(self):
        temp = self.top
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print("")
        
# Example test case
s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.display()  
print("Popped:", s.pop()) 
s.display() 
print("Size: ", s.size())