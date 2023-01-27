#!/usr/bin/python3
def uniq_add(my_list=[]):
    n = 0
    if len(my_list) == 0:
        return n
    new_list = []
    for i in my_list:
        if i not in new_list:
            new_list.append(i)
    for i in new_list:
        n += i
    return n
