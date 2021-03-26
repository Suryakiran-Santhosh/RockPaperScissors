"""
Rock, Paper, and Scissors Game
By: Suryakiran Santhosh
"""


import utils


def main() -> None:
    user_input = (utils.welcome()).lower().lstrip().rstrip()  # Display Menu

    while user_input != "q":
        if user_input == "a":  # Single Player against Computer
            player1_name = utils.get_player_name(num=1).lower().lstrip().rstrip()
            player1_choice = utils.get_player_choice(name=player1_name)

            # input validation
            while player1_choice.lower() not in ["r", "s", "p"]:
                player1_choice = utils.get_player_choice(name=player1_name)

            computer_choice = utils.get_computer_choice()

            player1 = tuple((player1_name, player1_choice))
            computer = tuple(("Computer", computer_choice))

            print(utils.print_choices(player1=player1, player2=computer))

            winner = utils.check_winner(player1=player1, player2=computer).lower()

            if winner == "tie":
                print(utils.print_winner(winner=winner, tie=True))
            else:
                print(utils.print_winner(winner=winner, tie=False))

        elif user_input == "b":  # Two Player
            player1_name = utils.get_player_name(num=1).lower().lstrip().rstrip()
            player2_name = utils.get_player_name(num=2)

            player1_choice = utils.get_player_choice(name=player1_name)
            # input validation
            while player1_choice.lower() not in ["r", "s", "p"]:
                player1_choice = utils.get_player_choice(name=player1_name)

            player2_choice = utils.get_player_choice(name=player2_name)
            # input validation
            while player1_choice.lower() not in ["r", "s", "p"]:
                player2_choice = utils.get_player_choice(name=player2_name)

            player1 = (player1_name, player1_choice)
            player2 = (player2_name, player2_choice)

            winner = utils.check_winner(player1=player1, player2=player2)

            if winner.lower() == "tie":
                print(utils.print_winner(winner=winner, tie=True))
            else:
                print(utils.print_winner(winner=winner, tie=False))
        elif user_input == "q":  # Quit
            print("THANK YOU FOR PLAYING, GOODBYE!")
            return
        else:
            print("IMPROPER INPUT! Please choose one of the options in menu.")

        user_input = (utils.welcome()).lower().lstrip().rstrip()  # Display Menu

    if user_input == "q":
        print("THANK YOU FOR PLAYING, GOODBYE!")
        return


if __name__ == "__main__":
    main()
