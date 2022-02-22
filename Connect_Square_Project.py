import numpy as np
import pandas as pd
import pygame
import sys

ROW_COUNT = 4 #Global Variable to set board values (rows)
COLUMN_COUNT = 4 #Global Variable to set board values (columns)

def create_board():
    board = np.zeros((ROW_COUNT,COLUMN_COUNT))
    return board

def add_coin(board, row, col, coin):
    board[row][col] = coin

def is_valid_location(board, col): #Looks at top row to see if empty. If not empty, will not allow further placement of coin.
    return board[ROW_COUNT-1][col] == 0

def get_next_open_row(board, col): #Identifies which rows have been filled, so coin will not stack ontop of each other.
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r

def print_board(board): #Python has 0 defined as the top left corner, needed coins to be placed beginning bottom left. Flipped the 'board'.
    print(np.flip(board, 0))

def is_winner(board, coin):
    # Check horizontal locations for win
    for c in range(COLUMN_COUNT-1):
        for r in range(ROW_COUNT-1):
            if board[r][c] == coin and board[r][c+1] == coin and board[r+1][c] == coin and board[r+1][c+1] == coin:
               return True 
    # Check square for win

def draw_board(board):
    pass

board = create_board()
print_board(board)
game_over = False #game over needs to be false so the game can play.
turn = 0 #Beginning at turn 0

while not game_over:
            # Ask for Player 1 Input
        if turn == 0:
            col = int(input("Player 1 Make your Selection (0-3):"))

            if is_valid_location(board, col):
                row = get_next_open_row(board, col)
                add_coin(board, row, col, 1)

                if is_winner(board, 1):
                    print("Player 1 Wins")
                    game_over = True

            # Ask for Player 2 Input
        else:
            col = int(input("Player 2 Make your Selection (0-3):"))

            if is_valid_location(board, col):
                row = get_next_open_row(board, col)
                add_coin(board, row, col, 2)

                if is_winner(board, 2):
                    print("Player 2 Wins")
                    game_over = True

        print_board(board)

        turn += 1
        turn = turn % 2