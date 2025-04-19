class MinHeap:
    def __init__(self):
        self.heap = []
    
    # Insert
    def insert(self, value):
        self.heap.append(value)
        self.heapify_up(len(self.heap) - 1)
    
    # Heapify Up
    def heapify_up(self, ind):
        parent_ind = (ind - 1) // 2
        if ind > 0 and self.heap[parent_ind] > self.heap[ind]:
            self.heap[parent_ind], self.heap[ind] = self.heap[ind], self.heap[parent_ind]
            self.heapify_up(parent_ind)
    
    # Delete
    def delete(self):
        if not self.heap:
            return None
        
        if len(self.heap) == 1:
            return self.heap.pop()
        
        root_node = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)
        return root_node
    
    # Heapify Down
    def heapify_down(self,ind):
        smallest = ind
        left_child = (2*ind) + 1
        right_child = (2*ind) + 2
        if left_child < len(self.heap) and self.heap[smallest] > self.heap[left_child]:
            smallest = left_child
        if right_child < len(self.heap) and self.heap[smallest] > self.heap[right_child]:
            smallest = right_child
        if smallest != ind:
            self.heap[smallest], self.heap[ind] = self.heap[ind],self.heap[smallest]
            self.heapify_down(smallest)
    
    # Peek
    def peek(self):
        if not self.heap:
            return None
        return self.heap[0]
    
    # Size
    def size(self):
        if not self.heap:
            return 0
        return len(self.heap)
    
    # Clear
    def clear(self):
        self.heap = []
    
    # Check it empty
    def isEmpty(self):
        return len(self.heap) == 0
    
    # Display
    def get_heap(self):
        return self.heap

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
print(h.size())
print(h.isEmpty())
h.clear()
print(h.isEmpty())



"""
# Insert
    Elements = 50, 40, 70, 30, 20, 60

    Step 1: Insert 50
        Heap: []
        Add 50 → heap = [50]
        No parent → done
        ✅ Final: [50]

    Step 2: Insert 40
        Heap: [50]
        Add 40 → heap = [50, 40]
        Compare 40 with 50 → 40 < 50 → swap
        ✅ Final: [40, 50]

    Step 3: Insert 70
        Heap: [40, 50]
        Add 70 → heap = [40, 50, 70]
        Compare 70 with 40 → 70 > 40 → no swap
        ✅ Final: [40, 50, 70]

    Step 4: Insert 30
        Heap: [40, 50, 70]
        Add 30 → heap = [40, 50, 70, 30]
        Compare 30 with 50 → 30 < 50 → swap
        Now: [40, 30, 70, 50]
        Compare 30 with 40 → 30 < 40 → swap again
        ✅ Final: [30, 40, 70, 50]

    Step 5: Insert 20
        Heap: [30, 40, 70, 50]
        Add 20 → heap = [30, 40, 70, 50, 20]
        Compare 20 with 40 → 20 < 40 → swap
        Now: [30, 20, 70, 50, 40]
        Compare 20 with 30 → 20 < 30 → swap again
        ✅ Final: [20, 30, 70, 50, 40]

    Step 6: Insert 60
        Heap: [20, 30, 70, 50, 40]
        Add 60 → heap = [20, 30, 70, 50, 40, 60]
        Compare 60 with 70 → 60 < 70 → swap
        Now: [20, 30, 60, 50, 40, 70]
        Compare 60 with 20 → 60 > 20 → done
        ✅ Final: [20, 30, 60, 50, 40, 70]

    Heap:
              20
            /    \
          30      60
         /  \     /
        50   40  70

# Delete
    Initial heap: heap = [20, 30, 60, 50, 40, 70]
    We will now call the delete() function once. This removes the root (minimum) value and re-heapifies.

    Step 1: Start delete()
    self.heap = [20, 30, 60, 50, 40, 70]
    Not empty and length > 1 → continue
    Save root value: root_node = 20
    Replace root with last element: self.heap[0] = 70
    Remove last: self.heap.pop()
    Heap after swap & pop: [70, 30, 60, 50, 40]
    Call heapify_down(0)

    🔄 Step-by-Step heapify_down(0)
    📍 Iteration 1:
    ind = 0 → value = 70
    Left child index = 1 → value = 30
    Right child index = 2 → value = 60
    Smallest = 30 at index 1 → swap 70 with 30
    Heap becomes:
    [30, 70, 60, 50, 40]

    📌 Recursive call: heapify_down(1)
    📍 Iteration 2:
    ind = 1 → value = 70
    Left child index = 3 → value = 50
    Right child index = 4 → value = 40
    Smallest = 40 at index 4 → swap 70 with 40
    Heap becomes:
    [30, 40, 60, 50, 70]

    📌 Recursive call: heapify_down(4)
    📍 Iteration 3:
    ind = 4 → value = 70
    Left child index = 9 → out of bounds
    Right child index = 10 → out of bounds
    ✅ No swap needed → done
    Final Heap after delete():
    [30, 40, 60, 50, 70]

    Heap:
            30
          /    \
        40      60
       /  \
      50   70








"""