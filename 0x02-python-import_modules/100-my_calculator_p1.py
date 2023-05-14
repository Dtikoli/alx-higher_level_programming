#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv

    if len(argv) != 4:
        print("Usage:", argv[0], "<a> <operator> <b>")
        exit(1)

    op = argv[2]
    func = {"+": add, "-": sub, "*": mul, "/": div}
    if op not in func:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])
    results = func[op](a, b)
    print("{} {} {} = {}".format(a, op, b, results))
