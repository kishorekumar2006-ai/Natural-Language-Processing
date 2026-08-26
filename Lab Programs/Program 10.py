"""
Program 10: Implement transformation-based tagging (Brill-style tagging)
using a set of transformation rules applied on top of an initial
naive tagging.
"""


# Step 1: Initial naive tagger - assign the most frequent tag to each
# word using a simple lexicon, default to NOUN if unknown.
lexicon = {
    "the": "DET",
    "a": "DET",
    "dog": "NOUN",
    "cat": "NOUN",
    "runs": "NOUN",   # deliberately "wrong" initial tag to be fixed by TBL
    "run": "VERB",
    "barks": "NOUN",  # deliberately "wrong" initial tag
    "quickly": "NOUN",  # deliberately "wrong" initial tag
    "very": "ADV",
}


def initial_tag(words):
    return [(w, lexicon.get(w, "NOUN")) for w in words]


# Step 2: Transformation rules
# Each rule: (condition_function, from_tag, to_tag, description)
def rule_verb_after_noun_ending_s(tagged, i):
    """If a word ends with 's' and follows a DET+NOUN subject pattern
    at sentence position > 0 and is tagged NOUN, but the previous word
    is a NOUN (i.e., acting as a verb like 'runs', 'barks') -> change to VERB."""
    word, tag = tagged[i]
    if tag == "NOUN" and word.endswith("s") and i > 0:
        prev_word, prev_tag = tagged[i - 1]
        if prev_tag == "NOUN":
            return "VERB"
    return tag


def rule_adverb_ending_ly(tagged, i):
    """If word ends in 'ly' and tagged NOUN -> change to ADV."""
    word, tag = tagged[i]
    if tag == "NOUN" and word.endswith("ly"):
        return "ADV"
    return tag


transformation_rules = [
    ("Change NOUN->VERB if word ends in 's' and follows a NOUN", rule_verb_after_noun_ending_s),
    ("Change NOUN->ADV if word ends in 'ly'", rule_adverb_ending_ly),
]


def apply_transformations(tagged):
    tagged = list(tagged)
    for description, rule in transformation_rules:
        new_tagged = []
        changed = False
        for i, (word, tag) in enumerate(tagged):
            new_tag = rule(tagged, i)
            if new_tag != tag:
                changed = True
            new_tagged.append((word, new_tag))
        tagged = new_tagged
        if changed:
            print(f"Applied rule: {description}")
    return tagged


def main():
    sentence = "the dog runs quickly and the cat barks"
    words = sentence.split()

    initial = initial_tag(words)
    print("Initial (naive) tagging:")
    print(" ", initial)

    final = apply_transformations(initial)
    print("\nFinal tagging after transformation-based learning:")
    print(" ", final)


if __name__ == "__main__":
    main()
