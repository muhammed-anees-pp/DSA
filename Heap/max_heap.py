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
    
    # Delete Element
    def delete_element(self,value):
        if value not in self.heap:
            return False

        ind = self.heap.index(value)
        self.heap[ind] = self.heap[-1]
        self.heap.pop()

        if ind < len(self.heap):
            self.heapify_up(ind)
            self.heapify_down(ind)
        return True

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
    
    # Build Heap from a list
    def build_heap(self, arr):
        self.heap = list(arr)
        for i in range((len(self.heap) // 2) - 1, -1, -1):
            self.heapify_down(i)
    

    # Heap Sort
    def heap_sort(self):
        temp_heap = MaxHeap()
        temp_heap.build_heap(self.heap)

        sorted_list = []
        
        while temp_heap.heap:
            sorted_list.insert(0,temp_heap.delete())
        return sorted_list

    # Peek    
    def peek(self):
        if self.heap:
            return self.heap[0]
        else:
            return None
    
    # Search
    def search(self,value):
        if value in self.heap:
            return True
        else:
            return False
        
    # Find Kth Largest
    def find_kth_largest(self,k):
        if k > len(self.heap):
            return None
        
        temp_heap = MaxHeap()
        temp_heap.build_heap(self.heap)
        result = None

        for _ in range(k):
            result = temp_heap.delete()
        return result

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
        
h.build_heap([20, 30, 60, 50, 40, 70])
print("Heap after build:", h.get_heap())  # Should print a valid max heap


arr = [10, 20, 50, 30, 40, 90, 70, 100, 60, 80]
h.build_heap(arr)
print("Heap:", h.get_heap())
h.insert(110)
print("After insert 110:", h.get_heap())
print("Kth largest (3rd):", h.find_kth_largest(3))
print("Search 70:", h.search(70))
print("Delete 70:", h.delete_element(70))
print("After deleting 70:", h.get_heap())
print("Heap sort:", h.heap_sort())
        
        
        
        
        
        
        
        
        
        
    