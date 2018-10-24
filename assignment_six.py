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
        return True
    else:
       return False




def main():
    birthday_check = birthday_lists()
    duplicate_birthdays(birthday_check)
    birthday_match = 0
    if duplicate_birthdays == True:
        birthday_match += 1
    elif duplicate_birthdays == False:
        print("There were no matches")
    print(birthday_match)



main()