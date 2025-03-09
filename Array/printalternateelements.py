"""
Print alternate elements in an array
"""

def alternate_elements(arr):
    return arr[::2] #Slicing


arr1 = [1,2,3,4,5]
arr2 = [2,1,4,5,6]

print("Array1: ",alternate_elements(arr1))
print("Array2: ",alternate_elements(arr2))