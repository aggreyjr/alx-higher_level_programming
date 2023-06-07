#!/usr/bin/python3
def uppercase(string):
    for char in string:
        u_char = chr(ord(char) - 32) if ord('a')
        <= ord(char) <= ord('z') else char
        print("{}".format(u_char), end='')
    print()
