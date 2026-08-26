"""
Program 3: Perform morphological analysis using the NLTK library.

Morphological analysis breaks words down into their root/stem and
identifies affixes (prefixes/suffixes), and also uses POS tagging
to understand word forms.
"""

import nltk

# Download required resources (only downloads if not already present)
for pkg in ["punkt", "punkt_tab", "averaged_perceptron_tagger",
            "averaged_perceptron_tagger_eng", "wordnet", "omw-1.4"]:
    try:
        nltk.download(pkg, quiet=True)
    except Exception:
        pass

from nltk.stem import WordNetLemmatizer
from nltk import word_tokenize, pos_tag


def morphological_analysis(text):
    lemmatizer = WordNetLemmatizer()
    tokens = word_tokenize(text)
    tagged = pos_tag(tokens)

    # Map POS tag to WordNet POS for accurate lemmatization
    def get_wordnet_pos(tag):
        if tag.startswith("J"):
            return "a"
        elif tag.startswith("V"):
            return "v"
        elif tag.startswith("N"):
            return "n"
        elif tag.startswith("R"):
            return "r"
        return "n"

    print(f"{'Word':<15}{'POS Tag':<10}{'Lemma (Root)':<15}")
    print("-" * 40)
    for word, tag in tagged:
        wn_pos = get_wordnet_pos(tag)
        lemma = lemmatizer.lemmatize(word, pos=wn_pos)
        print(f"{word:<15}{tag:<10}{lemma:<15}")


def main():
    sample_text = "The children were running happily and playing games in the fields."
    print(f"Input text: {sample_text}\n")
    morphological_analysis(sample_text)


if __name__ == "__main__":
    main()
