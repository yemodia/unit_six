# Yerim Dia
# October 25, 2018
# Introduction to Computer Science

# This program is based in the Birthday Paradox
# This program starts off by getting a number of simulations that the user wants to run
# Then the program generates a lists of 23 birthdays from 1 to 365
#


import random


def number_simulation():
    """
    This function gets the 
    :return: This returns the number of simulations the user wishes to run
    """
    user_simulation = int(input("How many simulations do you wish to run?"))
    return user_simulation


def birthday_lists():
    birthdays = []
    for i in range(23):
            birthdays.append(random.randint(1, 365))
    return birthdays


def duplicate_birthdays(birthdays):
    #   A set deletes all duplicates in the list and then checks
    check_birthdays = set(birthdays)
    if len(check_birthdays) < len(birthdays):
        return True
    else:
        return False


def main():
    user_simulation = number_simulation()
    birthday_match = 0
    for i in range(user_simulation):
        birthday_check = birthday_lists()
        duplicate_birthdays(birthday_check)
        if duplicate_birthdays(birthday_check) == True:
                birthday_match += 1
    print("There was", birthday_match, "of the same birthday")
    birthday_percent = birthday_match / user_simulation * 100
    print(" This is about", birthday_percent, "% of the time ")


main()
