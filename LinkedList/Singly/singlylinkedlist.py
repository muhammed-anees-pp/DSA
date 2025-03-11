"""
Singly linked list basic structure
"""
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class SinglyLinkedList:
    def __init__(self):
        self.head = None
    
    # for appending node
    def append(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
    
    # display singly linked list
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print(None)

sll = SinglyLinkedList()
sll.append(10)
sll.append(20)
sll.append(30)
sll.display()

# Output: 10 -> 20 -> 30 -> None