#!/usr/bin/python3
def magic_calculation(a, b):
    from magic_calculation_102 import add, sub
    if a < b:
        c = sub(a, b)
        for i in range(4, 6):
            c = sub(c, i)
        return c
    else:
        return (sub(a, b))
    return None
