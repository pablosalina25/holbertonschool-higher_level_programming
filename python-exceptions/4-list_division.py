#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    finished_list = []
    try:
        for j in range(list_length):
            finished_list.append(my_list_1[j] / my_list_2[j])
    except IndexError:
        finished_list.append(0)
        print("out of range")
    except TypeError:
        finished_list.append(0)
        print("wrong type")
    except ZeroDivisionError:
        finished_list.append(0)
        print("division by 0")
    finally:
        return finished_list
    