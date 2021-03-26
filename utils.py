"""
Rock, Paper, and Scissors Game
By: Suryakiran Santhosh

Utility Functions
"""


import random


# Welcome Message
def welcome():
    return input(
        "\nWELCOME TO CONSOLE ROCK, PAPER, & SCISSORS GAME\n" +
        "===============================================\n" +
        "A.) SINGLE PLAYER AGAINST COMPUTER\n" +
        "B.) TWO PLAYER\n" +
        "Q.) QUIT\n" +
        "Please select one option from options A, B, and Q:\n"
    )


def get_computer_choice():
    return random.choice(["r", "p", "s"])


def get_player_choice(name: str):
    return input(
        "\n" +
        f"{name.title()} please make a choice: \n" +
        "R.) Rock \n" +
        "P.) Paper \n" +
        "S.) Scissors \n" +
        "Please select one option from R, P, and S:"
    )


def get_player_name(num: int):
    return input(f"\nPlease enter player{num}'s name: ")


def check_winner(player1: tuple, player2: tuple):
    if (player1[1].lower() == player2[1].lower()):
        return "TIE"
    elif (player1[1].lower() == "r" and player2[1].lower() == "s") \
            or (player1[1].lower() == "p" and player2[1].lower() == "r") \
            or (player1[1].lower() == "s" and player2[1].lower() == "p"):
        return player1[0]
    elif (player2[1].lower() == "r" and player1[1].lower() == "s") \
            or (player2[1].lower() == "p" and player1[1].lower() == "r") \
            or (player2[1].lower() == "s" and player1[1].lower() == "p"):
        return player2[0]


def print_winner(winner: tuple, tie: bool):
    if tie == True:
        return ("\nTIE GAME!!")
    else:
        return(f"\nCONGRATULATIONS! {winner.title()} IS THE WINNER!!!!")


def print_choices(player1: tuple, player2: tuple):
    string = f"\n{player1[0].title()} chose {__transcriber(player1[1]).title()} \n" +\
        f"{player2[0].title()} chose {__transcriber(player2[1]).title()}"
    return string


def __transcriber(choice: str):
    if choice.lower() == "r":
        return "Rock"
    elif choice.lower() == "p":
        return "Paper"
    elif choice.lower() == "s":
        return "Scissors"
