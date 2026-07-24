from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
from nltk.stem import SnowballStemmer

porter = PorterStemmer()
lancaster = LancasterStemmer()
snowball = SnowballStemmer("english")

words = ["running", "studies", "connection", "happiness", "playing"]

print("Word\t\tPorter\t\tLancaster\tSnowball")

for word in words:
    p = porter.stem(word)
    l = lancaster.stem(word)
    s = snowball.stem(word)

    print(f"{word}\t\t{p}\t\t{l}\t\t{s}")