"""
Palindrome Number
"""
def isPalindrome(x):
    if x < 0 or (x % 10 == 0 and x !=0):
        return False
        
    reversed = 0
    while x > reversed:
        reversed = reversed * 10 + x % 10
        x //= 10
        
    return x == reversed or x == reversed // 10


# Print results of checking examples
print(isPalindrome(121))
print(isPalindrome(-121))
print(isPalindrome(10))