#!/usr/bin/python3
import sys
numbers = sys.argv
result = 0
if __name__ == "__main__":
    for number in numbers[1:]:
        result += int(number)
    print(result)
