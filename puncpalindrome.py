# Markhus Dammar
# 7 April 2020
# This program will use a recursive formula to check if a string is a Palindrome or not.
# Will reuse original code to write a new program that checks for punctuation.

import time


def true():
    print("This string is a Palindrome.")


def false():
    print("This string is not a Palindrome.")


def punc(string):
    return ''.join(i for i in string if i.isalnum())


def p_check(string):
    string.strip()
    string = punc(string)
    string = string.lower().replace(" ", "")
    print(string)
    time.sleep(0.5)
    if len(string) < 1:      # BASE CASE
        true()
    elif string[0] == string[-1]:
        return p_check(string[1:-1])    # Will check each letter until base case is reached
    else:
        false()


def welcome():
    print("""
    --------PALINDROME CHECK VERSION 2.1--------
    Welcome. Please enter a word or sentence and 
    we'll check if it is a Palindrome or not.""")
    usrstring = str(input(">>>"))
    p_check(usrstring)
    time.sleep(2)
    next()


def next():
    print("Now what?")
    choice = int(input("""
    TYPE 1 or 2
        1. Restart
        2. Exit
        >>>"""))
    if choice == 1:
        welcome()
    elif choice == 2:
        exit()
    else:
        print("INVALID CHOICE")
        time.sleep(1)
        next()

# Program starts here
welcome()
