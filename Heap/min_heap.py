class MinHeap:
    def __init__(self) -> None:
        self.heap = []

    def insert(self, val):
        self.heap.append(val)
        self.heapify_up(len(self.heap) - 1)

    def heapify_up(self, idx):
        parent_idx = (idx - 1) // 2
        if idx > 0 and self.heap[parent_idx] > self.heap[idx]:
            self.heap[parent_idx], self.heap[idx] = self.heap[idx], self.heap[parent_idx]
            self.heapify_up(parent_idx)

    def delete(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        root_node = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)
        return root_node

    def heapify_down(self, index):
        smallest = index
        left_child = (2*index) + 1
        right_child = (2*index) + 2
        if left_child < len(self.heap) and self.heap[smallest] > self.heap[left_child]:
            smallest = left_child
        if right_child < len(self.heap) and self.heap[smallest] > self.heap[right_child]:
            smallest = right_child
        if smallest != index:
            self.heap[smallest], self.heap[index] = self.heap[index], self.heap[smallest]
            self.heapify_down(smallest)

    def peek(self):
        if not self.heap:
            return None
        return self.heap[0]

    def size(self):
        return len(self.heap)

    def get_heap(self):
        return self.heap

    def clear(self):
        self.heap = []

    def isEmpty(self):
        return len(self.heap) == 0