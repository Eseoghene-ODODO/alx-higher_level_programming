#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < my_list[0]:
        return None
    elif idx > my_list[4]:
        return None
    else:
        return my_list[idx]
