"""
Find count of a specific substring in a string using recursion.
"""
def count_substring(str, sub, index = 0):
    if index > len(str) - len(sub):
        return 0
    
    count = 1 if str[index:index + len(sub)] == sub else 0
    return count + count_substring(str, sub, index + 1)
    

# Example test case
s = "ababcabc"
sub = "abc"
print(count_substring(s,sub))