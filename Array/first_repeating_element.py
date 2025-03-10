"""
Find the First Repeating Element
"""
## Without inbuilt method
# Method 1
def repeating_element(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]:
                return arr[i]
        
    return -1


# Method 2
def repeating_element_set(arr):
    seen = set()
    for num in arr:
        if num in seen:
            return num
        seen.add(num)
    
    return -1


# Example Usage:
arr = [1, 2, 3, 4, 4, 5]
result = repeating_element(arr)
print(result)


result2 = repeating_element_set(arr)
print(result2)
