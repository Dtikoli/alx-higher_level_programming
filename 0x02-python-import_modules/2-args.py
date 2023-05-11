#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    ac = len(argv)
    if ac == 1:
        print("0 arguments.")
    elif ac == 2:
        print("{:d} argument:".format(ac - 1))
    else:
        print("{:d} arguments:".format(ac - 1))
    for i in range(1, ac):
        print("{}: {}".format(i, argv[i]))
