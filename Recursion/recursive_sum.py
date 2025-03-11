"""
Write a recursive function in Python that calculates the sum of the digits of a given integer n.
"""

def recursive_sum(num):
    if num == 0:
        return 0
    return (num % 10) + recursive_sum(num // 10)

# Example Usage:
print("Sum:", recursive_sum(1234))
print("Sum:", recursive_sum(12345))