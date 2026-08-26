"""
Program 15: Implement probabilistic context-free grammar (PCFG) parsing
for a sentence.
"""

import nltk
from nltk import PCFG
from nltk.parse import ViterbiParser


grammar = PCFG.fromstring("""
    S -> NP VP [1.0]
    NP -> Det N [0.6] | Det N PP [0.4]
    VP -> V NP [0.7] | V NP PP [0.3]
    PP -> P NP [1.0]
    Det -> 'the' [0.6] | 'a' [0.4]
    N -> 'dog' [0.3] | 'cat' [0.3] | 'park' [0.2] | 'man' [0.2]
    V -> 'saw' [0.5] | 'chased' [0.5]
    P -> 'in' [0.5] | 'with' [0.5]
""")


def main():
    parser = ViterbiParser(grammar)

    sentence = "the dog saw a cat in the park".split()
    print("Sentence:", " ".join(sentence))
    print("\nMost probable parse tree (Viterbi PCFG parsing):\n")

    for tree in parser.parse(sentence):
        print(tree)
        print(f"\nProbability of this parse: {tree.prob():.8f}")
        tree.pretty_print()


if __name__ == "__main__":
    main()
