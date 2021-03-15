# # Exercise 3
# cash = 19867324678987.99
# # print(cash/5)
#
# # Exercise 4
#
# city = "Waco"
# price = 9.99
# high_score = 10
# is_having_fun = True
#
# # Exercise 5
#
# message = "No \nyou"
# # print(message)
#
# mountains = "/\\/\\/\\"
# # print(mountains)
#
# quotation = "No I said \"you\""
# # print(quotation)
#
# # Exercise 7
#
# first = "Orlando"
# last = "Garcia"
#
# formatted = f"First Name: {first}, Last Name: {last}"
# # print(formatted)
#
# # Exercise 8
# # Lucky 7
#
from random import randint, choice
#
# for _ in range(50):
#     Rchoice = randint(1, 10)
#
#     #print(choice)
#
# # Exercise 9
#
# for _ in range(50):
#     Rchoice = randint(1, 1000)
#
#     #print(choice)
#
#     #if choice % 2 == 0:
#         #print("Even")
#     #else:
#         #print("Odd")
#
#     #print("Ternary Even") if choice % 2 == 0 else print("Ternary Odd")
#     #print()
#
# # Exercise 10
#
# food = choice(['apple', 'grape', 'bacon', 'steak', 'worm', 'dirt'])
#
# #print(food)
#
# #if food == 'apple' or food == 'grape':
# #    print("Fruit")
# #elif food == 'bacon' or food == 'steak':
# #    print("Meat")
# #else:
# #    print("Yuck")
#
# #
#
# #x = True
#
# #if x:
#   #  print("If")
#  #   x = False
# # THE ELSE BRANCH WILLL ONLY RUN IF THE FIRST CONDITION IS NOT TRUE DUMMY
# # THAT IS WHY IT IS CALLED AN ELSE IF
# # IF THIS IS TRUE, THEN DO THIS
# # ELSE IF IT IS NOT TRUE, THEN CHECK THIS CASE AND THEN DO THIS
# #elif not x:
#   #  print("Else")
#  #   x = True
#
# #print(x)
# #print(not x)
#
# # Exercise 11
# # Maybe can be made to use less mem by just using the numbers to check
# # Over engineered? Could be the case
# x = randint(-100, 100)
#
# while x == 0:
#     x = randint(-100, 100)
#
# y = randint(-100, 100)
#
# while y == 0:
#     y = randint(-100, 100)
#
# x_positive = True if x > 0 else False
# y_positive = True if y > 0 else False
#
# numbers = f"x: {x}, bool: {x_positive}\ny:{y}, bool: {y_positive}\n"
#
# #print(numbers)
#
# #if x_positive and y_positive:
#  #   print("Both positive")
# #elif not x_positive and not y_positive:
#   #  print("Both negative")
# #else:
#    # print("x is positive") if x_positive else print("x is negative")
#     #print("y is positive") if y_positive else print("y is negative")
#
# # Exercise 12
#
# actually_sick = choice([True, False])
# kinda_sick = choice([True, False])
# hate_your_job = choice([True, False])
# sick_days = randint(0, 10)
#
# calling_in_sick = None
#
# values = f"AS: {actually_sick}, KS: {kinda_sick}, HYJ: {hate_your_job}, Days: {sick_days}"
# #print(values)
#
# if actually_sick and sick_days > 0:
#     calling_in_sick = True
# elif kinda_sick and hate_your_job and sick_days > 0:
#     calling_in_sick = True
# else:
#     calling_in_sick = False
#
# #print("Am I calling in sick? Yeah that's " + str(calling_in_sick))
#
# # Exercise 13
#
# # x = 0
# # # Option 1
# # # for num in range(9, 20, 2):
# # #     if num > 10:
# # #         print(f"{x} + {num} = ")
# # #         x += num
# # #         print(f"{x}\n")
# # #
# # # print(x)
# #
# # for num in range(10, 21):
# #     if num % 2 == 1:
# #         print(f"{x} + {num} = ")
# #         x += num
# #         print(f"{x}\n")
# #
# # print(x)
#
# # Exercise ##
#
# # for num in range(1, 21):
# #     if num == 4 or num == 13:
# #         print(f"{num} is UNLUCKY")
# #     elif num % 2 == 0:
# #         print(f"{num} is even")
# #     else:
# #         print(f"{num} is odd")
#
# # Exercise ##
# #
# # for times in range(1, 10):
# #     print("\U0001F974" * times)
# #
# # print()
# #
# # loops = 1
# # while loops < 10:
# #     print("\U0001F974" * loops)
# #     loops += 1
#
# # Exercise ##
#
# userIn = input("Hey how are you? ")
# while userIn != "stop copying me":
#     print(userIn)
#     userIn = input()
#
# print("UGH YOU WIN")

# Exercise ##

# rand_num = randint(1, 10)
# iterations = 0
#
# while rand_num != 5:
#     rand_num = randint(1, 10)
#     print(rand_num)
#     iterations += 1
#
# print(f"Took {iterations} iterations to find 5")

# Exercise 16
#
# people = ["Hanna","Louisa","Claudia", "Angela","Geoffrey", "aparna"]
#
# people[0] = "Hannah"
# people[-2] = "Jeffery"
# people[-1] = "Aparna"
#
# print(people)

