#!/usr/bin/python3
import sys
argv = sys.argv[1:]
num_arg = len(argv)

if num_arg == 0:
    print("Number of argument(s): 0.")
else:
    print(f"Number of argument(s): {num_arg}{'.' if num_arg == 1 else ':'}")

    for i, arg in enumerate(argv, start=1):
        print(f"{i}: {arg}")
