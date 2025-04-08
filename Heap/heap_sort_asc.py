def heapify(arr, n, i):
    largest = i
    left_node = i*2 + 1
    right_node = i*2 + 2
    if left_node < n and arr[left_node] > arr[largest]:
        largest = left_node
    if right_node < n and arr[right_node] > arr[largest]:
        largest = right_node
    if largest != i:
        arr[largest], arr[i] = arr[i], arr[largest]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)
    ran = (len(arr) // 2) - 1
    for i in range(ran, -1, -1):
        heapify(arr, n, i)
    print(arr)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


arr = [4, 5, 1, 9, 11, 10, 2]
heap_sort(arr)
print(arr)