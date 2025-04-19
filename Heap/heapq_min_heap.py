import heapq

class MinHeap:
    def __init__(self):
        self.heap = []
    
    # Insert
    def insert(self,value):
        heapq.heappush(self.heap,value)
    
    # Delete
    def delete(self):
        if not self.heap:
            return None
        return heapq.heappop(self.heap)
    
    # Peek
    def peek(self):
        if not self.heap:
            return None
        
        return self.heap[0]
    
    # Display
    def get_heap(self):
        return self.heap
        
    # Build heap
    def build_heap(self,arr):
        self.heap = arr
        heapq.heapify(self.heap)
        
    # Heap Sort
    def heap_sort(self):
        sorted_list = []
        while self.heap:
            sorted_list.append(heapq.heappop(self.heap))
        return sorted_list
        
        
h = MinHeap()
h.insert(50)
h.insert(40)
h.insert(70)
h.insert(30)
h.insert(20)
h.insert(60)
print(h.get_heap())
h.delete()
print(h.get_heap())
print(h.peek())

# Building heap from list
h.build_heap([3, 1, 5, 10, 2])

# Heap Sort
print("Heap Sort Result:", h.heap_sort())