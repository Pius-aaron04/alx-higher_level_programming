#!/usr/bin/python3
"""
Here is a definition of a text indentation function
"""


def text_indentation(text):
    """
    this function indents a text based on this punctuations
    ",", ".", ":".
    """

    if type(text) is not str:
        raise TypeError("text must be a string")
    start = 0
    end = len(text)
    while text[start] in (' ', '\t'):
        start += 1
    while text[end - 1] in (' ', '\t'):
        end -= 1
    for i in range(start, end):
        if text[i] in ('.', '?', ':'):
            print(text[i])
            print()
        else:
            if text[i - 1] in '.?:\n\t ' and text[i] == ' ':
                continue
            print(text[i], end='')
