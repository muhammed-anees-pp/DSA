"""
Given an array arr[], check whether it is sorted in non-decreasing order. Return true if it is sorted otherwise false.
"""

def is_sorted(arr):
    for i in range(1, len(arr)):
        if arr[i-1] > arr[i]:  # If previous element is greater than the next one, not sorted
            return False
    return True  # If loop completes, array is sorted

# Example Test Cases
arr1 = [10, 20, 30, 40, 50]
result = is_sorted(arr1)
print("The given array is sorted" if result else "The given array is not sorted")

arr2 = [90, 80, 100, 70, 40, 30]
result = is_sorted(arr2)
print("The given array is sorted" if result else "The given array is not sorted")
