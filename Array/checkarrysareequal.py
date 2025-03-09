"""
Check if Two Lists are Equal
"""
## Without inbuilt methods
def are_lists_equal_no_builtin(arr1, arr2):
    if len(arr1) != len(arr2):
        return False
    for i in range(len(arr1)):
        if arr1[i] != arr2[i]:
            return False
    return True

# Example Test Case
arr1 = [1, 2, 3]
arr2 = [1, 2, 3]

print(are_lists_equal_no_builtin(arr1, arr2))  # Output: True


##With inbuilt methods
def are_lists_equal(arr1, arr2):
    return arr1 == arr2

# Example Test Case
print(are_lists_equal(arr1, arr2))  # Output: True