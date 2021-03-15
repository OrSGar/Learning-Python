from pyfiglet import print_figlet, COLOR_CODES

user_str = input("What message do you want to print? ")
user_color = input("What color? ").upper()

print(user_color)

if user_color in COLOR_CODES:
    print_figlet(user_str, font="isometric1", colors=user_color)
else:
    print_figlet(user_str, font="isometric1", colors="MAGENTA")
