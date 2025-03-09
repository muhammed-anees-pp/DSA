"""
Q:3099 - Harshad number
"""
def harshad_number(num):
    sum = 0
    temp = num
    while temp > 0:
        sum += temp % 10
        temp //= 10
    
    return sum if num % sum == 0 else -1


# Example Test Case
num1 = 18
print("Num1: ", harshad_number(num1))

num2 = 23
print("Num2: ", harshad_number(num2))