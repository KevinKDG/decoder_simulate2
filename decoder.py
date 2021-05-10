#!/usr/bin/env python
"""
This code codes and decodes a certain word
"""

def break_text(text):                   # Breaks up a text in characters and puts it in a list
    text_list = []
    length_text = len(text)
    for i in range(length_text):
        text_list.append(text[i:i + 1])
    return text_list


def code_text(text): # Changes every character requested to a different one. You can make your own code/decoder here
    if text == "a":
        return "b"
    if text == "b":
        return "c"
    if text == "c":
        return "d"
    if text == "d":
        return "e"
    if text == "e":
        return "f"
    if text == "f":
        return "g"
    if text == "g":
        return "h"
    if text == "h":
        return "i"
    if text == "i":
        return "j"
    if text == "j":
        return "k"
    if text == "k":
        return "l"
    if text == "l":
        return "m"
    if text == "m":
        return "n"
    if text == "n":
        return "o"
    if text == "o":
        return "p"
    if text == "p":
        return "q"
    if text == "q":
        return "r"
    if text == "r":
        return "s"
    if text == "s":
        return "t"
    if text == "t":
        return "u"
    if text == "u":
        return "v"
    if text == "v":
        return "w"
    if text == "w":
        return "x"
    if text == "x":
        return "y"
    if text == "y":
        return "z"
    if text == "z":
        return "a"
    if text == " ":
        return "?"


def decode_text(text): # Changes every character requested to a different one. You can make your own code/decoder here
    if text == "a":
        return "z"
    if text == "b":
        return "a"
    if text == "c":
        return "b"
    if text == "d":
        return "c"
    if text == "e":
        return "d"
    if text == "f":
        return "e"
    if text == "g":
        return "f"
    if text == "h":
        return "g"
    if text == "i":
        return "h"
    if text == "j":
        return "i"
    if text == "k":
        return "j"
    if text == "l":
        return "k"
    if text == "m":
        return "l"
    if text == "n":
        return "m"
    if text == "o":
        return "n"
    if text == "p":
        return "o"
    if text == "q":
        return "p"
    if text == "r":
        return "q"
    if text == "s":
        return "r"
    if text == "t":
        return "s"
    if text == "u":
        return "t"
    if text == "v":
        return "u"
    if text == "w":
        return "v"
    if text == "x":
        return "w"
    if text == "y":
        return "x"
    if text == "z":
        return "y"
    if text == "?":
        return " "


def get_code(text):
    list_to_code = break_text(text)      # Takes a text and uses the break_text function to create a list with letters.
    coded_text = ""
    for x in list_to_code:               # Goes over te list and changes each index
        coded_text += str(code_text(x))
    return coded_text


def get_decode(text):                         # Takes a text and uses the break_text function to create a list with letters.
    list_to_decode = break_text(text)
    decoded_text = ""
    for x in list_to_decode:            # Goes over te list and changes each index
        decoded_text += str(decode_text(x))
    return decoded_text

