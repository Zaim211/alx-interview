#!/usr/bin/python3
""" UTF-8 Validation """


def validUTF8(data):
    """  method that determines if a given data set
    represents a valid UTF-8 encoding
    """
    byte = 0

    for x in data:
        if byte == 0:
            if x >> 5 == 0b110 or x >> 5 == 0b1110:
                byte = 1
            elif x >> 4 == 0b1110:
                byte = 2
            elif x >> 3 == 0b11110:
                byte = 3
            elif x >> 7 == 0b1:
                return False
        else:
            if x >> 6 != 0b10:
                return False
            byte -= 1
    return byte == 0
