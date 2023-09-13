#!/usr/bin/python3
def roman_to_int(roman_string):
    """
    roman to int
    converts roman numeral to integer

    Args:
        roman_string: roman numeral to be converted
    Return Values:
        integer form of numeral
    """
    if not roman_string:
        return 0
    roman_rep = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
            }
    integer = 0
    for i, letter in enumerate(roman_string):
        val = roman_rep.get(letter)
        x = i - 1
        if not val:
            return integer
        if not x < 0 and val > roman_rep.get(roman_string[x]):
            integer += val - (2 * roman_rep.get(roman_string[x]))
        else:
            integer += val
    return integer
