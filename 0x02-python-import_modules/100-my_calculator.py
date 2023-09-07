#!/usr/bin/python3
if __name__ == "__main__":
    """Handle basic arithmetic operations."""
    from calculator_1 import add, sub, mul, div
    import sys

    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <num1> <operator> <num2>")
        sys.exit(1)

    ops = {"+": add, "-": sub, "*": mul, "/": div}
    if sys.argv[2] not in list(ops.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    num1 = int(sys.argv[1])
    num2 = int(sys.argv[3])
    print("{} {} {} = {}".format(num1, sys.argv[2], num2,
          ops[sys.argv[2]](num1, num2)))
