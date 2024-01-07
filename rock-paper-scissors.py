import random

def rock_paper_scissors():
    choices = ["rock", "paper", "scissors"]
    user_score = 0
    computer_score = 0

    while user_score < 3 and computer_score < 3:
        computer_choice = random.choice(choices)
        user_choice = input("Make your move (rock, paper, scissors): ")

        if user_choice == computer_choice:
            print("Tie!")
        elif user_choice == "rock" and computer_choice == "scissors":
            print("You beat me.")
            user_score += 1
        elif user_choice == "paper" and computer_choice == "rock":
            print("You beat me.")
            user_score += 1
        elif user_choice == "scissors" and computer_choice == "paper":
            print("You beat me.")
            user_score += 1
        else:
            print("You lost!")
            computer_score += 1

    if user_score > computer_score:
        print("Congratulations! You won the game!")
    else:
        print("You lost! I knew you would.")

rock_paper_scissors()
