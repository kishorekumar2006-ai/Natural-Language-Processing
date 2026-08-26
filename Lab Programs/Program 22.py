"""
Program 22: Perform reference resolution (anaphora/coreference resolution)
within a text using a simple heuristic-based approach.
"""

import nltk

for pkg in ["punkt", "punkt_tab", "averaged_perceptron_tagger",
            "averaged_perceptron_tagger_eng"]:
    try:
        nltk.download(pkg, quiet=True)
    except Exception:
        pass

from nltk import word_tokenize, pos_tag, sent_tokenize


PRONOUNS = {"he", "she", "it", "they", "him", "her", "them", "his", "hers", "its", "their"}

MALE_PRONOUNS = {"he", "him", "his"}
FEMALE_PRONOUNS = {"she", "her", "hers"}
NEUTRAL_PRONOUNS = {"it", "its"}
PLURAL_PRONOUNS = {"they", "them", "their"}


def get_candidate_entities(sentence):
    """Extract proper nouns (NNP) as candidate entities."""
    tokens = word_tokenize(sentence)
    tagged = pos_tag(tokens)
    entities = [word for word, tag in tagged if tag in ("NNP", "NNPS")]
    return entities


def resolve_references(text):
    sentences = sent_tokenize(text)
    entity_history = []  # tracks entities in order of mention
    resolutions = []

    for sentence in sentences:
        entities = get_candidate_entities(sentence)
        entity_history.extend(entities)

        tokens = word_tokenize(sentence)
        for word in tokens:
            word_lower = word.lower()
            if word_lower in PRONOUNS and entity_history:
                # Simple heuristic: link to most recently mentioned entity
                # (in a real system this would consider gender/number agreement)
                antecedent = entity_history[-1]
                resolutions.append((word, sentence, antecedent))

    return resolutions


def main():
    text = ("John went to the market. He bought some apples and vegetables. "
             "Mary saw John there. She greeted him warmly. "
             "The dog followed John home. It was very happy.")

    print("Input text:\n", text)

    resolutions = resolve_references(text)

    print("\nReference Resolution Results:")
    for pronoun, sentence, antecedent in resolutions:
        print(f"  In sentence: \"{sentence}\"")
        print(f"    Pronoun '{pronoun}' -> refers to -> '{antecedent}'\n")


if __name__ == "__main__":
    main()
