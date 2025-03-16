"""
Selection Sort
"""
def selection_sort(arr):
    for i in range(len(arr) - 1):
        # Assume the minimum value is at index i
        min_index = i
        
        # Find the index of the minimum element in the unsorted part
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # Swap the found minimum element with the first element of the unsorted part
        arr[i], arr[min_index] = arr[min_index], arr[i]
    
    return arr

# Example test case
num = [7, 5, 9, 2, 8]
num1 = [13,46,24,52,20,9]
num2 = [5,4,3,2,1]

print(selection_sort(num))
print(selection_sort(num1))
print(selection_sort(num2))
