def heapify(arr,n,i):
    smallest = i
    left = (2*i) + 1
    right = (2*i) + 2
    if left < n and arr[smallest] > arr[left]:
        smallest = left
    if right < n and arr[smallest] > arr[right]:
        smallest = right
    
    if smallest != i:
        arr[smallest],arr[i] = arr[i],arr[smallest]
        heapify(arr,n,smallest)


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
ran = (len(arr) // 2) - 1 = (6 // 2) - 1 = 2

Step 1: Build a Min Heap
    🔁 Iteration 1: heapify(arr, 6, 2)
    Subtree rooted at index 2 → value 60
    Left = 5 (arr[5] = 20), Right = 6 (out of bounds)
    Compare: 60 > 20 → swap them
    ✔ Swap 60 and 20 → [70, 50, 20, 30, 40, 60]
    Now, call heapify(arr, 6, 5)
        No children → done
        ✅ Result: [70, 50, 20, 30, 40, 60]

    🔁 Iteration 2: heapify(arr, 6, 1)
    Subtree rooted at index 1 → value 50
    Left = 3 (30), Right = 4 (40)
    50 > 30 → smallest = 3
    ✔ Swap 50 and 30 → [70, 30, 20, 50, 40, 60]
    Call heapify(arr, 6, 3)
        No children → done
        ✅ Result: [70, 30, 20, 50, 40, 60]

    🔁 Iteration 3: heapify(arr, 6, 0)
    Subtree rooted at index 0 → value 70
    Left = 1 (30), Right = 2 (20)
    70 > 30 → smallest = 1
    30 > 20 → smallest = 2
    ✔ Swap 70 and 20 → [20, 30, 70, 50, 40, 60]
    Call heapify(arr, 6, 2)
    Left = 5 (60), Right = 6 (out of bounds)
    70 > 60 → swap
    ✔ Swap 70 and 60 → [20, 30, 60, 50, 40, 70]
    Call heapify(arr, 6, 5) → no children
    ✅ Min Heap Built: [20, 30, 60, 50, 40, 70]
    👆 This is printed in the first print(arr)

Step 2: Sorting Begins
Now we extract the minimum (root of Min Heap) and place it at the end.
    🔁 Iteration 1:
    Swap arr[0] (20) and arr[5] (70) → [70, 30, 60, 50, 40, 20]
    Call heapify(arr, 5, 0)
        Root = 70, Left = 30, Right = 60
        70 > 30 → smallest = 1
            ✔ Swap → [30, 70, 60, 50, 40, 20]
            Call heapify(5, 1)
        Root = 70, Left = 3 (50), Right = 4 (40)
        70 > 50 → smallest = 3
        50 > 40 → smallest = 4
            ✔ Swap → [30, 40, 60, 50, 70, 20]
            ✅ Result: [30, 40, 60, 50, 70, 20]

    🔁 Iteration 2:
    Swap arr[0] (30) and arr[4] (70) → [70, 40, 60, 50, 30, 20]
    Call heapify(arr, 4, 0)
    70 > 40 → smallest = 1
        ✔ Swap → [40, 70, 60, 50, 30, 20]
        Call heapify(4, 1)
    70 > 50 → swap → [40, 50, 60, 70, 30, 20]
        ✅ Result: [40, 50, 60, 70, 30, 20]

    🔁 Iteration 3:
    Swap arr[0] (40) and arr[3] (70) → [70, 50, 60, 40, 30, 20]
    Call heapify(arr, 3, 0)
        70 > 50 → smallest = 1
            ✔ Swap → [50, 70, 60, 40, 30, 20]
            ✅ Result: [50, 70, 60, 40, 30, 20]

    🔁 Iteration 4:
    Swap arr[0] (50) and arr[2] (60) → [60, 70, 50, 40, 30, 20]
    Call heapify(arr, 2, 0)
        60 < both children → nothing to do
            ✅ Result: [60, 70, 50, 40, 30, 20]

    🔁 Iteration 5:
    Swap arr[0] (60) and arr[1] (70) → [70, 60, 50, 40, 30, 20]
    Call heapify(arr, 1, 0)
        Nothing to do
        ✅ Result: [70, 60, 50, 40, 30, 20]
    👆 This array is printed after the second print(arr)

    Final Result:
    [70, 60, 50, 40, 30, 20]



"""