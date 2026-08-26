"""
Program 7: Use the NLTK library to perform part-of-speech (POS)
tagging on a text.
"""

import nltk

for pkg in ["punkt", "punkt_tab", "averaged_perceptron_tagger",
            "averaged_perceptron_tagger_eng"]:
    try:
        nltk.download(pkg, quiet=True)
    except Exception:
        pass

from nltk import word_tokenize, pos_tag


def main():
    text = "Natural Language Processing enables computers to understand human language effectively."

    tokens = word_tokenize(text)
    tagged = pos_tag(tokens)

    print("Input text:", text, "\n")
    print(f"{'Word':<15}{'POS Tag'}")
    print("-" * 25)
    for word, tag in tagged:
        print(f"{word:<15}{tag}")

    # POS tag meaning reference for common tags
    tag_meaning = {
        "NN": "Noun singular", "NNS": "Noun plural", "NNP": "Proper noun",
        "VB": "Verb base form", "VBZ": "Verb 3rd person singular",
        "VBG": "Verb gerund", "JJ": "Adjective", "RB": "Adverb",
        "DT": "Determiner", "IN": "Preposition", "TO": "to", "CC": "Conjunction"
    }
    print("\nTag meanings used in this sentence:")
    seen = set()
    for _, tag in tagged:
        if tag in tag_meaning and tag not in seen:
            print(f"  {tag}: {tag_meaning[tag]}")
            seen.add(tag)


if __name__ == "__main__":
    main()
