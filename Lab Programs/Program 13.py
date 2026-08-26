"""
Program 13: Generate a parse tree for a given sentence using a
context-free grammar.
"""

import nltk
from nltk import CFG
from nltk.parse import RecursiveDescentParser


grammar = CFG.fromstring("""
    S -> NP VP
    NP -> Det N
    VP -> V NP
    Det -> 'the' | 'a'
    N -> 'boy' | 'ball' | 'girl'
    V -> 'kicked' | 'threw'
""")


def main():
    sentence = "the boy kicked a ball".split()
    parser = RecursiveDescentParser(grammar)

    print("Sentence:", " ".join(sentence))

    for tree in parser.parse(sentence):
        print("\nParse Tree (bracketed notation):")
        print(tree)

        print("\nParse Tree (pretty print):")
        tree.pretty_print()

        # Save tree diagram as a PostScript/image file (optional, needs Ghostscript/Tk)
        try:
            tree.draw()
        except Exception as e:
            print(f"(Skipping graphical draw - no display available: {e})")


if __name__ == "__main__":
    main()
