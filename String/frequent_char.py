def most_frequent_char(s):
    freq = {}
    
    # Count the frequency of each character
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    
    # Find the character with the maximum frequency
    max_freq = 0
    max_char = ''
    for char in freq:
        if freq[char] > max_freq:
            max_freq = freq[char]
            max_char = char
    
    return max_char

s = "abracadabra"
result = most_frequent_char(s)
print(f"The most frequent character is: '{result}'")


def most_frequent_char(s):
    return max(set(s), key=s.count)

s = "abracadabra"
result = most_frequent_char(s)
print(f"The most frequent character is: '{result}'")
