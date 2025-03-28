"""
Queue implementation using two stacks
"""

class Queue:
    def __init__(self):
        # Initialize two empty stacks
        self.stack1 = []  
        self.stack2 = []  

    def enqueue(self, value):
        """
        Enqueue operation: Insert an element into the queue.
        - Move all elements from stack1 to stack2 (reverse order)
        - Push the new element into stack1
        - Move all elements back from stack2 to stack1 (restore order)
        """
        while len(self.stack1) > 0:
            self.stack2.append(self.stack1.pop())  # Pop from stack1 and push to stack2
        
        self.stack1.append(value)  # Push the new element into stack1
        
        while len(self.stack2) > 0:
            self.stack1.append(self.stack2.pop())  # Pop from stack2 and push to stack1

    def dequeue(self):
        """
        Dequeue operation: Remove the front element of the queue.
        - If queue is empty, return "Empty"
        - Otherwise, remove the top element of stack1
        """
        if not self.stack1:
            return "Empty"
        
        self.stack1.pop()  # Remove the front element

    def size(self):
        """
        Returns the number of elements in the queue.
        """
        return len(self.stack1)

    def front(self):
        """
        Returns the front element of the queue.
        - Since we maintain queue order in stack1, the last element is the front
        """
        return self.stack1[-1] if self.stack1 else "Empty"

    def is_empty(self):
        """
        Checks if the queue is empty.
        Returns True if empty, otherwise False.
        """
        return len(self.stack1) == 0

    def display(self):
        """
        Displays the elements of the queue in order.
        - Stack1 stores elements in reverse, so we print its reversed version
        """
        if not self.stack1:
            print("Empty")
        else:
            print("Queue: ", self.stack1[::-1])  # Print in correct order

# Creating an instance of the queue
q = Queue()

# Attempt to dequeue from an empty queue
print(q.dequeue())  # Output: Empty

# Enqueuing elements into the queue
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)

# Displaying the queue
q.display()  # Output: Queue: [10, 20, 30, 40, 50]

# Printing the size of the queue
print("Size: ", q.size())  # Output: Size: 5

# Printing the front element
print("Front: ", q.front())  # Output: Front: 10

# Removing one element from the queue (dequeue)
q.dequeue()

# Displaying the queue after dequeue operation
q.display()  # Output: Queue: [20, 30, 40, 50]

# Printing the size of the queue after dequeue
print("Size: ", q.size())  # Output: Size: 4

# Printing the front element after dequeue
print("Front: ", q.front())  # Output: Front: 20
