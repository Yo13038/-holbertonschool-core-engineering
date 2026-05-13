#!/usr/bin/env python3
"""module of the classe square
"""


Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """class square inherits from Rectangle"""

    def __init__(self, size):
        """initialise square from Rectangle"""

        self.integer_validator("size", size)

        super().__init__(size, size)

        self.__size = size
