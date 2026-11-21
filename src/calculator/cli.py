"""Interactive command-line calculator."""

import re

from calculator.calculator import calculate

OPERATORS = {
    "+": "add",
    "-": "subtract",
    "*": "multiply",
    "/": "divide",
    "**": "power",
}

# A number, an operator, and a number, e.g. "2 + 3", "2+3", "-1.5 * 4"
EXPRESSION_PATTERN = re.compile(
    r"^\s*(-?\d+(?:\.\d+)?)\s*(\*\*|[+\-*/])\s*(-?\d+(?:\.\d+)?)\s*$"
)


def _to_number(text):
    return float(text) if "." in text else int(text)


def evaluate(expression):
    """Safely evaluate 'number operator number'. Returns None for invalid input."""
    match = EXPRESSION_PATTERN.match(expression)
    if match is None:
        return None
    left, symbol, right = match.groups()
    return calculate(OPERATORS[symbol], _to_number(left), _to_number(right))


def run():
    print("Simple Calculator - type an expression like 2 + 3, or 'quit' to exit")
    while True:
        expression = input("> ")
        if expression == "quit":
            break
        result = evaluate(expression)
        print("Error" if result is None else result)


if __name__ == "__main__":
    run()
