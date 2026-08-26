"""
Program 17: Access WordNet, a lexical database, to retrieve synsets
and explore word meanings.
"""

import nltk

for pkg in ["wordnet", "omw-1.4"]:
    try:
        nltk.download(pkg, quiet=True)
    except Exception:
        pass

from nltk.corpus import wordnet as wn


def explore_word(word):
    print(f"\n===== Exploring word: '{word}' =====")
    synsets = wn.synsets(word)

    if not synsets:
        print("No synsets found.")
        return

    for i, syn in enumerate(synsets[:3], start=1):  # limit to first 3 senses
        print(f"\nSense {i}: {syn.name()}")
        print(f"  Definition : {syn.definition()}")
        print(f"  Examples   : {syn.examples()}")
        print(f"  Lemmas     : {[lemma.name() for lemma in syn.lemmas()]}")

        # Synonyms
        synonyms = set()
        for lemma in syn.lemmas():
            synonyms.add(lemma.name())
        print(f"  Synonyms   : {synonyms}")

        # Antonyms
        antonyms = set()
        for lemma in syn.lemmas():
            for ant in lemma.antonyms():
                antonyms.add(ant.name())
        print(f"  Antonyms   : {antonyms if antonyms else 'None'}")

        # Hypernyms (more general terms) and Hyponyms (more specific terms)
        hypernyms = syn.hypernyms()
        hyponyms = syn.hyponyms()
        print(f"  Hypernyms  : {[h.name() for h in hypernyms]}")
        print(f"  Hyponyms   : {[h.name() for h in hyponyms[:5]]}")


def word_similarity(word1, word2):
    syn1 = wn.synsets(word1)
    syn2 = wn.synsets(word2)
    if syn1 and syn2:
        similarity = syn1[0].wup_similarity(syn2[0])
        print(f"\nWu-Palmer similarity between '{word1}' and '{word2}': {similarity}")


def main():
    explore_word("good")
    explore_word("run")
    word_similarity("dog", "cat")
    word_similarity("car", "boat")


if __name__ == "__main__":
    main()
