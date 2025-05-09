"""
Two Sum
"""     
def twosum(nums,target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]

# Print results of checking both examples
nums = [2,7,11,15]
print(twosum(nums,9))