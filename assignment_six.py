import random


def number_simulation():
    user_simulation = (input("How many simulations do you wish to run?"))
    return user_simulation

def birthday_lists():
    birthdays = []
    for i in range(23):
         birthdays.append(random.randint(1, 365))
    print(birthdays)
    return birthdays


def duplicate_birthdays(birthdays):

    check_birthdays = set(birthdays)
    if len(check_birthdays) < len(birthdays):
        print("Found duplicates")
    else:
        print("no duplicates")




def main():
    birthday_check = birthday_lists()
    duplicate_birthdays(birthday_check)


main()