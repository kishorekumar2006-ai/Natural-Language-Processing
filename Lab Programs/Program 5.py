"""
Program 5: Use the Porter Stemmer algorithm to perform word stemming
on a list of words using the NLTK library.
"""

from nltk.stem import PorterStemmer


def main():
    stemmer = PorterStemmer()

    words = [
        "running", "runner", "ran", "easily", "fairly", "happiness",
        "connection", "connected", "connecting", "studies", "studying",
        "national", "nationality", "generalization", "flying", "cats"
    ]

    print(f"{'Original Word':<18}{'Stemmed Word'}")
    print("-" * 35)
    for word in words:
        print(f"{word:<18}{stemmer.stem(word)}")

    # Stem an entire sentence
    sentence = "The children were playing happily while studying their national history"
    stemmed_sentence = " ".join(stemmer.stem(w) for w in sentence.split())
    print("\nOriginal sentence:", sentence)
    print("Stemmed sentence :", stemmed_sentence)


if __name__ == "__main__":
    main()
