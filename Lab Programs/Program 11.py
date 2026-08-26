"""
Program 11: Implement a simple top-down parser for context-free grammars.

Grammar (example):
    S  -> NP VP
    NP -> Det N | Det N PP
    VP -> V NP | V NP PP
    PP -> P NP
    Det -> 'the' | 'a'
    N  -> 'dog' | 'cat' | 'park'
    V  -> 'saw' | 'chased'
    P  -> 'in' | 'with'
"""

import nltk
from nltk import CFG
from nltk.parse import RecursiveDescentParser


grammar = CFG.fromstring("""
    S -> NP VP
    NP -> Det N | Det N PP
    VP -> V NP | V NP PP
    PP -> P NP
    Det -> 'the' | 'a'
    N -> 'dog' | 'cat' | 'park'
    V -> 'saw' | 'chased'
    P -> 'in' | 'with'
""")


def main():
    parser = RecursiveDescentParser(grammar)

    sentence = "the dog saw a cat in the park".split()
    print("Sentence:", " ".join(sentence))
    print("\nTop-down parse trees:")

    found = False
    for tree in parser.parse(sentence):
        found = True
        print(tree)
        tree.pretty_print()

    if not found:
        print("No valid parse found for the given grammar.")


if __name__ == "__main__":
    main()
