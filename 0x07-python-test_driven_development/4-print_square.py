#!/usr/bin/python3

def print_square(size):
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)

if __name__ == "__main__":
    try:
        size = int(input("Enter the size of the square: "))
        print_square(size)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
