def number_keys(a_dictionary):
    n = 0
    if len(a_dictionary) == 0:
        return n
    for i in a_dictionary:
        n += 1
    return n
