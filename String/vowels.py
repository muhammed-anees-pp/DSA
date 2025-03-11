"""
Write a function to count the number of vowels in a given string.
"""
## Without inbuilt method
def vowels_check(str):
    vowels = "aeiouAEIOU"
    count = 0
    for char in str:
        if char in vowels:
            count += 1
    return count


## With inbuilt method
def vowels(str):
    return sum(1 for char in str if char.lower() in "aeiou")


# Example test case
result = vowels_check("Malayalam")
print(result)

result2 = vowels("English")
print(result2)