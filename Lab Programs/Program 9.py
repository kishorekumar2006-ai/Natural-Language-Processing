"""
Program 9: Implement a rule-based part-of-speech tagging system
using regular expressions.
"""

import re

# Ordered list of (regex_pattern, tag) rules
rules = [
    (r"^(the|a|an)$", "DET"),
    (r".*ing$", "VERB"),        # gerunds e.g. running
    (r".*ed$", "VERB"),         # past tense e.g. played
    (r".*es$", "VERB"),         # 3rd person singular e.g. goes
    (r".*ly$", "ADV"),          # adverbs e.g. quickly
    (r".*ould$", "MODAL"),      # modals e.g. would, could, should
    (r".*'s$", "NOUN"),         # possessive nouns
    (r".*s$", "NOUN"),          # plural nouns
    (r"^[A-Z][a-z]*$", "PROPN"),  # proper nouns (capitalized)
    (r"^\d+$", "NUM"),          # numbers
    (r".*", "NOUN"),            # default fallback rule
]


def rule_based_tag(word):
    for pattern, tag in rules:
        if re.match(pattern, word):
            return tag
    return "UNK"


def main():
    sentence = "The quick brown Fox was running and it jumped 5 times yesterday"
    words = sentence.split()

    print(f"{'Word':<12}{'Tag'}")
    print("-" * 20)
    for word in words:
        tag = rule_based_tag(word)
        print(f"{word:<12}{tag}")


if __name__ == "__main__":
    main()
