"""
You are given an array of integers arr[]. Your task is to reverse the given array.
"""

## Without inbuilt method
def reverse_array(arr):
    left, right = 0, len(arr) - 1  # Initialize two pointers

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]  # Swap elements
        left += 1
        right -= 1  # Move pointers inward



# Example Usage:
arr1 = [1, 4, 3, 2, 6, 5]
reverse_array(arr1)
print(arr1)  # Output: [5, 6, 2, 3, 4, 1]

arr2 = [4, 5, 2]
reverse_array(arr2)
print(arr2)  # Output: [2, 5, 4]

arr3 = [1]
reverse_array(arr3)
print(arr3)  # Output: [1]


## With builtin method
def reverse_array_inbuilt(arr):
    arr = reversed(arr)
    return arr

# Example Usage:
arr1 = [1, 4, 3, 2, 6, 5]
reverse_array_inbuilt(arr1)
print(arr1)  # Output: [5, 6, 2, 3, 4, 1]

arr2 = [4, 5, 2]
reverse_array_inbuilt(arr2)
print(arr2)  # Output: [2, 5, 4]

arr3 = [1]
reverse_array_inbuilt(arr3)
print(arr3)  # Output: [1]

