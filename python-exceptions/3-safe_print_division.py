#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        c = None
        c = a / b
        return c
    except:
        return None
    finally:
        if c is None:
            print("Inside result: None")
        else:
            print("Inside result: {:0.1f}".format(c))
