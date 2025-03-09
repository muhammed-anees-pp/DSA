"""
Find the Frequency of an Element
"""

## Without inbuilt method
def count_frequency(arr, target):
    count = 0
    for value in arr:
        if value == target:
            count += 1
    return count

# Example Test Case
num = [10, 16, 17, 18, 19, 17, 16, 15, 17, 20]
target = 17
result = count_frequency(num, target)
print(f"Number of times {target} appears in the array: {result}")


## With inbuilt method
def count_frequency_inbuilt(arr, target):
    return arr.count(target)

result = count_frequency_inbuilt(num, target)
print(f"Number of times {target} appears in the array: {result}")
