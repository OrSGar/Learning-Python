from pyfiglet import print_figlet, COLOR_CODES

""" Prints a user supplied message formatted in a figlet format """

user_str = input("What message do you want to print? ")
user_color = input("What color? ").upper()

print(user_color)

if user_color in COLOR_CODES:
    print_figlet(user_str, font="slant", colors=user_color)
else:
    print_figlet(user_str, font="slant", colors="MAGENTA")
