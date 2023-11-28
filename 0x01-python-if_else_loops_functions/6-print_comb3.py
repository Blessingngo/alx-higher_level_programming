#!/usr/bin/python3
for ten_digit in range(0, 9):
    for one_digit in range(ten_digit + 1, 10):
        if ten_digit == 8:
            print("{:d}{:d}".format(ten_digit, one_digit))
            break
        print("{:d}{:d}".format(ten_digit, one_digit), end=", ")
