import os
import time
import random

board = [" "," "," "," "," "," "," "," "," "," "]

def print_header():
    print("welcome to TIC-TAC-TOE")
def print_board():
    print("   |   |   ")
    print(" "+board[1]+" | "+board[2]+" | "+board[3]+" ")
    print("   |   |   ")
    print("---|---|---")
    print("   |   |   ")
    print(" "+board[4]+" | "+board[5]+" | "+board[6]+" ")
    print("   |   |   ")
    print("---|---|---")
    print("   |   |   ")
    print(" "+board[7]+" | "+board[8]+" | "+board[9]+" ")
    
while True:
    print_header()
    print_board()
    choice = raw_input("please chose an empty space for X.")
    choice = int(choice)
    if board[choice] == " ":    
        board[choice] = 'X'
    else:
        print("you cannot enter in this filed")
        time.sleep(1)

    if (board[1] == 'X' and board[2] == 'X' and board[3] == 'X') or \
        (board[4] == 'X' and board[5] == 'X' and board[6] == 'X') or \
        (board[7] == 'X' and board[8] == 'X' and board[9] == 'X') or \
        (board[1] == 'X' and board[4] == 'X' and board[7] == 'X') or \
        (board[2] == 'X' and board[5] == 'X' and board[8] == 'X') or \
        (board[1] == 'X' and board[5] == 'X' and board[9] == 'X') or \
        (board[3] == 'X' and board[6] == 'X' and board[9] == 'X') or \
        (board[3] == 'X' and board[5] == 'X' and board[7] == 'X'):
        print_header()
        print_board()
        print("X WINS!!!")
        break

    print_header()
    print_board()

    isfull = True
    for index in range(1, 10):
        if board[index] == " ":
            isfull = False
            break
   
    if isfull == True:
        print("Tie!")
        break

    choice = raw_input("please chose an empty space for O.")
    choice = int(choice)
    if board[choice] == " ":    
        board[choice] = 'O'
    else:
        print("you cannot enter in this filed")
        time.sleep(1)

    if (board[1] == 'O' and board[2] == 'O' and board[3] == 'O') or \
        (board[4] == 'O' and board[5] == 'O' and board[6] == 'O') or \
        (board[7] == 'O' and board[8] == 'O' and board[9] == 'O') or \
        (board[1] == 'O' and board[4] == 'O' and board[7] == 'O') or \
        (board[2] == 'O' and board[5] == 'O' and board[8] == 'O') or \
        (board[1] == 'O' and board[5] == 'O' and board[9] == 'O') or \
        (board[3] == 'O' and board[6] == 'O' and board[9] == 'O') or \
        (board[3] == 'O' and board[5] == 'O' and board[7] == 'O'):
        print_header()
        print_board()
        print("O WINS!!!")
        break
    isfull = True
    for index in range(1, 10):
        if board[index] == " ":
            isfull = False
            break
   
    if isfull == True:
        print("Tie!")
        break
