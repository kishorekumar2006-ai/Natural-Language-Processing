import re
from pathlib import Path

import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()

file_path = Path(__file__).with_name("sample.txt")
with file_path.open("r", encoding="utf-8") as file:
    text = file.read()

try:
    words = word_tokenize(text)
except LookupError:
    nltk.download("punkt_tab", quiet=True)
    words = word_tokenize(text)

if not words:
    words = re.findall(r"\b\w+\b", text)

stemmed_words = [ps.stem(word) for word in words]

print("Original Words:\n")
print(words)

print("\nStemmed Words:\n")
print(stemmed_words)