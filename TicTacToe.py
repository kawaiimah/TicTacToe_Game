# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 23:14:43 2020

Play Tic Tac Toe against the Computer

"""

import random
import sys

def displayboard(pegs):

    print('\n--- Tic Tac Toe ---\n\n')

    board = ['','','','','']
    board[0] = '  {}┃{}┃{}     7┃8┃9'.format(pegs[7],pegs[8],pegs[9])
    board[1] = '  ━╋━╋━     ━╋━╋━'
    board[2] = '  {}┃{}┃{}     4┃5┃6'.format(pegs[4],pegs[5],pegs[6])
    board[3] = '  ━╋━╋━     ━╋━╋━'
    board[4] = '  {}┃{}┃{}     1┃2┃3'.format(pegs[1],pegs[2],pegs[3])
    
    for i in board:
        print(i)
    
    print('\n')

def checkwin(pegs, gamestate):
    
    # checks if lines completed,
    # returns 2 for player win, 3 for comp win,
    # then checks if tie i.e. return 4
    # otherwise return gamestate unchanged
    winlines = [(1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7)]
    for (i,j,k) in winlines:
        if pegs[i] == 'X' and pegs[j] == 'X' and pegs[k] == 'X':
            return 2
        if pegs[i] == 'O' and pegs[j] == 'O' and pegs[k] == 'O':
            return 3
    count = 0
    for i in pegs:
        if i != ' ':
            count += 1
    if count == 9:
        return 4
    return gamestate

def decide(pegs):
    
    winlines = [(1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7)]
    # Check if immediate win is possible
    for (i,j,k) in winlines:
        if pegs[i] == ' ' and pegs[j] == 'O' and pegs[k] == 'O':
            return i
        elif pegs[i] == 'O' and pegs[j] == ' ' and pegs[k] == 'O':
            return j
        elif pegs[i] == 'O' and pegs[j] == 'O' and pegs[k] == ' ':
            return k
    
    # Check if blocking is necessary
    for (i,j,k) in winlines:
        if pegs[i] == ' ' and pegs[j] == 'X' and pegs[k] == 'X':
            return i
        elif pegs[i] == 'X' and pegs[j] == ' ' and pegs[k] == 'X':
            return j
        elif pegs[i] == 'X' and pegs[j] == 'X' and pegs[k] == ' ':
            return k

    # Comp always takes centre if possible,
    # Otherwise priority is corners then sides
    if pegs[5] == ' ':
        return 5
    elif pegs[1] == ' ' or pegs[3] == ' ' or pegs[7] == ' ' or pegs[9] == ' ':
        option = []
        for i in range(1,10,2):
            if pegs[i] == ' ':
                option.append(i)
        return random.choice(option)
    else:
        option = []
        for i in range(2,9,2):
            if pegs[i] == ' ':
                option.append(i)
        return random.choice(option)


def main():
    
    pegs = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    
    gamestate = 0
    # 0=player turn, 1=comp turn, 
    # 2=player win, 3=comp win, 4=tie
    
    while True:
        
        displayboard(pegs)
        gamestate = checkwin(pegs, gamestate)
        
        if gamestate == 0: # Player X turn
            
            valid = False
            while not valid:
                choice = input('Your choice (1-9, Q to quit)? ').lower()
                if choice in ['q','1','2','3','4','5','6','7','8','9']:
                    if choice == 'q':
                        sys.exit()
                    elif pegs[int(choice)] == ' ':
                        pegs[int(choice)] = 'X'
                        valid = True
                        gamestate = 1
                    else:
                        print('That square is already occupied!')
                else:
                    print('Invalid input, pls try again.')
                
        
        elif gamestate == 1: # Comp O turn
            
            pegs[decide(pegs)] = 'O'
            gamestate = 0
                                                
        else:
            
            if gamestate == 2:
                print('You win!!!\n')
            elif gamestate == 3:
                print('Computer wins!\n')
            else:
                print('It is a tie!\n')
            return


while True:
    
    main()
    if input('Play again (y/n)? ').lower() == 'n':
        sys.exit()
