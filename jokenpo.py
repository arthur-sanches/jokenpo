import sys
from random import randint


class Jokenpo:

    def __init__(self):
        self.game_active = True
        self.weapons = ("Rock", "Paper", "Scissors")

    def run_game(self):
        while self.game_active:
            print("Press 1 to play indefinitely.")
            print("Press 2 to play best of 3.")
            print("Press 3 to play best of 5.")
            print("Press Q to quit at any time.")

            choice = input()
            self._check_quit(choice)

            self._reset_game()

            if choice == "1":
                self.infinite_game()
            elif choice == "2":
                self.best_three_game()
            elif choice == "3":
                self.best_five_game()

    def infinite_game(self):
        while True:
            self._single_game()

    def best_three_game(self):
        self._limited_game(3)

    def best_five_game(self):
        self._limited_game(5)

    def _single_game(self):
        user_key_press = input(
            "Choose your weapon: (1)Rock (2)Paper (3)Scissors: ")
        self._check_quit(user_key_press)

        try:
            user_choice = int(user_key_press) - 1
            computer_choice = randint(0, 2)
            result = user_choice - computer_choice

            if (result == 0):
                self._chosen_weapons(user_choice, computer_choice)
                print("\nIt's a draw!\n")
            elif (result == 1) or (result == -2):
                self._chosen_weapons(user_choice, computer_choice)
                print("\nYou won!\n")
                self.user_score += 1
            elif (result == -1) or (result == 2):
                self._chosen_weapons(user_choice, computer_choice)
                print("\nThe computer won :(\n")
                self.computer_score += 1
        except:
            print(f"'{user_key_press}' is not a valid choice.")
        print(
            f"The present score is User: [{self.user_score}] and Computer: [{self.computer_score}]")

    def _limited_game(self, max_matches):
        wins_needed = (max_matches//2) + 1
        while (self.user_score < wins_needed and self.computer_score < wins_needed):
            self._single_game()
        self._game_result_msg(wins_needed)

    def _game_result_msg(self, wins_needed):
        if self.user_score == wins_needed:
            print("\n Congratulations you won! \n")
        else:
            print("\n Sorry but the computer won :(\n")

    def _chosen_weapons(self, user_choice, computer_choice):
        print(f"\n         You chose: {self.weapons[user_choice]}")
        print(f"The computer chose: {self.weapons[computer_choice]}")

    def _reset_game(self):
        self.user_score = 0
        self.computer_score = 0

    def _check_quit(self, key_press):
        if type(key_press) == str:
            if key_press.capitalize() == "Q":
                sys.exit()


if __name__ == '__main__':
    # Make a game instance and run the game.
    jk = Jokenpo()
    jk.run_game()
