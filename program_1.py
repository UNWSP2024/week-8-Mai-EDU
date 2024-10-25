# Programmer: Mai Lillie
# Date: 10/25/2024
# Program #1: Initials
# Code that returns initials from users name

def initials_generator(name_input):
    persons_initials = ""
    name = name_input.split()

    for string in name:
        print(string[0].upper(), end = "")
        print(".", end = " ")

    return persons_initials.strip()

# Person enters their name
persons_name = input('Enter the users first, middle, and last name: ')

initials = initials_generator(persons_name)

print(initials)
