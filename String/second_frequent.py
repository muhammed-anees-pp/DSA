def find_most_frequent_chars(s):
    freq = {}
    
    # Count the frequency of each character
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    
    # Initialize variables for the most and second most frequent characters
    max_char = second_max_char = ''
    max_freq = second_max_freq = 0
    
    for char in freq:
        if freq[char] > max_freq:
            # Update second max before changing max
            second_max_freq = max_freq
            second_max_char = max_char
            
            max_freq = freq[char]
            max_char = char
        elif freq[char] > second_max_freq and freq[char] != max_freq:
            second_max_freq = freq[char]
            second_max_char = char
    
    return max_char, max_freq, second_max_char, second_max_freq

s = "abracadabra"
most_char, most_freq, second_char, second_freq = find_most_frequent_chars(s)
print(f"The most frequent character is '{most_char}' with frequency {most_freq}")
print(f"The second most frequent character is '{second_char}' with frequency {second_freq}")
