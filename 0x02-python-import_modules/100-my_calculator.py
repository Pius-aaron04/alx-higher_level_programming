#!/usr/bin/python3
import sys
from calculator_1 import add, mul, sub, div
argv = sys.argv[1:]
operation = {
        "+": add,
        "*": mul,
        "-": sub,
        "/": div
}
if __name__ == "__main__":
    if len(argv) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    if argv[1] not in '+-*/':
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    a, op, b = argv
    print("{} {} {} = {}".format(a, op, b, operation[op](int(a), int(b))))
