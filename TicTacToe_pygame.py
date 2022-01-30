# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 23:14:43 2020

Play Tic Tac Toe against the Computer

"""

import random
import sys
import pygame
pygame.init()

board = pygame.display.set_mode((240, 280))
pygame.display.set_caption('TicTacToe')

peg_tiles = []
peg_tiles.append('')
for i in range(9):
    x,y = i % 3, i // 3
    peg_tiles.append(pygame.Rect(2+x*80,2+y*80,76,76))

white = (255,255,255)
black = (0,0,0)
grey = (200,200,200)
green = (0,150,0)

tile_font = pygame.font.SysFont('arial', 50)
stats_font = pygame.font.SysFont('arial', 18)


def displayboard(pegs,mouseover,win,loss,tie):

    board.fill(white)
    
    for i in range(1,10):
        pygame.draw.rect(board, black, peg_tiles[i], 3)
        
        if pegs[i] != ' ':
            char = tile_font.render(pegs[i],1,black)
            char_tile = char.get_rect()
            char_tile.center = peg_tiles[i].center
            board.blit(char, char_tile)
        
        if i == mouseover:
            char = tile_font.render('X',1,grey)
            char_tile = char.get_rect()
            char_tile.center = peg_tiles[i].center
            board.blit(char, char_tile)
    
    stats = f'W:{win}     L:{loss}     T:{tie}'
    stats_char = stats_font.render(stats,1,grey)
    stats_tile = stats_char.get_rect()
    stats_tile.center = (125, 260)
    board.blit(stats_char, stats_tile)
    
    pygame.display.update()
    

def checkwin(pegs):
    
    # checks if lines completed,
    # returns 2 for player win, 3 for comp win,
    # then checks if tie i.e. return 4
    # otherwise return gamestate based on whose turn it is
    # 0 for player, 1 for comp
    winlines = [(1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7)]
    for (i,j,k) in winlines:
        if pegs[i] == 'X' and pegs[j] == 'X' and pegs[k] == 'X':
            return 2
        if pegs[i] == 'O' and pegs[j] == 'O' and pegs[k] == 'O':
            return 3
    count = 0
    for p in pegs:
        if p == ' ':
            count += 1
    if count == 0:
        return 4
    elif count in [2,4,6,8]:
        return 1
    else:
        return 0

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


def main(win,loss,tie):
    
    pegs = ['',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    mouseover = 0
    
    while True:
        
        pygame.time.Clock().tick(60)
        displayboard(pegs,mouseover,win,loss,tie)
        gamestate = checkwin(pegs)
        
        if gamestate == 0: # Player X turn
            # check mouseover
            mouseover = 0
            x,y = pygame.mouse.get_pos()
            if x>2 and x<238 and y>2 and y<238:
                i = x//80 + 3*(y//80) + 1
                if pegs[i] == ' ':
                    mouseover = i
            # check events (quit and mousedown)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and mouseover != 0:
                    pegs[mouseover] = 'X'
                    mouseover = 0
                    
        if gamestate == 1: # Comp O turn
            pegs[decide(pegs)] = 'O'
            
        elif gamestate > 1: # Game completed
            if gamestate == 2: # Player win
                msg = 'YOU WIN!'
                win += 1
            elif gamestate == 3: # Computer win
                msg = 'Sorry!'
                loss += 1
            else:
                msg = 'Tie!'
                tie += 1
            for _ in range(3):
                msg += '.'
                msg_char = tile_font.render(msg,1,green)
                msg_tile = msg_char.get_rect()
                msg_tile.center = (120, 120)
                pygame.draw.rect(board,white,msg_tile)
                board.blit(msg_char, msg_tile)
                pygame.display.update()
                pygame.time.delay(1000)
            
            main(win,loss,tie)


if __name__ == "__main__":
    main(0,0,0)
