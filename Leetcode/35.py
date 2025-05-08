"""
Search Insert Position
"""
def search_insert(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left


# Example test cases
nums_list = [1, 3, 5, 6]
targets = [5, 2, 7, 0]

for target in targets:
    index = search_insert(nums_list, target)
    print(f"Target {target} → Insert position: {index}")
