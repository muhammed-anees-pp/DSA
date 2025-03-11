"""
Linear Searching
"""
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    
    return -1


# Example test case
num = [1,3,4,2,5]
target = 4
result = linear_search(num, target)
if result != -1:
    print(f"Element is found at index {result}")
else:
    print("Element is not found")