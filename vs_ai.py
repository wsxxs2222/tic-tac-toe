# Qizhou Fang
# qsfang
# 77491862
# TicTacToe Gameplay Module
# Includes functions that would normally be included in another file at the top
# While loop is how the game play happens
import os
import model_tictactoe


# functions required to run the game
def print_header():
    print("Welcome to Tic Tac Toe\n")


# function that refreshes the screen and prints the header
def refresh_screen():
    # Clear the screen
    os.system("clear")

    # Print the Header
    print_header()

    # Show the Board
    board.display()


# Function that shows a message after the board object has determined if there is
# a winner, or it is a tie
def show_win(player: str):
    if player == "Tie":
        print("\nTie Game!\n")
    else:
        print("\nPlayer {} wins!\n".format(player))


board = model_tictactoe.Board()

# Gameplay starts from here
while True:
    refresh_screen()

    # Get X input
    x_choice = int(input("\nX) Please choose 1 - 9 >"))

    # Update board
    board.update_cell(x_choice, "X")

    # refresh screen
    refresh_screen()

    # check for x win
    if board.is_winner("X"):
        show_win("X")
        play_again = input("would you like to play again? Y/N").upper()
        if play_again == "Y":
            board.reset()
            continue
        else:
            break

    # check for Tie
    if board.is_tie():
        show_win("Tie")
        play_again = input("would you like to play again? Y/N").upper()
        if play_again == "Y":
            board.reset()
            continue
        else:
            break

    # Get O input
    o_choice = board.ai_move('O')

    # Update board
    board.update_cell(o_choice, "O")

    # check for o win
    if board.is_winner("O"):
        show_win("O")
        play_again = input("would you like to play again? Y/N").upper()
        if play_again == "Y":
            board.reset()
            continue
        else:
            break

    # check for Tie
    if board.is_tie():
        show_win("Tie")
        play_again = input("would you like to play again? Y/N").upper()
        if play_again == "Y":
            board.reset()
            continue
        else:
            break
