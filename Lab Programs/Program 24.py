"""
Program 24: Recognize dialog acts in a given dialog or conversation
using a simple rule-based classifier.

Dialog act categories: GREETING, QUESTION, STATEMENT, REQUEST,
THANKING, FAREWELL
"""

import re


def classify_dialog_act(utterance):
    text = utterance.strip().lower()

    greeting_patterns = [r"\bhi\b", r"\bhello\b", r"\bhey\b", r"good (morning|afternoon|evening)"]
    farewell_patterns = [r"\bbye\b", r"goodbye", r"see you", r"take care"]
    thanking_patterns = [r"\bthanks\b", r"thank you", r"much appreciated"]
    request_patterns = [r"^please\b", r"could you", r"can you", r"would you mind"]

    for pattern in greeting_patterns:
        if re.search(pattern, text):
            return "GREETING"

    for pattern in farewell_patterns:
        if re.search(pattern, text):
            return "FAREWELL"

    for pattern in thanking_patterns:
        if re.search(pattern, text):
            return "THANKING"

    for pattern in request_patterns:
        if re.search(pattern, text):
            return "REQUEST"

    if text.endswith("?") or re.match(r"^(what|who|where|when|why|how|is|are|do|does|can|could)\b", text):
        return "QUESTION"

    return "STATEMENT"


def main():
    dialog = [
        "Hi there!",
        "How are you doing today?",
        "I am doing well, thank you.",
        "Could you please help me book a flight?",
        "Sure, where would you like to go?",
        "I want to go to Chennai next week.",
        "Thanks a lot for your help.",
        "You're welcome. Goodbye!",
    ]

    print(f"{'Utterance':<45}{'Dialog Act'}")
    print("-" * 65)
    for utterance in dialog:
        act = classify_dialog_act(utterance)
        print(f"{utterance:<45}{act}")


if __name__ == "__main__":
    main()
