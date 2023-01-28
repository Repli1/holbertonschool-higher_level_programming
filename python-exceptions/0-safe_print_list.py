#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    n = 0
    try:
        for element in my_list:
            n += 1
        if x < n:
            n = x
        for i in range(0, x):
            print(my_list[i], end="")
        print("")
    except:
        print("")
        return n
    return n
