import random
 
intro = input("Welcome to the game! press 'Y' to continue or 'E' to exit.").upper()
 
if intro == 'Y':
    game_start = True
    while game_start:
        user_action = input("Enter a choice 'R' for Rock, 'P' for Paper or 'S' for Scissors")
        possible_choices = ["R","P","S"]
        computer_choice = random.choice(possible_choices)
        if user_action == computer_choice:
            print(f"Both players selected {user_action}. it is a tie!")
            game_start = False
            break
        elif user_action == 'R':
            if computer_choice == 'S':
                print("Rock smashes scissors! you win!")
            else:
                print("paper covers rock, you lose!")
            game_start = False
            break
        elif user_action == 'P':
            if computer_choice == 'R':
                print("paper covers rock! you win!")
            else:
                print("scissors cuts paper! you lose.")
            game_start = False
            break
        elif user_action == 'S':
            if computer_choice == 'P':
                print("Scissors cuts paper! you win!")
            else:
                print("Rock smashes scissors! you lose.")
            game_start = False
            break
elif intro == 'E':
    print("Thank you for playing")
else:
    print("you picked the wrong option, please try again")
 