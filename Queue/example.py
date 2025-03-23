"""
Queue strucuture
"""

class Queue:
    def __init__(self):
        self.queue = []
    
    # Add item to the back of the queue
    def enqueue(self, item):
        self.queue.append(item)
    
    # Remove item from the front of the queue
    def dequeue(self):
        if len(self.queue) > 0:
            return self.queue.pop(0)
        else:
            return "Queue is empty"
    
    # View the front element without removing it
    def peek(self):
        if len(self.queue) > 0:
            return self.queue[0]
        else:
            return "Queue is empty"
            
    # Check if the queue is empty
    def is_empty(self):
        return len(self.queue) == 0
    
    
    # Get the size of the queue
    def size(self):
        return len(self.queue)
    
    # Display
    def display(self):
        return print("Queue: ", self.queue)

# Example test case        
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()
print(q.dequeue())
q.display()
print(q.peek())
print("Size of the queue: ", q.size())







