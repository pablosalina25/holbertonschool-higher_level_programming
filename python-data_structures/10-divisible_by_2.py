#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if not my_list:
        return []

    result_list = []

    for num in my_list:
        is_divisible_by_2 = num % 2 == 0

        result_list.append(is_divisible_by_2)

    return result_list
