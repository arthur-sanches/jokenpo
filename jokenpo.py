import sys
from random import randint

from PyQt5.QtWidgets import QApplication, QDialog

from gui import *


class Jokenpo(QDialog):

    def __init__(self):
        super().__init__()
        self.game_active = True
        self.weapons = ("Rock", "Paper", "Scissors")
        self.user_score = 0
        self.computer_score = 0
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.button_rock.clicked.connect(self.rock_chosen)
        self.ui.button_paper.clicked.connect(self.paper_chosen)
        self.ui.button_scissors.clicked.connect(self.scissors_chosen)
        self.ui.button_reset.clicked.connect(self._reset_game)
        self.show()

    def rock_chosen(self):
        self._single_game(0)

    def paper_chosen(self):
        self._single_game(1)

    def scissors_chosen(self):
        self._single_game(2)

    def _single_game(self, choice):
        user_key_press = choice

        try:
            user_choice = int(user_key_press)
            computer_choice = randint(0, 2)
            result = user_choice - computer_choice
            self.ui.your_weapon_label.setText(self.weapons[user_choice])
            self.ui.foes_weapon_label.setText(self.weapons[computer_choice])

            if (result == 0):
                self._chosen_weapons(user_choice, computer_choice)
                self.ui.result_label.setText("It's a draw!")
                print("\nIt's a draw!\n")
            elif (result == 1) or (result == -2):
                self._chosen_weapons(user_choice, computer_choice)
                self.ui.result_label.setText("You won!")
                print("\nYou won!\n")
                self.user_score += 1
            elif (result == -1) or (result == 2):
                self._chosen_weapons(user_choice, computer_choice)
                self.ui.result_label.setText("The computer won :(")
                print("\nThe computer won :(\n")
                self.computer_score += 1
        except:
            print(f"'{user_key_press}' is not a valid choice.")
        finally:
            self._update_score()

    def _chosen_weapons(self, user_choice, computer_choice):
        print(f"\n         You chose: {self.weapons[user_choice]}")
        print(f"The computer chose: {self.weapons[computer_choice]}")

    def _update_score(self):
        self.ui.label_your_score.setText(str(self.user_score))
        self.ui.label_foe_score.setText(str(self.computer_score))
        print(
            f"The present score is User: [{self.user_score}] and Computer: [{self.computer_score}]")

    def _reset_game(self):
        self.user_score = 0
        self.computer_score = 0
        self._update_score()


if __name__ == '__main__':
    # Make a game instance and run the game.
    app = QApplication(sys.argv)
    jk = Jokenpo()
    jk.show()
    sys.exit(app.exec_())
