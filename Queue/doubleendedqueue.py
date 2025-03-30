class Deque:
    def __init__(self, size):
        self.size = size  # Maximum size of deque
        self.queue = [None] * size  # Initialize deque with fixed size
        self.front = -1
        self.rear = -1

    # Check if the deque is full
    def is_full(self):
        return (self.rear + 1) % self.size == self.front

    # Check if the deque is empty
    def is_empty(self):
        return self.front == -1

    # Enqueue at the rear
    def enqueue_rear(self, value):
        if self.is_full():
            print("Deque is Full!")
            return
        if self.is_empty():  # First element insertion
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size  # Circular increment

        self.queue[self.rear] = value

    # Enqueue at the front
    def enqueue_front(self, value):
        if self.is_full():
            print("Deque is Full!")
            return
        if self.is_empty():  # First element insertion
            self.front = self.rear = 0
        else:
            self.front = (self.front - 1 + self.size) % self.size  # Circular decrement

        self.queue[self.front] = value

    # Dequeue from the front
    def dequeue_front(self):
        if self.is_empty():
            print("Deque is Empty!")
            return

        print(f"Deleted from Front: {self.queue[self.front]}")
        if self.front == self.rear:  # If only one element left
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size  # Circular increment

    # Dequeue from the rear
    def dequeue_rear(self):
        if self.is_empty():
            print("Deque is Empty!")
            return

        print(f"Deleted from Rear: {self.queue[self.rear]}")
        if self.front == self.rear:  # If only one element left
            self.front = self.rear = -1
        else:
            self.rear = (self.rear - 1 + self.size) % self.size  # Circular decrement

    # Display the deque
    def display(self):
        if self.is_empty():
            print("Deque is Empty!")
            return

        print("Deque:", end=" ")
        i = self.front
        while True:
            print(self.queue[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.size  # Circular increment
        print()


# Example Usage
dq = Deque(5)
dq.enqueue_rear(10)
dq.enqueue_rear(20)
dq.enqueue_front(5)
dq.enqueue_rear(30)
dq.enqueue_front(2)  # Should insert at the front
dq.display()  # Output: Deque: 2 5 10 20 30

dq.dequeue_front()
dq.display()  # Output: Deque: 5 10 20 30

dq.dequeue_rear()
dq.display()  # Output: Deque: 5 10 20

dq.enqueue_rear(40)
dq.enqueue_front(1)
dq.display()  # Output: Deque: 1 5 10 20 40
