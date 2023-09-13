#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """
    search and replace function
    Args:
        my_list: list
        search: element to search for
        replace: element to replace search with

    Return:
        Nothing
    """

    if not my_list:
        return my_list
    new_list = my_list.copy()
    while search in new_list:
        pos = new_list.index(search)
        new_list.insert(pos, replace)
        new_list.pop(pos + 1)
    return new_list
