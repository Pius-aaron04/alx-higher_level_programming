#!/usr/bin/python3
import sys
argv = sys.argv[1:]
n = len(argv)
if __name__ == "__main__":
    if n == 1:
        print("1 argument")
    elif n == 0:
        print("0 arguments.")
    else:
        print("{} agruments:".format(n))
    for i, arg in enumerate(argv):
        print("{}: {}".format(i + 1, arg))
