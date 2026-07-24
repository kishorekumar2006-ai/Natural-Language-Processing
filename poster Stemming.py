from nltk.stem import PorterStemmer

ps = PorterStemmer()

words = ["playing", "running", "studies", "happiness", "connection"]

print("Original Word -> Stemmed Word")

for word in words:
    stem = ps.stem(word)
    print(word, "->", stem)