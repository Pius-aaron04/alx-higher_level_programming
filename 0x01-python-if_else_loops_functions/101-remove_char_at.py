#!/usr/bin/python3
def remove_char_at(string, n):
    if n > len(string):
        return string
    new_string = ""
    for i, c in enumerate(string):
        if i == n:
            continue
        new_string += c
    return new_string
