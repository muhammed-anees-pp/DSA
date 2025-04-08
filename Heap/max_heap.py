class MaxHeap:
    def __init__(self) -> None:
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, idx):
        parent_idx = (idx - 1)//2
        if idx > 0 and self.heap[parent_idx] < self.heap[idx]:
            self.heap[parent_idx], self.heap[idx] = self.heap[idx], self.heap[parent_idx]
            self._heapify_up(parent_idx)

    def delete(self):
        if not self.heap:
            return False
        if len(self.heap) == 1:
            return self.heap.pop()
        del_node = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return del_node

    def _heapify_down(self, idx):
        large_idx = idx
        left_idx = 2 * idx + 1
        right_idx = 2 * idx + 2
        if left_idx < len(self.heap) and self.heap[large_idx] < self.heap[left_idx]:
            large_idx = left_idx
        if right_idx < len(self.heap) and self.heap[large_idx] < self.heap[right_idx]:
            large_idx = right_idx
        if large_idx != idx:
            self.heap[large_idx], self.heap[idx] = self.heap[idx], self.heap[large_idx]
            self._heapify_down(large_idx)

    def peek(self):
        if self.heap:
            return self.heap[0]
        else:
            return None

    def get_heap(self):
        return self.heap

    def clear(self):
        self.heap = []

    def get_size(self):
        return len(self.heap)

    def isEmpty(self):
        return len(self.heap) == 0


max_heap = MaxHeap()
max_heap.insert(10)
max_heap.insert(20)
max_heap.insert(30)
max_heap.insert(4)
max_heap.insert(25)
heap_values = max_heap.get_heap()
print(heap_values)
max_heap.delete()
heap_values = max_heap.get_heap()
print(heap_values)
print(max_heap.get_size())
print(max_heap.peek())