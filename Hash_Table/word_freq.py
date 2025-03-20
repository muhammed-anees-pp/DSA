def word_frequency(text):
    freq_table = {}
    words = text.split()

    for word in words:
        word = word.lower().strip(".,!?")  # Clean punctuation
        freq_table[word] = freq_table.get(word, 0) + 1  # Increment count

    return freq_table

text = "Python is a beginner friendly programming language."
print(word_frequency(text))
