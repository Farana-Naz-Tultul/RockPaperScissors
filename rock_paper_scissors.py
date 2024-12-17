import random

user_wins = 0
computer_wins = 0

options_list = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock, Paper, Scissors or Q to Quit: ")
    if user_input == "q":
        break
    if user_input not in options_list:
        continue
    random_number = random.randint(0,2)
    #Here, 0 = rock, 1 = paper, 2 = scissors, according to the numbering of the list.

    computer_picks = options_list[random_number]
    print("Computer picked", computer_picks + ".")

    if user_input == "rock" and computer_picks == "scissors":
        print("~~~You won~~~")
        user_wins +=1
    elif user_input == "paper" and computer_picks == "rock":
        print("~~~You won~~~")
        user_wins += 1
    elif user_input == "scissors" and computer_picks == "paper":
        print("~~~You won~~~")
        user_wins += 1
    else:
        print("You lost!!!")
        computer_wins +=1

print("You won", user_wins, "times!")
print("Computer won", computer_wins, "times!")
print("Thank you, Goodbye!")