#!/usr/bin/python3
import dis
def magic_calculation(a, b, c):
    if a < b:
        if c > b:
            return (a * b) - c;
        return a + b;
    else:
        return c