# # Exercise 17
#
# sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]
#
# final = ""
#
# for sound in sounds:
#     final += sound.upper()
#
# print(final)

# Exercise 19
# Indexes always start at 0
#
# instructors = []
#
# instructors.append("Colt")
# instructors.append("Blue")
# instructors.append("Lisa")
#
# instructors.pop()
# instructors.pop(0)
#
# instructors.insert(0, "Done")
#
# print(instructors)

# Exercise 20

# names = ["Ellie", "Tim", "Matt"]
#
# first_letter = [name[0] for name in names]
#
# print(first_letter)
#
# numbers = [1, 2, 3, 4, 5, 6]
#
# even_numbers = [num for num in numbers if num % 2 == 0]
#
# print(even_numbers)

# Exercise 21

# nums1 = [1, 2, 3, 4]
# nums2 = [3, 4, 5, 6]
#
# # Get every num in nums1 if that num is in nums2
# intersection = [num for num in nums1 if num in nums2]
#
# print(intersection)
#
# names = ["Elie", "Tim", "Matt"]
#
# # Slice [::-1] is a quick and easy way to reverse a string
#
# names_modified = [name[::-1].lower() for name in names]
#
# print(names_modified)
#
# my_name = "Orlando"
#
# print(my_name[::-1])

# Exercise 22

# div_by_12 = [num for num in range(1, 101) if num % 12 == 0]
#
# print(div_by_12)
#
# # print([num for num in range(1, 101)])

# Exercise 23

# string = "amazing"
#
# # Need to make sure to include that conditional
# non_vowels = [char for char in string if char not in "aeiou"]
#
# print(non_vowels)

# Exercise 24

# Maybe do a better job at naming your variables
# list1 = [[num for num in range(0, 3)] for num in range(0, 3)]
#
# print(list1)

# Exercise 25

# ten_by_ten = [[inner for inner in range(0, 10)] for outer in range(0, 10)]
#
# print(ten_by_ten)
#

# Exercise 26
#
# artist = {
#     "first": "Neil",
#     "last": "Young"
# }
# # Can be accomplished with an f string
# full_name_fstring = f"{artist['first']} {artist['last']}"
#
# full_name = artist["first"] + " " + artist["last"]
#
#
# print(full_name)
# print(full_name_fstring)

# Exercise 27

# donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0, lisa=50.25, harrison=10.0)
#
# total_donations = 0
# for amounts in donations.values():
#     total_donations += amounts
#
# print(total_donations)

# Exercise 28
#
# food = choice(["cheese pizza", "quiche","morning bun","gummy bear","tea cake"])
#
# bakery_stock = {
#     "almond croissant" : 12,
#     "toffee cookie": 3,
#     "morning bun": 1,
#     "chocolate chunk cookie": 9,
#     "tea cake": 25
# }
#
# print(food)
#
# if food in bakery_stock:
#     print(f"{bakery_stock[food]} {food} left")
# else:
#     print("We dont make that")

# Exercise 29

# game_properties = ["current_score", "high_score", "number_of_lives", "items_in_inventory", "power_ups", "ammo", "enemies_on_screen", "enemy_kills", "enemy_kill_streaks", "minutes_played", "notifications", "achievements"]
#
# init_game_state = {}.fromkeys(game_properties, 0)
#
# print(init_game_state)

# Exercise 30

# inventory = {'croissant': 19, 'bagel': 4, 'muffin': 8, 'cake': 1}
#
# stock_list = inventory.copy()
#
# print(stock_list)
#
# # stock_list["cookie"] = 18
# stock_list.update({"cookie": 18})
#
# print(stock_list)
#
# stock_list.pop("cake")
#
# print(stock_list)

# Exercise 32
#
# list1 = ["CA", "NJ", "RI"]
# list2 = ["California", "New Jersey", "Rhode Island"]
#
# # Regular
# state_abbrev1 = {list1[i]: list2[i] for i in range(0, len(list1))}
#
# print(state_abbrev1)
#
# # Using Zip method
#
# state_abbrev2 = {k: v for k, v in zip(list1, list2)}
#
# # Official way
# state_abbrev2 = dict(zip(list1, list2))
#
# # Dict can be made with a tuple
# # Zip method will give us tuples from the two lists we pass in
# dict()
#
# print(state_abbrev2)

# Exercise 33

# person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
#
# person_dict = {item[0]: item[1] for item in person}
#
# print(person_dict)
#
# # Can also be done with k, v and dict
# # List of pairs can be turned into a dict using dict method
# dict(person)

# Exercise 34

# vowels = {}.fromkeys("aeiou", 0)
#
# print(vowels)

# Exercise 35

# ascii_dict = {val: chr(val) for val in range(65, 91)}
#
# print(ascii_dict)

# Exercise 36

numbers = (1, 2, 3, 4)
print(numbers)

# value =
# (1, )
value = (1, )
print(value)

values = [10, 20, 30]
print(values)

static_values = tuple(values)
print(static_values)

stuff = [1, 3, 1, 5, 2, 5, 1, 2, 5]

unique_stuff = set(stuff)
print(unique_stuff)























