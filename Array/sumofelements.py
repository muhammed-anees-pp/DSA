"""
Write a Python program to find the sum of all elements in a list.
"""

## Without inbuilt methods

def sum_of_elements(arr):
    total = 0
    for i in range(len(arr)):
        total += arr[i]
    return total

# Example Test Case
num = [1, 2, 3, 4]
result = sum_of_elements(num)
print(f"Sum of elements in the array: {result}")


## With inbuilt methods

def sum_of_elements(arr):
    total = sum(arr)
    return total

# Example Test Case
num = [1, 2, 3, 4]
result = sum_of_elements(num)
print(f"Sum of elements in the array: {result}")