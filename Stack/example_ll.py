class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
    
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
    
    def pop(self):
        if not self.top:
            return "Stack is empty"
        
        popped_data = self.top.data
        self.top = self.top.next
        return popped_data
    
    def display(self):
        temp = self.top
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")
        
# Example test case
s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.display()  
print("Popped:", s.pop()) 
s.display() 