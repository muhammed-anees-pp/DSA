"""
Write a function to check if two strings are anagrams of each other.
"""
## Without inbuilt
def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    count1, count2 = {}, {}
    for char in s1:
        count1[char] = count1.get(char, 0) + 1
    for char in s2:
        count2[char] = count2.get(char, 0) + 1
    return count1 == count2




## Without inbuilt methods
def is_anagrams(s1, s2):
    return sorted(s1) == sorted(s2)

# Example test case
print(is_anagram("listen", "silent"))  
print(is_anagrams("hello", "world"))    