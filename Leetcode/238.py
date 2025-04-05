"""
Product of Array Except Self
"""

def product_except_self(nums):
    n = len(nums)
    answer = [1] * n

    prefix = 1
    for i in range(n):
        answer[i] = prefix
        prefix *= nums[i]

    suffix = 1
    for i in range(n - 1, -1, -1):
        answer[i] *= suffix
        suffix *= nums[i]

    return answer

# Example
nums = [1, 2, 3, 4]
result = product_except_self(nums)
print(result)
