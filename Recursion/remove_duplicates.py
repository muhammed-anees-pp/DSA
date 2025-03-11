"""
Remove duplicate elements from an array using recursion.
"""
def remove_duplicates(arr, index = 0, result=[]):
    if index == len(arr):
        return result
    
    if arr[index] not in result:
        result.append(arr[index])
    return remove_duplicates(arr, index+1, result)


# Example use case
num = [1,2,3,3,4,2,4,5,6]
print(remove_duplicates(num))