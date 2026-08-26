"""
Program 4: Implement a finite-state machine for morphological parsing.
This machine generates plural forms of English nouns based on
simple orthographic rules (a simplified two-level morphology).
"""


def pluralize(noun):
    """
    Finite-state style rule application for pluralization:
      1. If word ends in s, x, z, ch, sh -> add 'es'
      2. If word ends in consonant + y -> replace y with 'ies'
      3. If word ends in f -> replace f with 'ves'
      4. If word ends in fe -> replace fe with 'ves'
      5. Otherwise -> add 's'
    """
    vowels = "aeiou"
    noun_lower = noun.lower()

    # State-based checks (simulating FSM transitions)
    if noun_lower.endswith(("s", "x", "z", "ch", "sh")):
        state = "ADD_ES"
        plural = noun + "es"
    elif noun_lower.endswith("y") and len(noun) > 1 and noun_lower[-2] not in vowels:
        state = "Y_TO_IES"
        plural = noun[:-1] + "ies"
    elif noun_lower.endswith("fe"):
        state = "FE_TO_VES"
        plural = noun[:-2] + "ves"
    elif noun_lower.endswith("f"):
        state = "F_TO_VES"
        plural = noun[:-1] + "ves"
    else:
        state = "ADD_S"
        plural = noun + "s"

    return plural, state


def main():
    nouns = ["cat", "bus", "box", "church", "brush", "city", "baby",
             "knife", "leaf", "dog", "toy", "wolf", "wife"]

    print(f"{'Singular':<12}{'Plural':<15}{'Rule Applied (State)'}")
    print("-" * 45)
    for noun in nouns:
        plural, state = pluralize(noun)
        print(f"{noun:<12}{plural:<15}{state}")


if __name__ == "__main__":
    main()
