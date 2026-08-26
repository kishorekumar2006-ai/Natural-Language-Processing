"""
Program 6: Implement a basic N-gram model (bigram) for text generation.
"""

import random
from collections import defaultdict


def build_bigram_model(text):
    words = text.lower().split()
    model = defaultdict(list)

    for i in range(len(words) - 1):
        model[words[i]].append(words[i + 1])

    return model


def generate_text(model, start_word, num_words=15):
    current_word = start_word.lower()
    result = [current_word]

    for _ in range(num_words - 1):
        next_words = model.get(current_word)
        if not next_words:
            break
        current_word = random.choice(next_words)
        result.append(current_word)

    return " ".join(result)


def main():
    corpus = (
        "the cat sat on the mat the cat ran after the mouse "
        "the mouse ran into the hole the dog chased the cat "
        "the cat and the dog are friends the dog sat on the mat"
    )

    random.seed(42)  # for reproducible output

    model = build_bigram_model(corpus)

    print("Bigram model (word -> possible next words):")
    for word, next_words in model.items():
        print(f"  {word:<10} -> {next_words}")

    print("\nGenerated text samples:")
    for start in ["the", "cat", "dog"]:
        print(f"  Starting with '{start}': {generate_text(model, start, num_words=10)}")


if __name__ == "__main__":
    main()
