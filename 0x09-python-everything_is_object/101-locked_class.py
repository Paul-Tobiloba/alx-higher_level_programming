#!/usr/bin/python3
"""A class that __slots__ instead of __dict__"""


class LockedClass:
"""Locked class"""

    __slots__ = ['first_name']

    def __init__(self, first_name=''):
        self.first_name = first_name
