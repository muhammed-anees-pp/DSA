"""
Q:2413 - Smallest Even Multiple
"""
def smallestevenmultiple(n):
    if n % 2 == 0:
        return n
    else:
        return 2*n
    
# Example Test Case 
print(smallestevenmultiple(5))
print(smallestevenmultiple(6))