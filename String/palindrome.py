"""
Write a function to check if a string reads the same forward and backward.
"""

## Without inbuilt method
def palindrome(str):
    n = len(str)
    for i in range(n //2 ):
        if str[i] != str[n-i-1]:
            return False
    return True

## With inbuilt method
def palindrome_inbuilt(str):
    return str== str[::-1]


# Example Usage
check1 = palindrome("malayalam")
check2 = palindrome("english")
print("Palindrome" if check1 else "Not Palindrome")
print("Palindrome" if check2 else "Not Palindrome")

check3 = palindrome_inbuilt("malayalam")
check4 = palindrome_inbuilt("english")
print("Palindrome" if check3 else "Not Palindrome")
print("Palindrome" if check4 else "Not Palindrome")