from random import randint

""" Simple CP guessing game - user attempts to guess number stored in memory until the number matches"""

# code can be completed in a single while loop that runs forever
# In the while loop, after the exit case has been reached, we can ask to play again
# New number is generated if the case is yes
# The loop continues to let te user keep guessing the number
# 94 in Python bootcamp
user_cmd = None

while user_cmd != 'n':

    cp_choice = randint(1, 10)
    print(".. Computer has chosen a number between 1 and 10")

    while True:
        user_in = input("Guess the number that the computer chose - between 1 and 10: ")

        if int(user_in) > cp_choice:
            print("Too high! Try again")
        elif int(user_in) < cp_choice:
            print("Too low! Try again ")
        else:
            break

    print("You guessed it! You won!")

    user_cmd = input("Do you want to keep playing? (y/n) ")

print("Thanks for playing! Bye!")
