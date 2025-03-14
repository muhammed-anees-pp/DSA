"""
Sorting
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
        
    # sort
    def sort(self):
        if not self.head or not self.head.next:
            return
        swapped = True
        while swapped:
            swapped = False
            current = self.head
            while current.next:
                if current.data > current.next.data:
                    current.data, current.next.data = current.next.data, current.data
                    swapped = True
                current = current.next
        
    # display singly linked list
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print(None)

ll = SinglyLinkedList()
ll.append(30)
ll.append(10)
ll.append(40)
ll.append(20)

print("Before sorting:")
ll.display()

ll.sort()

print("After sorting:")
ll.display()

# Output: 10 -> 20 -> 30 -> None