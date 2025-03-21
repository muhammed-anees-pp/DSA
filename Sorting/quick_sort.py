"""
Quick Sort
"""
def quick_sort(arr):
    # Base case: If the array has 1 or no element, it's already sorted
    if len(arr) <= 1:
        return arr
    
    # Choose the pivot as the middle element of the array
    pivot = arr[len(arr) // 2]
    
    # Partitioning:
    # - left → elements smaller than the pivot
    left = [x for x in arr if x < pivot]
    # - middle → elements equal to the pivot
    middle = [x for x in arr if x == pivot]
    # - right → elements greater than the pivot
    right = [x for x in arr if x > pivot]
    
    # Recursively sort left and right parts and combine them with the middle
    return quick_sort(left) + middle + quick_sort(right)


# Example test case
num = [5, 1, 4, 2, 8]
num1= [4, 1, 3, 9, 7]
num2= [2, 1, 6, 10, 4, 1, 3, 9, 7]

print(quick_sort(num))
print(quick_sort(num1))
print(quick_sort(num2))