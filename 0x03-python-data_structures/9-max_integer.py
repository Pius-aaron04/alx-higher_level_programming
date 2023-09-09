#!/usr/bin/python3
def max_integer(my_list=[]):
    max_num = my_list[0]
    if my_list == []:
        return None
    for num in my_list:
        # checks if current number is greater than max_num
        if num > max_num:
            max_num = num
    return max_num
