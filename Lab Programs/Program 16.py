"""
Program 16: Use the SpaCy library to perform Named Entity Recognition
(NER) on a given text.

Note: Requires the spaCy English model. Install with:
    pip install spacy
    python -m spacy download en_core_web_sm
"""

import spacy


def main():
    try:
        nlp = spacy.load("en_core_web_sm")
    except OSError:
        print("Model 'en_core_web_sm' not found. Downloading it now...")
        from spacy.cli import download
        download("en_core_web_sm")
        nlp = spacy.load("en_core_web_sm")

    text = ("Apple Inc. was founded by Steve Jobs in Cupertino, California "
             "in 1976. It is now one of the largest companies in the world, "
             "competing with Microsoft and Google.")

    doc = nlp(text)

    print("Input text:\n", text, "\n")
    print(f"{'Entity':<20}{'Label':<12}{'Description'}")
    print("-" * 60)
    for ent in doc.ents:
        print(f"{ent.text:<20}{ent.label_:<12}{spacy.explain(ent.label_)}")


if __name__ == "__main__":
    main()
