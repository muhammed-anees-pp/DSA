"""
Remove Duplicates from a List
"""
## Wihout inbuilt methods
def remove_duplicates_no_builtin(arr):
    unique = []
    for num in arr:
        if num not in unique:
            unique.append(num)
    return unique

# Example Usage:
arr = [1, 2, 2, 3, 4, 4, 5]

print(remove_duplicates_no_builtin(arr))  # Output: [1, 2, 3, 4, 5]



## With inbuilt method
def remove_duplicates(arr):
    return list(set(arr))

print(remove_duplicates(arr))  # Output: [1, 2, 3, 4, 5]