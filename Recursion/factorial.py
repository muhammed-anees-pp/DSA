"""
Print the result of factorial
"""
def factorial(num):
    if num == 0:
        return 1
    
    return num*factorial(num-1)

# Example Usage:
print(factorial(6))