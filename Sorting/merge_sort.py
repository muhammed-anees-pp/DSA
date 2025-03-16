"""
Merge sort
"""

# Sorting
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    low = merge_sort(arr[:mid])
    high = merge_sort(arr[mid:])

    return merge(low,high)


# Merging
def merge(low, high):
    sorted_arr = []
    i = j = 0
    while i < len(low) and j < len(high):
        if low[i] < high[j]:
            sorted_arr.append(low[i])
            i += 1
        else:
            sorted_arr.append(high[j])
            j += 1
    
    sorted_arr.extend(low[i:])
    sorted_arr.extend(high[j:])

    return sorted_arr

# Example test case
num1 = [4, 1, 3, 9, 7]
num2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
num3 = [1, 3 , 2]

print(merge_sort(num1))
print(merge_sort(num2))
print(merge_sort(num3))