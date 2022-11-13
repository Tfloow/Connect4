import numpy as np
import random as rd
import ai_student
import math

import turtle
from threading import Timer

from pynput.mouse import Listener

keying = (952,800)

turtle.goto(0,0)

def on_move(x, y):
    pass


def on_click(x, y, button, pressed):
    global keying
    keying = (x,y)


def on_scroll(x, y, dx, dy):
    pass
def Transforming(A):
    return (A[0]-970)*(0.62), (590-A[1])*(0.65)

ecran = turtle.Screen()
turtle.speed(0)

def makeLine():
    base = turtle.pos()
    turtle.begin_fill()
    turtle.setheading(0)
    turtle.forward(600)
    turtle.setheading(90)
    turtle.forward(5)
    turtle.goto(base[0], base[1]+5)
    turtle.end_fill()

def makeColumn():
    base = turtle.pos()
    turtle.begin_fill()
    turtle.setheading(90)
    turtle.forward(480)
    turtle.setheading(0)
    turtle.forward(5)
    turtle.goto(base[0]+5, base[1])
    turtle.end_fill()

def Piece(line, colum, player):
    color = "blue"
    if player == 1:
        color = "red"
    turtle.color(color)
    origin = (-300, -250)
    turtle.penup()
    turtle.goto(-258+colum*86, -239+line*80)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(30)
    turtle.end_fill()

def posToRC(x,y):
    print(math.floor((x + 300)/85), math.floor((y+250)/80))
    return math.floor((x + 300)/85), math.floor((y+250)/80)

turtle.penup()
turtle.goto(-300, -250)
turtle.pendown()
makeColumn()

for f in range(7):
    turtle.penup()
    turtle.goto(-300,-250+f*80)
    turtle.pendown()
    makeLine()
    turtle.penup()
    turtle.goto(-300+(f+1)*85, -250)
    turtle.pendown()
    makeColumn()

turtle.setheading(0)


"""ecran.onclick(turtle.goto)"""

# The basic AI used for section 2 of the homework
def ai_random(arg_board, player):
    board = np.copy(arg_board)
    # Collects the moves which can be played (i.e. the nonfull columns)
    nonfull_cols = np.where(board[0] == 0)[0]
    for col in nonfull_cols:
        # Creates the attack and defense moves, to check if one is a winning move
        attack_board = np.copy(update_board(board, col, player))
        defense_board = np.copy(update_board(board, col, abs(player-3)))
        # Plays if winning move for him
        if check_win(attack_board, col, player):
            #print('Plays attack move')
            return col
        # Plays if winning move for opponent
        elif check_win(defense_board, col, abs(player-3)):
            #print('Plays defense move')
            return col
    # Otherwise, plays random
    return rd.choice(nonfull_cols)
    
def update_board(arg_board, col, player):
    board = np.copy(arg_board)
    # The arguments are the board and the last move of the last player
    for i in range(5,-1,-1):
        if board[i][col] == 0:
            board[i][col] = player
            return board
            
def print_board(board):
    # For visualisation
    for i in range(6):
        print('|', end = '')
        for j in range(7):
                if board[i][j] == 1:
                    print('🔴 ', end = '') # Change the red dot with '1' or 'x' if your terminal does not support colours
                elif board[i][j] == 2:
                    print('🔵 ', end = '') # Change the blue dot with '2' or 'o' if your terminal does not support colours
                else:
                    print('   ', end = '')
        print('|')
    print('')
    
