"""
Program 19: Word Sense Disambiguation (WSD) using the Lesk algorithm.
"""

import nltk

for pkg in ["punkt", "punkt_tab", "wordnet", "omw-1.4"]:
    try:
        nltk.download(pkg, quiet=True)
    except Exception:
        pass

from nltk.wsd import lesk
from nltk import word_tokenize
from nltk.corpus import wordnet as wn


def disambiguate(sentence, ambiguous_word):
    tokens = word_tokenize(sentence)
    sense = lesk(tokens, ambiguous_word)

    print(f"\nSentence: '{sentence}'")
    print(f"Ambiguous word: '{ambiguous_word}'")

    if sense:
        print(f"Best matched sense: {sense.name()}")
        print(f"Definition: {sense.definition()}")
        print(f"Examples: {sense.examples()}")
    else:
        print("No sense could be determined.")

    # Show all possible senses for comparison
    print("\nAll possible senses for this word:")
    for syn in wn.synsets(ambiguous_word):
        print(f"  {syn.name():<20} - {syn.definition()}")


def main():
    disambiguate("I went to the bank to deposit some money.", "bank")
    disambiguate("We sat by the river bank and watched the sunset.", "bank")
    disambiguate("The bat flew out of the cave at night.", "bat")
    disambiguate("He hit the ball with a bat during the match.", "bat")


if __name__ == "__main__":
    main()
