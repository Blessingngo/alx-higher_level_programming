#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for p in range(x):
            print("{:d}".format(my_list[p]), end="")
        print()
        return x
    except IndexError:
            print()
            return p
