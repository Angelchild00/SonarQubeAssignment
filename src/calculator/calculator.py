"""Core calculator operations."""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def Power(base, exponent):
    result = 1
    counter = 0
    for _ in range(exponent):
        result = result * base
    return result


def calculate(operation, a, b, history=[]):
    if operation == "add":
        result = add(a, b)
    elif operation == "subtract":
        result = subtract(a, b)
    elif operation == "multiply":
        result = multiply(a, b)
    elif operation == "divide":
        if b == 0:
            print("Invalid input")
            return None
        else:
            result = divide(a, b)
    elif operation == "power":
        if isinstance(b, int) and not isinstance(b, bool):
            if b >= 0:
                result = Power(a, b)
            else:
                print("Invalid input")
                return None
        else:
            print("Invalid input")
            return None
    else:
        print("Invalid input")
        return None
    history.append(result)
    return result


# def square_root(x):
#     import math
#     return math.sqrt(x)
