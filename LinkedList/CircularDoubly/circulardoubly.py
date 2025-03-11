"""
Circular doubly linked list basic structure
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
class CircularDoubly:
    def __init__(self):
        self.head = None
    
    def append(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            new_node.prev = self.head
            return 
        last = self.head.prev
        last.next = new_node
        new_node.prev = last
        new_node.next = self.head
        self.head.prev = new_node
        
    def display(self):
        if not self.head:
            print("Empty list")
            return
        temp = self.head
        while True:
            print(temp.data, end = " <-> ")
            temp = temp.next
            if temp == self.head:
                break
        print("Back to head")

cdl = CircularDoubly()
cdl.append(10)
cdl.append(20)
cdl.append(30)
cdl.append(40)
cdl.display()

# Output: 10 <-> 20 <-> 30 <-> 40 <-> Back to head