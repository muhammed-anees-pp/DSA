"""
628 - Maximum Product of Three Numbers
"""

from typing import List

def maximum_product(nums: List[int]) -> int:
    max1 = max2 = max3 = float('-inf')
    min1 = min2 = float('inf')

    for num in nums:
        if num > max1:
            max3, max2, max1 = max2, max1, num
        elif num > max2:
            max3, max2 = max2, num
        elif num > max3:
            max3 = num

        if num < min1:
            min2, min1 = min1, num
        elif num < min2:
            min2 = num

    return max(max1 * max2 * max3, max1 * min1 * min2)

# Example usage:
numbers = [1, 10, 2, 6, 5, 3]
result = maximum_product(numbers)
print("Maximum product of three numbers:", result)