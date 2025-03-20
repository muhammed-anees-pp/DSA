"""
Bubble Sorting
"""
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j] # swapping
    return arr

# Example test case
num1 = [4, 1, 3, 9, 7]
num2 =  [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
num3 = [1, 2, 3, 4, 5]


print(bubble_sort(num1))
print(bubble_sort(num2))
print(bubble_sort(num3))