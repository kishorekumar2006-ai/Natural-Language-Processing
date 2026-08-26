"""
Program 14: Check for subject-verb agreement in sentences based on
context-free grammar rules (singular/plural agreement).
"""

# Simple lexicon annotated with number (sg = singular, pl = plural)
determiners = {"the": "both", "a": "sg", "an": "sg"}
nouns = {
    "dog": "sg", "dogs": "pl",
    "cat": "sg", "cats": "pl",
    "child": "sg", "children": "pl",
    "boy": "sg", "boys": "pl",
}
verbs = {
    "runs": "sg", "run": "pl",
    "barks": "sg", "bark": "pl",
    "plays": "sg", "play": "pl",
    "is": "sg", "are": "pl",
}


def check_agreement(sentence):
    words = sentence.lower().split()

    if len(words) < 3:
        return False, "Sentence too short to check agreement (need Det N V)."

    det, noun, verb = words[0], words[1], words[2]

    if det not in determiners:
        return False, f"'{det}' is not a recognized determiner."
    if noun not in nouns:
        return False, f"'{noun}' is not a recognized noun."
    if verb not in verbs:
        return False, f"'{verb}' is not a recognized verb."

    noun_number = nouns[noun]
    verb_number = verbs[verb]
    det_number = determiners[det]

    if det_number != "both" and det_number != noun_number:
        return False, f"Determiner '{det}' does not agree with noun '{noun}' ({noun_number})."

    if noun_number != verb_number:
        return False, (f"Agreement error: noun '{noun}' is {noun_number} "
                        f"but verb '{verb}' is {verb_number}.")

    return True, f"Sentence is grammatically correct ({noun_number} agreement)."


def main():
    test_sentences = [
        "the dog runs",
        "the dogs run",
        "a dog run",       # incorrect
        "the children play",
        "the child plays",
        "the cats barks",  # incorrect
    ]

    for sentence in test_sentences:
        valid, message = check_agreement(sentence)
        status = "VALID" if valid else "INVALID"
        print(f"[{status}] '{sentence}' -> {message}")


if __name__ == "__main__":
    main()
