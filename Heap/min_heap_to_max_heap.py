class MaxHeap:
    def __init__(self):
        self.heap = []
    
    def insert(self, value):
        self.heap.append(value)
        self.heapify_up(len(self.heap) - 1)
    
    def heapify_up(self, ind):
        parent_ind = (ind - 1) // 2
        if ind > 0 and self.heap[parent_ind] < self.heap[ind]:
            self.heap[parent_ind], self.heap[ind] = self.heap[ind], self.heap[parent_ind]
            self.heapify_up(parent_ind)
    
    def delete(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        root_node = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)
        return root_node
    
    def heapify_down(self, ind):
        largest = ind
        left = (2 * ind) + 1
        right = (2 * ind) + 2
        if left < len(self.heap) and self.heap[largest] < self.heap[left]:
            largest = left
        if right < len(self.heap) and self.heap[largest] < self.heap[right]:
            largest = right
        if largest != ind:
            self.heap[largest], self.heap[ind] = self.heap[ind], self.heap[largest]
            self.heapify_down(largest)
    
    def peek(self):
        return self.heap[0] if self.heap else None
    
    def get_size(self):
        return len(self.heap)
    
    def clear(self):
        self.heap = []
    
    def isEmpty(self):
        return len(self.heap) == 0
    
    def get_heap(self):
        return self.heap
    
    def build_heap(self, arr):
        self.heap = list(arr)
        for i in range((len(self.heap) // 2) - 1, -1, -1):
            self.heapify_down(i)

# ----------------------------

# Given Min Heap (sample input)
min_heap = [10, 20, 15, 30, 40]

print("Original Min-Heap:", min_heap)

# Convert Min-Heap to Max-Heap
max_heap = MaxHeap()
max_heap.build_heap(min_heap)

print("Converted Max-Heap:", max_heap.get_heap())
