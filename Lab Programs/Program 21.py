"""
Program 21: Perform syntax-driven semantic analysis by extracting
noun phrases and their meanings from a sentence.
"""

import nltk

for pkg in ["punkt", "punkt_tab", "averaged_perceptron_tagger",
            "averaged_perceptron_tagger_eng", "wordnet"]:
    try:
        nltk.download(pkg, quiet=True)
    except Exception:
        pass

from nltk import word_tokenize, pos_tag, RegexpParser
from nltk.corpus import wordnet as wn


def extract_noun_phrases(sentence):
    tokens = word_tokenize(sentence)
    tagged = pos_tag(tokens)

    # Chunk grammar for noun phrases: optional determiner + adjectives + nouns
    grammar = "NP: {<DT>?<JJ>*<NN.*>+}"
    chunk_parser = RegexpParser(grammar)
    tree = chunk_parser.parse(tagged)

    noun_phrases = []
    for subtree in tree.subtrees(filter=lambda t: t.label() == "NP"):
        phrase = " ".join(word for word, tag in subtree.leaves())
        noun_phrases.append(phrase)

    return tree, noun_phrases


def get_meaning(phrase):
    """Fetch WordNet meaning for the head noun of the phrase (last word)."""
    head_word = phrase.split()[-1]
    synsets = wn.synsets(head_word, pos=wn.NOUN)
    if synsets:
        return synsets[0].definition()
    return "No definition found."


def main():
    sentence = "The intelligent student solved the difficult math problem quickly"

    tree, noun_phrases = extract_noun_phrases(sentence)

    print("Sentence:", sentence)
    print("\nChunked Tree:")
    print(tree)

    print("\nExtracted Noun Phrases and their meanings:")
    for phrase in noun_phrases:
        meaning = get_meaning(phrase)
        print(f"  Phrase: '{phrase}'")
        print(f"    Meaning (head word): {meaning}")


if __name__ == "__main__":
    main()
