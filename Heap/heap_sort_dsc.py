def heapify(arr, n, i):
    smallest = i
    left_idx = i * 2 + 1
    right_idx = i * 2 + 2
    if left_idx < n and arr[left_idx] < arr[smallest]:
        smallest = left_idx
    if right_idx < n and arr[right_idx] < arr[smallest]:
        smallest = right_idx
    if smallest != i:
        arr[smallest], arr[i] = arr[i], arr[smallest]
        heapify(arr, n, smallest)


def heap_sort(arr):
    n = len(arr)
    ran = n // 2 - 1
    for i in range(ran, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1,0,-1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
arr = [1,5,0,9,10,3]
heap_sort(arr)
print(arr)