"""
Program 18: Implement a simple First Order Predicate Calculus (FOPC)
parser for basic logical expressions.

Supports expressions like:
    forall x (Human(x) -> Mortal(x))
    exists x (Student(x) & Smart(x))
    Loves(John, Mary)
"""

import re


TOKEN_SPEC = [
    ("QUANT", r"forall|exists"),
    ("AND", r"&"),
    ("OR", r"\|"),
    ("NOT", r"~|not"),
    ("IMPLIES", r"->"),
    ("IFF", r"<->"),
    ("LPAREN", r"\("),
    ("RPAREN", r"\)"),
    ("COMMA", r","),
    ("PREDICATE", r"[A-Z][a-zA-Z0-9_]*(?=\()"),
    ("VARIABLE", r"[a-z][a-zA-Z0-9_]*"),
    ("CONSTANT", r"[A-Z][a-zA-Z0-9_]*"),
    ("SKIP", r"[ \t]+"),
]

master_pattern = re.compile("|".join(f"(?P<{name}>{pattern})" for name, pattern in TOKEN_SPEC))


def tokenize(expression):
    tokens = []
    for match in master_pattern.finditer(expression):
        kind = match.lastgroup
        value = match.group()
        if kind == "SKIP":
            continue
        tokens.append((kind, value))
    return tokens


def parse_fopc(expression):
    """A simplified structural parser: tokenizes and identifies the
    logical components (quantifiers, predicates, connectives, terms)."""
    tokens = tokenize(expression)

    quantifiers = [v for k, v in tokens if k == "QUANT"]
    predicates = [v for k, v in tokens if k == "PREDICATE"]
    variables = [v for k, v in tokens if k == "VARIABLE"]
    constants = [v for k, v in tokens if k == "CONSTANT" and v not in predicates]
    connectives = [v for k, v in tokens if k in ("AND", "OR", "NOT", "IMPLIES", "IFF")]

    return {
        "expression": expression,
        "tokens": tokens,
        "quantifiers": quantifiers,
        "predicates": predicates,
        "variables": list(set(variables)),
        "constants": list(set(constants)),
        "connectives": connectives,
    }


def display_analysis(analysis):
    print(f"\nExpression: {analysis['expression']}")
    print(f"  Tokens       : {analysis['tokens']}")
    print(f"  Quantifiers  : {analysis['quantifiers']}")
    print(f"  Predicates   : {analysis['predicates']}")
    print(f"  Variables    : {analysis['variables']}")
    print(f"  Constants    : {analysis['constants']}")
    print(f"  Connectives  : {analysis['connectives']}")


def main():
    expressions = [
        "forall x (Human(x) -> Mortal(x))",
        "exists x (Student(x) & Smart(x))",
        "Loves(John, Mary)",
        "forall x (Bird(x) -> Flies(x) | Penguin(x))",
        "~Rains(today) -> Sunny(today)",
    ]

    for expr in expressions:
        analysis = parse_fopc(expr)
        display_analysis(analysis)


if __name__ == "__main__":
    main()
