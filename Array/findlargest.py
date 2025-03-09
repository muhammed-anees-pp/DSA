"""
Find the largest element and return it.
"""

def findlarg(arr):
    if not arr:  # Handle empty list case
        return "Array is empty"

    larg = arr[0]  # Initialize with first element
    
    for i in range(1, len(arr)):  # Start loop from index 1
        if arr[i] > larg:
            larg = arr[i]
    
    return larg  # Return the largest number

num = [100, 50, 20, 150, 24, 110]
result = findlarg(num)
print(f"{result} is the largest element")
