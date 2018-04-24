from random import randint
from time import sleep

game_options = ['rock', 'paper', 'scissors']

def game_choice():
    game_active = True
    while game_active:
        rand_answers = randint(0, 2)
        human_answer = input("Which do you pick: rock, paper, or scissors \n")
        print("You've chosen: " + human_answer)
        print("Now the computer will select a random option...")
        sleep(1)
        computer_answer = (game_options[rand_answers])
        print("The computer has chosen: " + computer_answer)

        if human_answer == 'rock':
            if computer_answer == 'paper':
                winner = 'computerwin'
            if computer_answer == 'rock':
                winner = 'tiewin'
            if computer_answer == 'scissors':
                winner = 'humanwin'
            score_board(winner)

        if human_answer == 'paper':
            if computer_answer == 'paper':
                winner = 'tiewin'
            if computer_answer == 'rock':
                winner = 'humanwin'
            if computer_answer == 'scissors':
                winner = 'computerwin'
            score_board(winner)

        if human_answer == 'scissors':
            if computer_answer == 'paper':
                winner = 'humanwin'
            if computer_answer == 'rock':
                winner = 'computerwin'
            if computer_answer == 'scissors':
                winner = 'tiewin'
            score_board(winner)

        user_input = input("Would you like to play again (y/n)?\n")
        user_input = user_input.lower()
        if user_input == 'n':
            game_active = False

def score_board(winner):
    if winner == 'humanwin':
        print("You win!")
    if winner == 'computerwin':
        print("You lose.")
    if winner == 'tiewin':
        print("It's a draw!")

print("Welcome to Rock, Paper, Scissors!")

game_choice()

