from nltk.stem import PorterStemmer

ps = PorterStemmer()

words = ["caresses", "ponies", "running", "relational", "happiness"]

print("Word\t\tStem")

for word in words:
    print(f"{word}\t\t{ps.stem(word)}")