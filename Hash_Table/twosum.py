def two_sum(nums, target):
    # Create an empty dictionary to store the indices
    hash_table = {}
    
    # Iterate through the list
    for i, num in enumerate(nums):
        # Calculate the difference needed to reach the target
        difference = target - num
        
        # Check if the difference is already in the hash table
        if difference in hash_table:
            # If it is, return the indices of the two numbers
            return [hash_table[difference], i]
        
        # Otherwise, add the number to the hash table
        hash_table[num] = i
    
    # If no solution is found, return None
    return None

# Example usage:
nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)
print(result)  # Output: [0, 1]
