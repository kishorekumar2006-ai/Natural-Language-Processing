from collections import defaultdict

# ---------------- Corpus ----------------
corpus = [
    "I like NLP",
    "I like Python",
    "I study NLP",
    "We study Python",
    "You like NLP",
    "I study Python"
]

# ---------------- Count Unigrams and Bigrams ----------------
unigram_counts = defaultdict(int)
bigram_counts = defaultdict(int)

for sentence in corpus:
    words = sentence.split()

    # Count unigrams
    for word in words:
        unigram_counts[word] += 1

    # Count bigrams
    for i in range(len(words) - 1):
        bigram = (words[i], words[i + 1])
        bigram_counts[bigram] += 1

# Vocabulary
vocab = sorted(unigram_counts.keys())
V = len(vocab)

print("Vocabulary:", vocab)
print("Vocabulary Size =", V)

# ---------------- Bigram Counts ----------------
print("\nBigram Counts")
for bigram, count in bigram_counts.items():
    print(f"{bigram} : {count}")

# ---------------- MLE Probabilities ----------------
print("\nMLE Probabilities")
for bigram, count in bigram_counts.items():
    first = bigram[0]
    mle = count / unigram_counts[first]
    print(f"P({bigram[1]} | {bigram[0]}) = {count}/{unigram_counts[first]} = {mle:.4f}")

# ---------------- Laplace Smoothing ----------------
print("\nLaplace Smoothed Probabilities")
for first_word in vocab:
    for second_word in vocab:
        if first_word != second_word:    
            count = bigram_counts[(first_word, second_word)]
            laplace = (count + 1) / (unigram_counts[first_word] + V)
            print(f"P({second_word} | {first_word}) = ({count}+1)/({unigram_counts[first_word]}+{V}) = {laplace:.4f}")
        else:
            continue