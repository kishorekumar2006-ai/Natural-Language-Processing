import nltk
nltk.download('punkt')

from nltk.tokenize import sent_tokenize

text = "Hello World! Welcome to NLP. Python is easy to learn."

sentences = sent_tokenize(text)

print("Sentences:")
for sentence in sentences:
    print(sentence)