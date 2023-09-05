#!/usr/bin/python3
def print_last_digit(number):
    if type(number) is int:
        print(str(number)[-1], end='')
    return int(str(number)[-1])
