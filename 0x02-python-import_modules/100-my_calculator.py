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
        sys.stderr.write("Usage: ./100-my_calculator.py <a> <operator> <b>\n")
        sys.exit(1)
    if argv[1] not in '+-*/':
        sys.stderr.write("Unknown operator. Available operators:" +
                         "+, -, * and /\n")
        sys.exit(1)
    a, op, b = argv
    print("{} {} {} = {}".format(a, op, b, operation[op](int(a), int(b))))
