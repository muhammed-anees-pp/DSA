"""
Find the First Non-Repeating Element
"""
# Method 1
def first_non_repeating_no_builtin(arr):
    for i in range(len(arr)):
        is_unique = True
        for j in range(len(arr)):
            if arr[i] == arr[j] and i != j:
                is_unique = False
                break
        if is_unique:
            return arr[i]
    return -1

#Method 2
def first_non_repeating(arr):
    freq = {num: arr.count(num) for num in arr}
    for num in arr:
        if freq[num] == 1:
            return num
    return -1

# Example Usage:
arr = [1, 1, 2, 3, 4, 2, 5, 3]
print(first_non_repeating(arr)) 
print(first_non_repeating_no_builtin(arr))