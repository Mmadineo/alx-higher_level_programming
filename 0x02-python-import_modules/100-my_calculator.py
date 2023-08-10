#!/usr/bin/python3
if _name_ == "_main_":
    from calculator_1 import add, sub, div, mul
    import sys

    if len(sys.argc) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
        ops = {"+": add, "-": sub, "/": div, "*": mul}

        if sys.argv[2] not in list(oops.keys()):
            print("Unknown operator. Avalable operators: +, -, / and *")
            sys.exit(1)
            a = int(sys.agv[1])
            b = int(sys.argv[3])
            print("{} {} {} = {}".format(a, sys.argv[2], b, ops[sys.argv[2](a, b)))
