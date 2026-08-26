"""
Program 2: Implement a basic finite state automaton (FSA) that recognizes
strings ending with 'ab'.

States:
    q0 - start state
    q1 - last symbol read was 'a'
    q2 - accepting state, last two symbols were 'ab'
"""


def fsa_ends_with_ab(input_string):
    state = "q0"

    transition = {
        "q0": {"a": "q1", "b": "q0"},
        "q1": {"a": "q1", "b": "q2"},
        "q2": {"a": "q1", "b": "q0"},
    }

    for symbol in input_string:
        if symbol not in ("a", "b"):
            return False  # invalid alphabet symbol
        state = transition[state][symbol]

    return state == "q2"


def main():
    test_strings = ["ab", "aab", "abb", "abab", "b", "a", "bbab", "aba", "ababab", ""]

    print(f"{'String':<10}{'Accepted?':<10}")
    print("-" * 20)
    for s in test_strings:
        result = fsa_ends_with_ab(s)
        print(f"{s:<10}{str(result):<10}")

    # Allow user input testing
    user_input = "aabab"
    print(f"\nCustom test: '{user_input}' -> {fsa_ends_with_ab(user_input)}")


if __name__ == "__main__":
    main()
