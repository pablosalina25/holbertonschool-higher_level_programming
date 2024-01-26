#!/usr/bin/python3
if __name__ == "__main__":
    argument = []
    cont = 0
    while cont < len(argument):
        if len(argument) == 0:
            print("0 {} arguments.".format(len(argument), argument))
            cont += 1
        elif len(argument) == 1:
            print("{} argument: {}".format(len(argument), argument))
            cont += 1
        elif len(argument) > 1:
            print("{} arguments: {}".format(len(argument), argument))
            cont += 1
