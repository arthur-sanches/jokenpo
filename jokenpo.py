import sys
from random import randint

game_active = True
weapons = ("Rock", "Paper", "Scissors")


def single_game():
    global user_score, computer_score
    user_key_press = input(
        "Choose your weapon: (1)Rock (2)Paper (3)Scissors: ")
    check_quit(user_key_press)

    user_choice = int(user_key_press) - 1
    computer_choice = randint(0, 2)
    result = user_choice - computer_choice

    if (result == 0):
        chosen_weapons(user_choice, computer_choice)
        print("\nIt's a draw!\n")
    elif (result == 1) or (result == -2):
        chosen_weapons(user_choice, computer_choice)
        print("\nYou won!\n")
        user_score += 1
    elif (result == -1) or (result == 2):
        chosen_weapons(user_choice, computer_choice)
        print("\nThe computer won :(\n")
        computer_score += 1
    print(
        f"The present score is User: {user_score}! and Computer: {computer_score}!")


def limited_game(max_matches):
    wins_needed = (max_matches//2) + 1
    while (user_score < wins_needed and computer_score < wins_needed):
        single_game()
    game_result_msg(wins_needed)


def infinite_game():
    while True:
        single_game()


def best_three_game():
    limited_game(3)


def best_five_game():
    limited_game(5)


def game_result_msg(wins_needed):
    if user_score == wins_needed:
        print("\n Congratulations you won! \n")
    else:
        print("\n Sorry but the computer won :(\n")


def chosen_weapons(user_choice, computer_choice):
    print(f"\n         You chose: {weapons[user_choice]}")
    print(f"The computer chose: {weapons[computer_choice]}")


def check_quit(key_press):
    if type(key_press) == str:
        if key_press.capitalize() == "Q":
            sys.exit()


while game_active:
    print("Press 1 to play indefinitely.")
    print("Press 2 to play best of 3.")
    print("Press 3 to play best of 5.")
    print("Press Q to quit at any time.")

    choice = input()
    check_quit(choice)

    user_score = 0
    computer_score = 0

    if choice == "1":
        infinite_game()
    elif choice == "2":
        best_three_game()
    elif choice == "3":
        best_five_game()
