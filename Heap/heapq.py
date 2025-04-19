import heapq

# 1. Convert a list into a heap
heap = [20, 30, 60, 50, 40, 70]
heapq.heapify(heap)  # Converts the list into a min-heap

# 2. Push an element into the heap
heapq.heappush(heap, 10)

# 3. Pop the smallest element from the heap
smallest = heapq.heappop(heap)

# 4. Push and pop in one step (more efficient)
val = heapq.heappushpop(heap, 25)

# 5. Get the smallest element without popping
min_value = heap[0]
