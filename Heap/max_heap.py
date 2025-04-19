class MaxHeap:
    def __init__(self):
        self.heap = []
    
    # Insert
    def insert(self,value):
        self.heap.append(value)
        self.heapify_up(len(self.heap) - 1)
    
    # Heapify up
    def heapify_up(self,ind):
        parent_ind = (ind - 1) // 2
        if ind > 0 and self.heap[parent_ind] < self.heap[ind]:
            self.heap[parent_ind], self.heap[ind] = self.heap[ind], self.heap[parent_ind]
            self.heapify_up(parent_ind)
    
    # Delete
    def delete(self):
        if not self.heap:
            return False
        
        if len(self.heap) == 1:
            return self.heap.pop()
        
        root_node = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)
        return root_node
    
    # Heapify Down
    def heapify_down(self,ind):
        largest = ind
        left = (2*ind) + 1
        right = (2*ind) + 2
        if left < len(self.heap) and self.heap[largest] < self.heap[left]:
            largest = left
        if right < len(self.heap) and self.heap[largest] < self.heap[right]:
            largest = right
        
        if largest != ind:
            self.heap[largest], self.heap[ind] = self.heap[ind],self.heap[largest]
            self.heapify_down(largest)
    # Peek    
    def peek(self):
        if self.heap:
            return self.heap[0]
        else:
            return None
    
    # Clear
    def clear(self):
        self.heap = []
    
    # Size
    def get_size(self):
        return len(self.heap)
    
    # Empty Check
    def isEmpty(self):
        return len(self.heap) == 0
    
    # Display
    def get_heap(self):
        return self.heap
        
h = MaxHeap()
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
print(h.get_size())
print(h.isEmpty())
h.clear()
print(h.isEmpty())
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    