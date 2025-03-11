"""
Find the frequency of characters in a string using recursion
"""
def freq_str(str, index=0, freq = {}):
    if index == len(str):
        return freq
    
    char = str[index]
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1
    
    return freq_str(str, index + 1, freq)

# Example test case
s = "programming"
print(freq_str(s))