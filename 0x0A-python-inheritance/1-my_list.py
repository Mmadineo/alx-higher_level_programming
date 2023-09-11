#!/usr/bin/python3

"""Define an inherited class list MyList"""


class MyList(list):
    """IMplement sorted printing for built-in class list."""

    def print_sorted(self):
        """Print list in sorted ascending order."""
        print(sorted(self))
