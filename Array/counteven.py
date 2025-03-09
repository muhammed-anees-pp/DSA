"""
Write a Python program to count how many even numbers are in a list.
"""

def count_even(arr):
    count = 0
    for element in arr:
        if element % 2 == 0:
            count += 1
    return count

# Example Test Case
num = [1, 2, 4, 7, 8, 9]
result = count_even(num)
print(f"Number of even numbers in the given array: {result}")
