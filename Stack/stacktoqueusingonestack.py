"""
Queue implementation using a single stack with recursion
"""

class Queue:
    def __init__(self):
        # Initialize a single stack
        self.stack = []

    def enqueue(self, value):
        """
        Push the element to the stack.
        - This is a normal push operation.
        """
        self.stack.append(value)

    def dequeue(self):
        """
        Removes the front element using recursion.
        - Base Case: If only one element is left, pop it.
        - Recursive Case: Pop elements until reaching the first inserted one, then push them back.
        """
        if not self.stack:
            return "Empty"

        # Remove the last element
        top_element = self.stack.pop()

        if not self.stack:
            return top_element  # This was the first inserted element

        # Recursively remove the front element
        front = self.dequeue()

        # Push back the removed elements
        self.stack.append(top_element)

        return front

    def size(self):
        """
        Returns the number of elements in the queue.
        """
        return len(self.stack)

    def front(self):
        """
        Returns the front element using recursion.
        - Temporarily removes elements until reaching the first inserted one.
        - Pushes them back after retrieving the front.
        """
        if not self.stack:
            return "Empty"

        top_element = self.stack.pop()

        if not self.stack:
            front_element = top_element  # This is the first inserted element
        else:
            front_element = self.front()  # Keep removing until reaching the first element

        self.stack.append(top_element)  # Push elements back
        return front_element

    def is_empty(self):
        """
        Checks if the queue is empty.
        """
        return len(self.stack) == 0

    def display(self):
        """
        Displays the queue in correct order.
        - The queue is stored in reverse order, so we print it from first to last.
        """
        if not self.stack:
            print("Empty")
        else:
            print("Queue: ", self.stack)  # Print in correct order

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
print("Dequeued:", q.dequeue())  # Output: Dequeued: 10

# Displaying the queue after dequeue operation
q.display()  # Output: Queue: [20, 30, 40, 50]

# Printing the size of the queue after dequeue
print("Size: ", q.size())  # Output: Size: 4

# Printing the front element after dequeue
print("Front: ", q.front())  # Output: Front: 20
