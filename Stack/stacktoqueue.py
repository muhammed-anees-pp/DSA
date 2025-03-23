"""
Stack to queue
"""

class Queue:
    def __init__(self):
        # Initialize two empty stacks
        self.stack1 = []  
        self.stack2 = []  

    def enque(self, data):
        # Move all elements from stack1 to stack2 (reverse order)
        while len(self.stack1) > 0:
            self.stack2.append(self.stack1.pop())  # Pop from stack1 and push to stack2
        
        # Push the new element into stack1
        self.stack1.append(data)
        
        # Move all elements back from stack2 to stack1 (restore order)
        while len(self.stack2) > 0:
            self.stack1.append(self.stack2.pop())  # Pop from stack2 and push to stack1

    def dequeue(self):
        # If stack1 is empty, print "Empty" (Queue is empty)
        if len(self.stack1) == 0:
            print("Empty")
            return
        
        # Remove the front element of the queue (top of stack1)
        self.stack1.pop()

    def display(self):
        # Print the current state of the queue
        print("Queue: ", self.stack1)

# Creating an instance of the queue
sq = Queue()

# Enqueuing elements into the queue
sq.enque(10)
sq.enque(20)
sq.enque(30)
sq.enque(40)

# Displaying the queue
sq.display()  # Output: Queue: [10, 20, 30, 40]

# Removing one element from the queue (dequeue)
sq.dequeue()

# Displaying the queue after dequeue operation
sq.display()  # Output: Queue: [20, 30, 40]