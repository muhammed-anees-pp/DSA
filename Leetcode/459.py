"""
Repeated Substring Pattern
"""

def repeated_substring_pattern(s):
    n = len(s)
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            substring = s[:i]
            if substring * (n // i) == s:
                return True
    return False

# Example
test_strings = ["abab", "aba", "abcabcabc", "abcd"]

for s in test_strings:
    result = repeated_substring_pattern(s)
    print(f"String '{s}': repeated substring pattern? {result}")
