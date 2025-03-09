"""
Merge Two Lists
"""

## Without inbuilt method
def merge_arrays(arr1, arr2):
    merged_arr = []
    merged_arr.extend(arr1)
    merged_arr.extend(arr2)
    return merged_arr

# Example Test Case
num1 = [1, 2, 3, 4]
num2 = [5, 6, 7, 8]

result = merge_arrays(num1, num2)
print(f"Merged array (manual method): {result}")





## With inbuilt method
def merge_arrays_builtin(arr1, arr2):
    return arr1 + arr2

# Example Test Case
result = merge_arrays_builtin(num1, num2)
print(f"Merged array (built-in method): {result}")