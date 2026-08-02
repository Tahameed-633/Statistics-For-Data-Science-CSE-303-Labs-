sentence="The quick brown fox jumps over the lazy dog"
words=sentence.split()
print(words)
word_length=[len(word) for word in words if word.lower()!="the"]
print(word_length)