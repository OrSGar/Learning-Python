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

rand_num = randint(1, 10)
iterations = 0

while rand_num != 5:
    rand_num = randint(1, 10)
    print(rand_num)
    iterations += 1

print(f"Took {iterations} iterations to find 5")
