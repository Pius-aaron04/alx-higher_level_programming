#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    my_list = my_list.copy()
    if idx > len(my_list) or idx < 0:
        return my_list
    my_list[idx] = element
    return my_list
