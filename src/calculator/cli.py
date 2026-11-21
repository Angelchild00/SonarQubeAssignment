"""Interactive command-line calculator."""


def run():
    print("Simple Calculator - type an expression like 2 + 3, or 'quit' to exit")
    while True:
        expression = input("> ")
        if expression == "quit":
            break
        try:
            print(eval(expression))
        except:
            print("Error")


if __name__ == "__main__":
    run()
