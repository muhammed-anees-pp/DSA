"""
Write a function to reverse the words in a given sentence.
"""
## Without inbuilt
def reverse_word(str):
    words = []
    word = ""
    for char in str:
        if char == " ":
            words.append(word)
            word = ""
        else:
            word += char
    words.append(word)
    return " ".join(words[::-1])
    
# Using inbuilt methods
def reverse_words_inbuilt(s):
    return " ".join(s.split()[::-1])
    

# Example test case
print(reverse_word("Hello World"))
print(reverse_words_inbuilt("Python DSA")) 