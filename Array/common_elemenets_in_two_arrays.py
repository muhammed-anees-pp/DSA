"""
Find the Common Elements Between Two Lists
"""
def common_elements(arr1,arr2):
    return list(set(arr1) & set(arr2))

# Example Test Case
num1 = [1,2,3,4,5,2,3,1,2]
num2 = [1,2,3,4,3,2,1,6,7]

result = common_elements(num1,num2)
print(result)