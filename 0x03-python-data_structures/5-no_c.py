#!/usr/bin/python3
def no_c(my_str):
    length = len(my_str)

    a = 0

    new_str = my_str[:]

    for i in range(length):
        if (my_str[i] == 'c' or my_str[i] == 'C'):
            new_str = new_str[:(i - j)] + my_str[(i + 1):]
            a += 1

    return (new_str)
