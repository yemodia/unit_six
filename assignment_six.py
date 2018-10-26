# Yerim Dia
# October 25, 2018
# Introduction to Computer Science

# This program is based on the Birthday Paradox.
# This program starts off by getting a number of simulations that the user wants to run.
# Then the program generates lists of 23 birthdays from 1 to 365.
# It checks for the duplicate birthdays and keeps track of how many duplicate birthdays there are.
# Then it will repeat depending on how many simulations the user desires
# In th end it will have kept track of all the same birthdays and divide that number by the total simulations
# It will return the number to th user as a percentage and it should be about 50%.


import random


def number_simulation():
    """
    This function gets the number of simulations the user wants as an integer
    :return: This returns the number of simulations the user wishes to run as an integer
    """
    user_simulation = int(input("How many simulations do you wish to run?"))
    return user_simulation


def birthday_lists():
    """
    This function generates the random birthdays from 1 to 365
    :return: This returns the list of birthdays as a list
    """
    birthdays = []
    for i in range(23):
            birthdays.append(random.randint(1, 365))
    return birthdays


def duplicate_birthdays(birthdays):
    """
    This function uses a len to see if the birthdays are duplicated
    :param birthdays: This calls the list of birthdays
    :return: It returns if true or false depending on if there are duplicate birthdays or not
    """
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