def check_win(board, col, player):
    # This function checks if the player won with his last move.
    # The arguments are the board and the last move of the last player.
    # First, we locate the row of this last move.
    row = 6
    for i in range(6):
        if board[i][col] == player:
            row = i
            break
    # Check left
    if col > 2:
        if board[row][col-1] == player:
            if board[row][col-2] == player:
                if board[row][col-3] == player:
                    return True
    # Check 2 lefts and 1 right
    if col > 1 and col < 6:
        if board[row][col-1] == player:
            if board[row][col-2] == player:
                if board[row][col+1] == player:
                    return True
    # Check 1 left and 2 rights
    if col > 0 and col < 5:
        if board[row][col-1] == player:
            if board[row][col+1] == player:
                if board[row][col+2] == player:
                    return True
    # Check right
    if col < 4:
        if board[row][col+1] == player:
            if board[row][col+2] == player:
                if board[row][col+3] == player:
                    return True
    # Check up
    if row > 2:
        if board[row-1][col] == player:
            if board[row-2][col] == player:
                if board[row-3][col] == player:
                    return True
    # Check 2 ups and 1 down
    if row > 1 and row < 5:
        if board[row-1][col] == player:
            if board[row-2][col] == player:
                if board[row+1][col] == player:
                    return True
    # Check 1 up and 2 downs
    if row > 0 and row < 4:
        if board[row-1][col] == player:
            if board[row+1][col] == player:
                if board[row+2][col] == player:
                    return True
    # Check down
    if row < 3:
        if board[row+1][col] == player:
            if board[row+2][col] == player:
                if board[row+3][col] == player:
                    return True
    # Check NW (North West)
    if col > 2 and row > 2:
        if board[row-1][col-1] == player:
            if board[row-2][col-2] == player:
                if board[row-3][col-3] == player:
                    return True
    # Check 2 NW and 1 SE
    if col > 1 and col < 6 and row > 1 and row < 5:
        if board[row-1][col-1] == player:
            if board[row-2][col-2] == player:
                if board[row+1][col+1] == player:
                    return True
    # Check 1 NW and 2 SE
    if col > 0 and col < 5 and row > 0 and row < 4:
        if board[row-1][col-1] == player:
            if board[row+1][col+1] == player:
                if board[row+2][col+2] == player:
                    return True
    # Check SE (South East)
    if col < 4 and row < 3:
        if board[row+1][col+1] == player:
            if board[row+2][col+2] == player:
                if board[row+3][col+3] == player:
                    return True
    # Check NE
    if col < 4 and row > 2:
        if board[row-1][col+1] == player:
            if board[row-2][col+2] == player:
                if board[row-3][col+3] == player:
                    return True
    # Check 2 NE and 1 SW
    if col > 0 and col < 5 and row > 1 and row < 5:
        if board[row-1][col+1] == player:
            if board[row-2][col+2] == player:
                if board[row+1][col-1] == player:
                    return True
    # Check 1 NE and 2 SW
    if col > 1 and col < 6 and row > 0 and row < 4:
        if board[row-1][col+1] == player:
            if board[row+1][col-1] == player:
                if board[row+2][col-2] == player:
                    return True
    # Check SW
    if col > 2 and row < 3:
        if board[row+1][col-1] == player:
            if board[row+2][col-2] == player:
                if board[row+3][col-3] == player:
                    return True
    return False

def run_game():
    # Run the game. In 21 turns, the board is full and the game is over
    the_board = np.full((6, 7), 0)
    for x in range(21):
        #print_board(the_board)
        #print('Player 🔴 turn:')
        ####################################################################################
        ### Replace the line below with your own AI for sections 3 and 4 of the homework ###
        ####################################################################################
        move1 = ai_student.ai_student(the_board, 1)[0]#ai_random(the_board, 1)
        if the_board[0][move1] != 0:
            print('ERROR: The chosen column is already full.')
        prev = the_board
        the_board = update_board(the_board, move1, 1)
        i = 0
        new = the_board-prev
        while sum(new[i]) == 0:
            i += 1
        print(5-i, move1)
        Piece(5-i, move1, 1)
        print("done")
        #print_board(the_board) # Uncomment this line for visualisation / debugging
        if check_win(the_board, move1, 1):
            print_board(the_board)
            #print('Player 🔴 won!')
            return 1
    
        #print('Player 🔵 turn:')
        ####################################################################################
        ### Replace the line below with your own AI for sections 3 and 4 of the homework ###
        ####################################################################################
        print_board(the_board)

        with Listener(on_click=on_click) as l:
            Timer(5, l.stop).start()
            l.join()
            print('5 seconds passed')
        newCoord = Transforming(keying)
        move2 = posToRC(newCoord[1], newCoord[0])
        print(f"mon move {move2}")
        # int(input("what column to play ?")) ai_random(the_board, 2) added player possibility to play

        move2 = move2[1]
        if the_board[0][move2] != 0:
            print('ERROR: The chosen column is already full.')
        prev = the_board
        the_board = update_board(the_board, move2, 2)

        i = 0
        new = the_board - prev
        print(new)
        while sum(new[i]) == 0:
            i += 1
        print(i, move2)
        Piece(5-i, move2, 2)
        #print_board(the_board)  # Uncomment this line for visualisation / debugging
        if check_win(the_board, move2, 2):
            print_board(the_board)
            #print('Player 🔵 won!')
            return 2
    #print('Draw!')

    return 0

print(run_game())
turtle.done()






