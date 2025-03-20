"""
Insertion Sorting
"""
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]  # Shift elements
            j -= 1
        arr[j+1] = key  # Place key at the correct position
    return arr



# Example test case
num1 = [4, 1, 3, 9, 7]
num2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
num3 = [4, 1, 9]
print(insertion_sort(num1))
print(insertion_sort(num2))
print(insertion_sort(num3))
