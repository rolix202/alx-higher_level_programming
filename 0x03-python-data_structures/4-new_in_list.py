#!/usr/bin/python3

def new_in_list(my_list, idx, new_element):
    if idx < 0 or idx >= len(my_list):
        my_list.copy
        return my_list
    else:
        new_list = my_list[:]
        new_list[idx] = new_element
        return new_list
