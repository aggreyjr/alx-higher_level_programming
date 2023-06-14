#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """function that replaces all occurrences of
    an element by another in a new list"""
    new_list = my_list.copy()

    for m in range(len(new_list)):
        if new_list[m] == search:
            new_list[m] = replace
    return new_list
