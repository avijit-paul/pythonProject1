from IPython.display import clear_output
import random

def game_board(board):
    clear_output()
    board[0]
    print(board[7]+'|'+board[8]+'|'+board[9])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[1]+'|'+board[2]+'|'+board[3])

test_board = ['','X','O','X','O','X','O','X','O','X']


def player_input():
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input('Player 1, choose X or O: ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

player_input()

def place_marker(board, marker, position):
    board[position] = marker

p = place_marker(test_board, '$', 8)
game_board(test_board)

def win_check(board, mark):
        # check rows and columns and diagonal match
    return board[7] == mark and board[8] == mark and board[9] == mark or \
    board[4] == mark and board[5] == mark and board[6] == mark or \
    board[1] == mark and board[2] == mark and board[0] == mark or \
    board[1] == board[4] == board[7] == mark or \
    board[2] == board[5] == board[8] == mark or \
    board[3] == board[6] == board[9] == mark or \
    board[1] == board[5] == board[9] == mark or \
    board[3] == board[5] == board[7] == mark


def select_first_player():
    flip = random.randint(0,1)
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'

def space_checked(board,position):
    return board[position] == ' '

def full_board_check(board):
    for i in range(1,10):
        if space_checked(board,i):
            return False

def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_checked(board,position):
        position = int(input('Choose a position: (1-9)'))
    return position

def replay():
    choice = input("Play again? 'Y' or 'N'")
 
