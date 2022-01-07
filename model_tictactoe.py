# Qizhou Fang
# qsfang
# 77491862
import os
import random
# it contains data of the board and has methods to
# check the result of a game
# the board class enables the players to create objects
# that represents a real life tic tac toe board.
# It stores information of each cell of the board,
# it allows players to play moves (update the cells)
# checks if any player wins after each move and pronounce
# tie if all the squares all filled and no one wins
# after each game, players can choose th leave or continue
# if continue, the board will be reset and a new game can be started
class Board:

    #Constructor should intiliaze the board to a blank state
    def __init__(self):
        # initialize the board attribute to a 3*3 two dimensional list
        # each of the 3 sublist contains 3 white spaces
        # a mirror board is set up to record the transpose of the board matrix
        self.board = [[' ', ' ', ' '] for i in range(3)]
        self.rev_board = [[' ', ' ', ' '] for i in range(3)]
        self.last_player = "O"

    #Should print out the board
    # print the board and fill the 9 cells with 9 elements in self.board
    def display(self):
        print(' ', end='')
        print(self.board[0][0], end='')
        print(' ', end='')
        print('|', end='')
        print(' ', end='')
        print(self.board[0][1], end='')
        print(' ', end='')
        print('|', end='')
        print(' ', end='')
        print(self.board[0][2], end='')
        print(' ')
        print('-' * 12)
        print(' ', end='')
        print(self.board[1][0], end='')
        print(' ', end='')
        print('|', end='')
        print(' ', end='')
        print(self.board[1][1], end='')
        print(' ', end='')
        print('|', end='')
        print(' ', end='')
        print(self.board[1][2], end='')
        print(' ')
        print('-' * 12)
        print(' ', end='')
        print(self.board[2][0], end='')
        print(' ', end='')
        print('|', end='')
        print(' ', end='')
        print(self.board[2][1], end='')
        print(' ', end='')
        print('|', end='')
        print(' ', end='')
        print(self.board[2][2], end='')
        print(' ')





    #Method that updates a cell on the board based off the player
    # raise Valueerror when an occupied square is played
    def update_cell(self, cell_no : str, player: str):
        # translate number 1-9 to 2 dimension list coordinate
        # if the cell is already occupied, it will not be updated
        # the mirror list is updated too

            if self.board[(cell_no - 1) // 3][(cell_no - 1) % 3] != ' ':
                raise ValueError




            else:
                num = cell_no - 1
                row = num // 3
                col = num % 3
                if player == 'X':
                    if self.board[row][col] == ' ':
                        self.board[row][col] = 'X'
                        self.rev_board[col][row] = 'X'
                elif player == 'O':
                    if self.board[row][col] == ' ':
                        self.board[row][col] = 'O'
                        self.rev_board[col][row] = 'O'









    #Checks if the game has been won
    # this method contains two cases where player is 'X' or 'O'
    # for each case, it will check if diagonals, rows or columns
    # have consecutive 3 pieces by iterating over self.board
    # and counting the pieces belongs to the player
    def is_winner(self,player: str):
        win = False
        if player == 'X':
            #check for rows
            # if 3 elements in any of the three sublists belongs
            # to the same player, we declare the player winning
            for li in self.board:
                countR = 0
                for piece in li:
                    if piece == 'X':
                        countR += 1
                        if countR == 3:
                            win = True
            #check for columns
            # the same way as check the rows, we just check the rows
            # of the transpose matrix. It's the same as check the columns
            for li in self.rev_board:
                countC = 0
                for piece in li:
                    if piece == 'X':
                        countC += 1
                        if countC == 3:
                            win = True
            #check for diagonals
            # we check if a square is in diagonal by checking if its
            # row number equals to column number or its row number
            # and column number adds to 3
            countD = 0
            for i, li in enumerate(self.board):
                for j, piece in enumerate(li):
                    if i == j and piece == 'X':
                        countD += 1
                        if countD == 3:
                            win = True
            countD = 0
            for i, li in enumerate(self.board):
                for j, piece in enumerate(li):
                    if i + j == 2 and piece == 'X':
                        countD += 1
                        if countD == 3:
                            win = True
        if player == 'O':
            #check for rows
            for li in self.board:
                countR = 0
                for piece in li:
                    if piece == 'O':
                        countR += 1
                        if countR == 3:
                            win = True
            #check for columns
            for li in self.rev_board:
                countC = 0
                for piece in li:
                    if piece == 'O':
                        countC += 1
                        if countC == 3:
                            win = True
            #check for diagonals
            countD = 0
            for i, li in enumerate(self.board):
                for j, piece in enumerate(li):
                    if i == j and piece == 'O':
                        countD += 1
                        if countD == 3:
                            win = True
            countD = 0
            for i, li in enumerate(self.board):
                for j, piece in enumerate(li):
                    if i + j == 2 and piece == 'O':
                        countD += 1
                        if countD == 3:
                            win = True
        return win
        

    #Checks if the game has been tied
    # the method check if all the cells are occupied and no player has won
    # if so, it declares the game a tie
    def is_tie(self):
        tie = False
        count = 0
        for li in self.board:
            for piece in li:
                if piece == ' ':
                    count += 1
        if count == 0 and not (self.is_winner('X') or self.is_winner('O')):
            tie = True
        return tie


    #resets the game board for another round
    # set the elements in self.board back to 3 sublists of 3 whitespaces
    def reset(self):
        self.board = [[' ', ' ', ' '] for i in range(3)]
        self.rev_board = [[' ', ' ', ' '] for i in range(3)]
        self.last_player = "O"
        pass

    #Partial AI moves (Bonus Challenge(Optional))
    # ai move select the center square if it is open, it blocks
    # diagonals, rows and columns when the human player has two
    # consecutive pieces and the third square is open
    # it choose the winning move when ai has two consecutive
    # pieces and the third square is open.
    # if neither winner move and blocking move is
    # found, it will choose a random integer over and
    # over again until a unoccupied square is chosen
    def ai_move(self, player):

        ai_move = None
        #if the centre is open choose that
        if self.board[1][1] == ' ':
            ai_move = 5
        # AI Blocks
        for i, li in enumerate(self.board):
            countR = 0
            countB = 0
            for j, piece in enumerate(li):
                if piece != player and piece != ' ':
                    countR += 1
                elif piece == ' ':
                    moveR1 = 3 * i + j + 1
                    countB += 1
            if countR == 2 and countB == 1:
                ai_move = moveR1
        for i, li in enumerate(self.rev_board):
            countC = 0
            countB = 0
            for j, piece in enumerate(li):
                if piece != player and piece != ' ':
                    countC += 1
                elif piece == ' ':
                    moveC1 = 3 * j + i + 1
                    countB += 1
            if countC == 2 and countB == 1:
                ai_move = moveC1
        countD = 0
        countB = 0
        for i, li in enumerate(self.board):
            for j, piece in enumerate(li):
                if i == j and (piece != player and piece != ' '):
                    countD += 1
                elif i == j and piece == ' ':
                    moveD1 = 3 * i + j + 1
                    countB += 1
        if countD == 2 and countB == 1:
            ai_move = moveD1
        countD = 0
        countB = 0
        for i, li in enumerate(self.board):
            for j, piece in enumerate(li):
                if i + j == 2 and (piece != player and piece != ' '):
                    countD += 1
                elif i + j == 2 and piece == ' ':
                    moveD1 = 3 * i + j + 1
                    countB += 1
        if countD == 2 and countB == 1:
            ai_move = moveD1
        #AI can win
        # row win
        for i, li in enumerate(self.board):
            countR = 0
            countB = 0
            for j, piece in enumerate(li):
                if piece == player:
                    countR += 1
                elif piece == ' ':
                    moveR = 3 * i + j + 1
                    countB += 1
            if countR == 2 and countB == 1:
                ai_move = moveR
        #col win
        for i, li in enumerate(self.rev_board):
            countC = 0
            countB = 0
            for j, piece in enumerate(li):
                if piece == player:
                    countC += 1
                elif piece == ' ':
                    moveC = 3 * j + i + 1
                    countB += 1
            if countC == 2 and countB == 1:
                ai_move = moveC
        # diagonal win
        countD = 0
        countB = 0
        for i, li in enumerate(self.board):
            for j, piece in enumerate(li):
                if i == j and piece == player:
                    countD += 1
                elif i == j and piece == ' ':
                    moveD = 3 * i + j + 1
        if countD == 2 and countB == 1:
            ai_move = moveD
        countD = 0
        countB = 0
        for i, li in enumerate(self.board):
            for j, piece in enumerate(li):
                if i + j == 2 and piece == player:
                    countD += 1
                elif i + j == 2 and piece == ' ':
                    moveD = 3 * i + j + 1
                    countB += 1
        if countD == 2 and countB == 1:
            ai_move = moveD




        #Choose Random
        rand_move = None
        if ai_move == None:
            while rand_move == None:
                rand_move1 = random.randint(1, 9)
                num = rand_move1 - 1
                row = num // 3
                col = num % 3
                if self.board[row][col] == ' ':
                    rand_move = rand_move1
            ai_move = rand_move
        return ai_move
