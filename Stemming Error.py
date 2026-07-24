from nltk.stem import PorterStemmer

# Create Porter Stemmer object
ps = PorterStemmer()

# Collection of words
words = [
    "university",
    "universe",
    "organization",
    "organ",
    "better",
    "good",
    "studies",
    "studying",
    "running",
    "runner"
]

print("Original Word\t\tStemmed Word")
print("-" * 40)

for word in words:
    stem = ps.stem(word)
    print(f"{word:15} {stem}")

print("\nOverstemming Examples")
print("----------------------")
print("university  ->", ps.stem("university"))
print("universe    ->", ps.stem("universe"))
print("Both words are reduced to similar stems.")

print("\nUnderstemming Examples")
print("-----------------------")
print("better      ->", ps.stem("better"))
print("good        ->", ps.stem("good"))
print("These words remain different although they have similar meanings.")