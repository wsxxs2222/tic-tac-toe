# Qizhou Fang
# qsfang
# 77491862
# this module contains event handlers
import model_tictactoe
board = model_tictactoe.Board()
from tkinter import messagebox
# pop up a window to notice error when a occupied square is clicked
def error_pop():
    messagebox.showinfo("Tic-Tac-Toe", "Button already clicked")
    # fixme
    pass

# pop up a window to notice player if someone wins the game
def win_pop():
    if winner == "X":
        messagebox.showinfo("Tic-Tac-Toe", "Player X has won")
    elif winner == "O":
        messagebox.showinfo("Tic-Tac-Toe", "Player O has won")
    # fixme
    pass

#pop up a window to notice player if the game is drawn
def tie_pop():
    messagebox.showinfo("Tic=Tac-Toe","Game has been tie")

# this is called whenever any of the nine bottons representing the
# squares on the board is clicked. It calls update_board, is_tie and is_winner in
# model module. If error happens or game concludes,
# it calls methods defined earlier to pop up windows,
# When a move is made, it changes the text of buttons in the window
# as a game concludes, it also update the header
def move(value, btn, lbl_1, lbl_2, lbl_3,\
         btn_list):
    global winner
    if board.last_player == 'X':
        try:
            board.update_cell(value, 'O')
        except ValueError:
            error_pop()
            pass
        else:
            board.last_player = "O"
            btn["text"] = "O"
            if board.is_winner("O"):

                winner = "O"

                board.reset()
                text_reset(btn_list)
                update_1(lbl_1)
                update_3(lbl_3)
                win_pop()
            elif board.is_tie():
                board.reset()
                text_reset(btn_list)
                update_1(lbl_1)
                tie_pop()
    elif board.last_player == 'O':
        try:
            board.update_cell(value, 'X')
        except ValueError:
            error_pop()
            pass
        else:
            board.last_player = "X"
            btn["text"] = "X"
            if board.is_winner("X"):

                winner = "X"

                board.reset()
                text_reset(btn_list)
                update_1(lbl_1)
                update_2(lbl_2)
                win_pop()
            elif board.is_tie():
                board.reset()
                text_reset(btn_list)
                update_1(lbl_1)
                tie_pop()

# update row one of header to reflect number of games played
# called when a game is done
def update_1(lbl_1):
    li = lbl_1["text"].split()
    li[-1] = str(int(li[-1]) + 1)
    lbl_1["text"] = " ".join(li)

# update row two of header to reflect number of games win by X
# called when a game is done and X is winner
def update_2(lbl_2):
    li = lbl_2["text"].split()
    li[-1] = str(int(li[-1]) + 1)
    lbl_2["text"] = " ".join(li)

# update row three of header to reflect number of games win by O
# called when a game is done and O is winner
def update_3(lbl_3):
    li = lbl_3["text"].split()
    li[-1] = str(int(li[-1]) + 1)
    lbl_3["text"] = " ".join(li)

# reset all the text of the 9 buttons
# called when a game is done or new game button is clicked
def text_reset(btn_list):
    btn_list[0]["text"] = "-"
    btn_list[1]["text"] = "-"
    btn_list[2]["text"] = "-"
    btn_list[3]["text"] = "-"
    btn_list[4]["text"] = "-"
    btn_list[5]["text"] = "-"
    btn_list[6]["text"] = "-"
    btn_list[7]["text"] = "-"
    btn_list[8]["text"] = "-"

# reset board and text when called as the new game button is clicked
def new_game(btn_list):
    board.reset()
    text_reset(btn_list)
