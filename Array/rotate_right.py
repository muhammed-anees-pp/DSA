"""
Rotate a List to the Right by k Positions
"""
## Without inbuilt method
def right_rotate(arr,rotate):
    for i in range(rotate):
        last = arr[-1]
        for j in range(len(arr) - 1, 0, -1):
            arr[j] = arr[j-1]
        
        arr[0] = last
    return arr


## With inbuilt method (slicing)
def right_rotate_slicing(arr,rotate):
    return arr[-rotate:] + arr[:-rotate]



# Example Test Case
num = [1, 2, 3, 4, 5]
result = right_rotate(num, 2)
print(result)

num2 = [1, 2, 3, 4, 5, 6]
result_slice = right_rotate_slicing(num2,2)
print(result_slice)