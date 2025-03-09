"""
Find the Minimum Element in a List
"""

## Without inbuilt methods
def find_min_no_builtin(arr):
    min_num = arr[0]
    for num in arr:
        if num < min_num:
            min_num = num
    return min_num

# Example Usage:
arr = [10, 20, 4, 45, 99]
print(find_min_no_builtin(arr))



## With inbuilt methods
def find_min(arr):
    return min(arr)

# Example Usage:
print(find_min(arr))