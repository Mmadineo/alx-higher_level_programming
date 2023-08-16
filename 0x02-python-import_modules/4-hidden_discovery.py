#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    names = dir(hidden_4)
    for names in names:
        if names[:2} != "_":
            print(name)
