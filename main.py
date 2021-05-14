#!/usr/bin/env python
"""
Encode & decode text from input or from a .txt file

doesn't work with capital letter, numbers and special characters
"""


#               IMPORTS               #
import sys
import time
from datetime import datetime
import string
from pathlib import Path

#            IMPORTS SCRIPTS          #
import decoder
#          AUTHOR INFORMATION         #

#        _____
#      .'     `.
#     /  .-=-.  \   \ __
#     | (  C\ \  \_.'')
#     _\  `--' |,'   _/
#    /__`.____.'__.-' The coding snail~

__author__ = "Kevin Vervloet"
__email__ = "kevin.vervloet@student.kdg.be"
__Version__ = "V4.0"
__status__ = "Finished"

#              VARIABLES              #
time_now = datetime.now()
current_time = time_now.strftime("%H:%M:%S")

invalidcharacters = set(string.punctuation) # blocks all special characters from being used


#              MAIN CODE              #
def num_there(s):
    return any(i.isdigit() for i in s)


def menu():
    print("[", current_time, "]", " ====Encode/Decode===")  # Print the time & a title

    optionmenu = (input("""                                  
--------------------------------  
| [1] Decode                   |
| [2] Encode                   |
| [3] Exit                     |                                                                     
--------------------------------\n"""))
    if optionmenu == "1":  # Decode
        optie2 = (input(""" 
Do you want to decode from a file or manual input ?
[1] From file
[2] From manual input\n"""))
        if optie2 == "1":
            text = Path('text2decode.txt').read_text()  # read from a text file
            text = text.replace('\n', '')

            decoder.break_text(text)
            decoder.decode_text(text)
            print("We've hacked the code, here is the decoded version:")
            print("")
            decoder.get_decode(text)

        elif optie2 == "2":
            text = input("Input the text you want to decode\n")
            if num_there(text):
                print("error! your text contains numbers - Returning to the menu")      # Check for numbers
                time.sleep(2)
                menu()

            decoder.break_text(text)
            decoder.decode_text(text)
            print("we've hacked the code, here is the decoded version:")
            print("")
            decoder.get_decode(text)
        elif optie2 != "1" or "2":
            print("Invalid option we will return you to the menu")  # return to the menu
            menu()

    elif optionmenu == "2":       # encoding
        optie2 = (input(""" 
Do you want to encode from a file or manual input ?
[1] From file
[2] From manual input\n"""))
        if optie2 == "1":
            text = Path('text2encode.txt').read_text()  # read from a text file
            text = text.replace('\n', '')

            decoder.break_text(text)
            decoder.code_text(text)
            print("We've coded your top secret message:")
            print("")
            decoder.get_code(text)

        elif optie2 == "2":
            text = input("Input the text you want to code:\n")
            if num_there(text):
                print("error! your text contains numbers - Returning to the menu")
                time.sleep(2)
                menu()
            else:
                if any(char in invalidcharacters for char in text):
                    print("error! your text contains special characters - Returning to the menu")
                    time.sleep(2)
                    menu()

            decoder.break_text(text)
            decoder.code_text(text)
            print("We've coded your top secret message:")
            print("")
            decoder.get_code(text)

        elif optie2 != "1" or "2":
            print("Invalid option we will return you to the menu")  # return to the menu
            menu()

    elif optionmenu == "3":
        print("See you next time!")
        sys.exit(0)

    elif optionmenu != "1" or "2" or "3" or "4":
        print("Error! not a valid input - Please try again")
        time.sleep(1)
        print("")
        print("")
        menu()


if __name__ == '__main__':    # run tests if called from command-line
    menu()