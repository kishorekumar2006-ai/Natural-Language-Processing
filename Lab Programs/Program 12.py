"""
Program 12: Implement an Earley parser for context-free grammars.
"""

import nltk
from nltk import CFG
from nltk.parse import EarleyChartParser


grammar = CFG.fromstring("""
    S -> NP VP
    NP -> Det N | Det N PP | 'I'
    VP -> V NP | V NP PP
    PP -> P NP
    Det -> 'the' | 'a' | 'an'
    N -> 'man' | 'telescope' | 'park' | 'dog'
    V -> 'saw' | 'walked'
    P -> 'with' | 'in'
""")


def main():
    parser = EarleyChartParser(grammar)

    sentence = "I saw a man with a telescope".split()
    print("Sentence:", " ".join(sentence))
    print("\nEarley parser results:")

    count = 0
    for tree in parser.parse(sentence):
        count += 1
        print(f"\nParse {count}:")
        print(tree)

    if count == 0:
        print("No valid parse found.")
    else:
        print(f"\nTotal number of parse trees found: {count}")


if __name__ == "__main__":
    main()
