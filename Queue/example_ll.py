"""
Queue using linked list
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class Queue:
    def __init__(self):
        self.start = self.end = None
    
    def enqueue(self, data):
        new_node = Node(data)
        if not self.end:
            self.start = self.end = new_node
            return
        self.end.next = new_node
        self.end = new_node
    
    def dequeue(self):
        if not self.start:
            return "Queue is empty"
        dequeued_data = self.start.data
        self.start = self.start.next
        if not self.start:
            self.end = None
        return dequeued_data
    
    def display(self):
        temp = self.start
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print("")


# Example test case
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()  
print("Dequeued:", q.dequeue())  
q.display()