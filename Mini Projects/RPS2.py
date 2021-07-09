from random import choice

""" Rock paper scissors extended to use CP """

print("Rock Paper Scissors Game\n\n")

rock_paper_scissors = ["rock", "paper", "scissors"]

p1_choice = input("Enter Player 1's choice: ")

comp_choice = choice(rock_paper_scissors)

print("The computer plays " + comp_choice + "\n")

# Rock paper scissors
# (r, p), (p, r), (r, s), (s, r), (s, p) (p, s)

# Case for rock and paper - paper rock
if (p1_choice == "rock" and comp_choice == "paper") or (p1_choice == "paper" and comp_choice == "rock"):
    if p1_choice == "paper":
        print("Player 1 wins!")
    else:
        print("Comp wins!")
# Case for rock and scissors - scissors rock
elif (p1_choice == "rock" and comp_choice == "scissors") or (p1_choice == "scissors" and comp_choice == "rock"):
    if p1_choice == "rock":
        print("Player 1 wins!")
    else:
        print("Comp wins!")
# Case for scissors and paper - paper scissors
elif (p1_choice == "paper" and comp_choice == "scissors") or (p1_choice == "scissors" and comp_choice == "paper"):
    if p1_choice == "scissors":
        print("Player 1 wins!")
    else:
        print("Comp wins!")
elif p1_choice == comp_choice:
    print("Its a tie!!")
else:
    print("Please check input values")