#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for j in range(x):
            print(my_list[j], end="")
    except Exception:
        print()
        return j
    print()
    return x
