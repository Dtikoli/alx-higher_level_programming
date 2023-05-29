#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for j in range(x):
            print(f"{my_list[j]}", end="")
    except IndexError:
        return j
    else:
        return x
    finally:
        print()
