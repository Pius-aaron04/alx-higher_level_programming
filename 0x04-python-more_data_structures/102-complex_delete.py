#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if not a_dictionary:
        return a_dictionary
    d_list = []
    for k, v in a_dictionary.items():
        if value == v:
            d_list.append(k)
    for d in d_list:
        del a_dictionary[d]
    return (a_dictionary)
