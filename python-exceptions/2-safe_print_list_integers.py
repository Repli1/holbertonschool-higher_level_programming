#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        n = 0
        for i in range(0, x):
            if type(my_list[i]) == int:
                print("{:d}".format(my_list[i]), end="")
                n += 1
                if n == x:
                    break
        print("")
        return n
    except Exception as Ind:
        raise Ind
