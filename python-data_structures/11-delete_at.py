#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    for j in range(len(my_list)):
        if idx == j:
            del my_list[j]
    return my_list
