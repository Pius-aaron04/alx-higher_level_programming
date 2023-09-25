#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        n = 0
        for i in range(x):
            print(my_list[i], end='')
            n += 1
        print()
    except IndexError:
        print()
        return n
    else:
        return n
