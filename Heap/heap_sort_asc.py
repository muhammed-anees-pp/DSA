def heapify(arr,n,i):
    largest = i
    left = (2*i) + 1
    right = (2*i) + 2
    if left < n and arr[largest] < arr[left]:
        largest = left
    if right < n and arr[largest] < arr[right]:
        largest = right
    
    if largest != i:
        arr[largest],arr[i] = arr[i],arr[largest]
        heapify(arr,n,largest)


def heap_sort(arr):
    n = len(arr)
    ran = (len(arr) // 2) - 1
    for i in range(ran, -1,-1):
        heapify(arr,n,i)
    print(arr)
    for i in range(n-1, 0, -1):
        arr[i],arr[0] = arr[0],arr[i]
        heapify(arr,i,0)
    print(arr)
        
        
arr = [70, 50, 60, 30, 40, 20]
heap_sort(arr)


"""
arr = [70, 50, 60, 30, 40, 20]

Step 1: Build a Max Heap
    ran = (len(arr) // 2) - 1 = (6 // 2) - 1 = 2

    🔁 Iteration 1: heapify(arr, 6, 2)
        Subtree rooted at index 2 → value 60
        Left = 5 (arr[5] = 20), Right = 6 (out of bounds)
        Both children are smaller, so nothing changes.
        ✅ Result: [70, 50, 60, 30, 40, 20]

    🔁 Iteration 2: heapify(arr, 6, 1)
        Subtree rooted at index 1 → value 50
        Left = 3 (arr[3] = 30), Right = 4 (arr[4] = 40)
        Both children are smaller, so nothing changes.
        ✅ Result: [70, 50, 60, 30, 40, 20]

    🔁 Iteration 3: heapify(arr, 6, 0)
        Subtree rooted at index 0 → value 70
        Left = 1 (50), Right = 2 (60)
        Both children are smaller, so nothing changes.
        ✅ Max Heap Built: [70, 50, 60, 30, 40, 20]
        👆 This is printed by print(arr) in the heap_sort() function.

    ✅ Max Heap Complete!

Step 2: Sorting Begins
    🔁 Iteration 1:
    Swap arr[0] (70) with arr[5] (20)
    New array: [20, 50, 60, 30, 40, 70]
    Call heapify(arr, 5, 0)
        Root = 20
        Left = 1 (50), Right = 2 (60)
        Largest = 60 → swap with 20
    Now: [60, 50, 20, 30, 40, 70]
    Heapify index 2:
        Left = 5 (out of bounds), Right = 6 (out of bounds)
    ✅ Result: [60, 50, 20, 30, 40, 70]

    🔁 Iteration 2:
    Swap arr[0] (60) with arr[4] (40)
    New array: [40, 50, 20, 30, 60, 70]
    Call heapify(arr, 4, 0)
        Root = 40
        Left = 1 (50), Right = 2 (20)
        Largest = 50 → swap with 40
    Now: [50, 40, 20, 30, 60, 70]
    Heapify index 1:
        Left = 3 (30), Right = 4 (out of bounds)
        40 is bigger than 30 → no swap
    ✅ Result: [50, 40, 20, 30, 60, 70]

    🔁 Iteration 3:
    Swap arr[0] (50) with arr[3] (30)
    New array: [30, 40, 20, 50, 60, 70]
    Call heapify(arr, 3, 0)
        Root = 30
        Left = 1 (40), Right = 2 (20)
        Largest = 40 → swap with 30
    Now: [40, 30, 20, 50, 60, 70]
    Heapify index 1:
        No valid children (heap size is 3)
    ✅ Result: [40, 30, 20, 50, 60, 70]

    🔁 Iteration 4:
    Swap arr[0] (40) with arr[2] (20)
    New array: [20, 30, 40, 50, 60, 70]
    Call heapify(arr, 2, 0)
        Root = 20
        Left = 1 (30), Right = 2 (invalid)
        30 > 20 → swap
    Now: [30, 20, 40, 50, 60, 70]
    Heapify index 1 → no valid children
    ✅ Result: [30, 20, 40, 50, 60, 70]

    🔁 Iteration 5:
    Swap arr[0] (30) with arr[1] (20)
    New array: [20, 30, 40, 50, 60, 70]
    Heapify(1, 0) — no valid children
    ✅ Result: [20, 30, 40, 50, 60, 70]


    Final Sorted Array:
    [20, 30, 40, 50, 60, 70]


"""