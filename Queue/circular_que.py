"""
Circular que using List
"""
class CircularQueue:
    def __init__(self, size):
        self.size = size  # Maximum size of queue
        self.queue = [None] * size  # Initialize a fixed-size list
        self.front = self.rear = -1  # Both pointers start at -1

    # Enqueue operation
    def enqueue(self, value):
        if (self.rear + 1) % self.size == self.front:  # Check if the queue is full
            print("Queue is Full!")
            return

        if self.front == -1:  # First element insertion
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size  # Circular increment

        self.queue[self.rear] = value  # Insert value

    # Dequeue operation
    def dequeue(self):
        if self.front == -1:  # Check if the queue is empty
            print("Queue is Empty!")
            return

        print(f"Deleted: {self.queue[self.front]}")
        if self.front == self.rear:  # If only one element is left
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size  # Circular increment

    # Display queue
    def display(self):
        if self.front == -1:
            print("Queue is Empty!")
            return

        print("Circular Queue:", end=" ")
        i = self.front
        while True:
            print(self.queue[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.size  # Circular increment
        print()

# Example Usage
cq = CircularQueue(5)
cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.enqueue(40)
cq.display()  # Output: Circular Queue: 10 20 30 40
cq.dequeue()
cq.display()  # Output: Circular Queue: 20 30 40
cq.enqueue(50)
cq.enqueue(60)  # It should insert at the beginning due to circular nature
cq.display()  # Output: Circular Queue: 20 30 40 50 60
cq.enqueue(70)  # Should print "Queue is Full!"
