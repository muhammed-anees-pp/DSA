class MinHeap:
    def __init__(self):
        self.heap = []
    
    def insert(self, value):
        self.heap.append(value)
        self.heapify_up(len(self.heap) - 1)
    
    def heapify_up(self, ind):
        parent_ind = (ind - 1) // 2
        if ind > 0 and self.heap[parent_ind] > self.heap[ind]:
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
        smallest = ind
        left_child = (2 * ind) + 1
        right_child = (2 * ind) + 2
        if left_child < len(self.heap) and self.heap[smallest] > self.heap[left_child]:
            smallest = left_child
        if right_child < len(self.heap) and self.heap[smallest] > self.heap[right_child]:
            smallest = right_child
        if smallest != ind:
            self.heap[smallest], self.heap[ind] = self.heap[ind], self.heap[smallest]
            self.heapify_down(smallest)
    
    def peek(self):
        if not self.heap:
            return None
        return self.heap[0]
    
    def size(self):
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

# Given Max Heap (just a sample)
max_heap = [70, 50, 60, 30, 40, 20]

print("Original Max-Heap:", max_heap)

# Convert Max-Heap to Min-Heap
min_heap = MinHeap()
min_heap.build_heap(max_heap)

print("Converted Min-Heap:", min_heap.get_heap())
