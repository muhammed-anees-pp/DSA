"""
Find the element from an array and return it's position
"""

def target(arr, num):
    for i in range(len(arr)):
        if arr[i] == num:
            return i  # Return index if found
    
    return -1

arr1 = [1, 2, 3, 4, 5]
num1 = 5
result = target(arr1,num1)

print(f"{num1} is available at {result}" if result != -1 else "Element not found")
