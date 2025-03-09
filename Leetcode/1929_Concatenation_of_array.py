"""
Q:1929 - Concatenation of Array
"""
## Method 1
def concatenation(arr):
    return arr + arr

## Method 2
# def concatenation(arr):
#     ans = []
#     ans.extend(arr)
#     ans.extend(arr)
#     return ans

## Method 3
# def concatenation(arr):
#     ans = []
#     for value in arr:
#         ans.append(value)
#     for value in arr:
#         ans.append(value)
#     return ans

# Example Test Case
num = [1,2,3,4]

print("Final array: ", concatenation(num))