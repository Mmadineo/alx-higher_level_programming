#!/usr/bin/python3
"""Define a locke class"""


class LockedClass:
    """
    Stop the user from instantiating new LockedClass attaributes for anything but attributes called 'first_name'
    """

    __slots__ = ["first_name"]
