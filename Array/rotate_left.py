"""
Rotate a List to the Left by k Positions
"""
## Without inbuilt method
def left_rotate(arr, rotate):
    for i in range(rotate):
        first = arr[0]  # Store first element
        for j in range(len(arr) - 1):  
            arr[j] = arr[j + 1]  # Shift elements left
        
        arr[-1] = first  # Move first element to last position
    return arr

## With inbuilt method (slicing)
def left_rotate_slicing(arr, rotate):
    return arr[rotate:] + arr[:rotate]

# Example Test Case
num = [1, 2, 3, 4, 5]
result = left_rotate(num, 2)
print(result)

num2 = [1, 2, 3, 4, 5, 6]
result_slice = left_rotate_slicing(num2, 2)
print(result_slice)
