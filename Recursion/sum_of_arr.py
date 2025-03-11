"""
Find the sum of elements in an array using recursion
"""
def sum_of_array(arr, index = 0):
    if index == len(arr):
        return 0
    
    return arr[index] + sum_of_array(arr,index + 1)
    
# Example test case
num = [1,2,3,4,5]
print(sum_of_array(num))