print("Rock Paper Scissors Game\n\n")

p1_choice = input("Enter Player 1's choice: ")

for _ in range(30):
    print("--anti cheat--")

# print("-anti cheat" * 30)

p2_choice = input("Enter Player 2's choice: ")

# Rock paper scissors
# (r, p), (p, r), (r, s), (s, r), (s, p) (p, s)

# Case for rock and paper - paper rock
if (p1_choice == "rock" and p2_choice == "paper") or (p1_choice == "paper" and p2_choice == "rock"):
    if p1_choice == "paper":
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")
# Case for rock and scissors - scissors rock
elif (p1_choice == "rock" and p2_choice == "scissors") or (p1_choice == "scissors" and p2_choice == "rock"):
    if p1_choice == "rock":
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")
# Case for scissors and paper - paper scissors
elif (p1_choice == "paper" and p2_choice == "scissors") or (p1_choice == "scissors" and p2_choice == "paper"):
    if p1_choice == "scissors":
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")
elif p1_choice == p2_choice:
    print("Its a tie!!")
else:
    print("Please check input values")