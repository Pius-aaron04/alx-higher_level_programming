#!/usr/bin/python3
def max_integer(my_list=[]):
    max_num = my_list[0]
    if len(my_list) == 0:
        return None
    for num in my_list:
        # checks if current number is greater than max_num
        if type(num) is not int:
            return None
        if num > max_num:
            max_num = num
    return max_num
