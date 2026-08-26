"""
Program 1: Demonstrate how to use regular expressions in Python
to match and search for patterns in text.
"""

import re

def main():
    text = "Contact us at support@example.com or sales@example.org. Call 9876543210 or 044-12345678."

    # 1. re.match - checks match only at the beginning of string
    m = re.match(r"Contact", text)
    print("re.match result:", m.group() if m else None)

    # 2. re.search - finds first match anywhere in string
    s = re.search(r"\d{10}", text)
    print("re.search (10 digit phone):", s.group() if s else None)

    # 3. re.findall - finds all matches
    emails = re.findall(r"[\w.\-]+@[\w.\-]+\.\w+", text)
    print("All emails found:", emails)

    # 4. re.finditer - iterator of match objects with positions
    print("Phone numbers with positions:")
    for match in re.finditer(r"\d{2,4}-?\d{7,10}", text):
        print(f"  Found '{match.group()}' at position {match.start()}-{match.end()}")

    # 5. re.sub - substitution
    masked = re.sub(r"[\w.\-]+@[\w.\-]+\.\w+", "[EMAIL HIDDEN]", text)
    print("Text after masking emails:", masked)

    # 6. re.split - splitting text using pattern
    words = re.split(r"\s+", text)
    print("Words split by whitespace:", words[:8], "...")

    # 7. Pattern with groups
    pattern = re.compile(r"(\w+)@(\w+)\.(\w+)")
    for match in pattern.finditer(text):
        print(f"  Username: {match.group(1)}, Domain: {match.group(2)}, TLD: {match.group(3)}")


if __name__ == "__main__":
    main()
