#!/usr/bin/python3


import pyfiglet
from termcolor import cprint
from datetime import datetime as dt
import random, string


print_red = lambda x: cprint(x, 'red')
print_green = lambda x: cprint(x, 'green')
print_blue = lambda x: cprint(x, 'blue')


#intro
print("\n")
print("WELCOME TO...")
ascii_banner = pyfiglet.figlet_format("p@ssg3n",)
print_green(ascii_banner)
print("A simple CLI password generator")
print_red("WARNING: The passwords generated by this tool are in plain text!\n")


letters_up_low = list(string.ascii_letters)
nums = list(string.digits)
specials = list("!@#$%^&*()")
char_all = list(string.ascii_letters + string.digits + "!@#$%^&*()")


def pass_gen():

    while True:
        charlen = int(input("\nHow many characters does your password need? Pick a number between 8 and 32:\n>>>"))
        if charlen < 8:
            print("\nToo few characters; please pick a number between 8 & 32")
            continue
        if charlen > 32:
            print("\nToo many characters; please pick a number between 8 & 32")
            continue
        if charlen > 7 and charlen < 33:
            break

    letters_up_low_count = int(input("\nHow many letters (Both upper and lower case) do you require?:\n>>>"))
    nums_count = int(input("\nHow many numbers (0-9) do you require?:\n>>>"))
    specials_count = int(input("\nHow many special characters (!@#$%^&*) do you require?:\n>>>"))
    charlen_total = letters_up_low_count + nums_count + specials_count

    if charlen_total > charlen:
        print("\nToo many characters selected; must not exceed password length.")
        return
    
    password = []

    for i in range(letters_up_low_count):
        password.append(random.choice(letters_up_low))

    for i in range(nums_count):
        password.append(random.choice(nums))

    for i in range(specials_count):
        password.append(random.choice(specials))

    if charlen_total < charlen:
        random.shuffle(char_all)
        for i in range(charlen - charlen_total):
            password.append(random.choice(char_all))

    random.shuffle(password)

    print("\n")
    print('-' *40)
    print(f'Password generated at:\n {str(dt.now())}')
    print('-' *40) 
    print("\nYour Password is:")   
    print_green("".join(password))

    #ADD: SAVE TO FILE FUNCTIONALITY
    #save_file = input("\nDo you want to save a text file with your password? y/[n]:\n>>>")
    #if save_file in ('y', 'Y'):
    #    print_red("\nWarning: If using existing filename, contents will be overwritten!\n") #add append funcionality in future
    #    save_file_name = open("~/Desktop/" + input("Enter name of file to be placed on '~/Desktop'...(Syntax:'filename.txt'):\n>>>"))
    #    save_file_name.write(password)    
    #    print(save_file_name)
    #else:
    #    print("Have a nice day")
    

pass_gen()
