#!/usr/bin/python3
def element_at(my_list, idx):
    for idx in range(len(my_list)):
        if idx < 0:
            return (NONE)
        length = len(my_list)

	if idx > length -1:
            return (NONE)
        return(my_list[idx])
