#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < my_list[0]:
        return None
    elif idx >= len(my_list):
        return None
    return my_list[idx]
