#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    my_list = []
    new_matrix = []
    if len(matrix) == 0:
        return new_matrix
    for i in matrix:
        for j in i:
            my_list.append(j*j)
        new_matrix.append(my_list[:])
        my_list.clear()
    return new_matrix
