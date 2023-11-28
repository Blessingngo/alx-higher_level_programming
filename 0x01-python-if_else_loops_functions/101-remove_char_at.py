#!/usr/bin/python3
def remove_char_at(str, n):
    p = ""
    for s in range(len(str)):
        if p != n:
            p = p + str[s]
    return (p)
