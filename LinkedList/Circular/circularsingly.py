"""
Circular singly linked list basic structure
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class CircularSingly:
    def __init__(self):
        self.head = None
        
    def append(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return
        
        last = self.head
        while last.next != self.head:
            last = last.next
        last.next = new_node
        new_node.next = self.head
        
    def display(self):
        if not self.head:
            print("List is empty")
            return
        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("Back to head")


# Example usage
csl = CircularSingly()
csl.append(10)
csl.append(20)
csl.append(30)
csl.append(40)
csl.display()

# Output: 10 -> 20 -> 30 -> 40 -> Back to head