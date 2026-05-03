#  2nd GAME TRY!! stopped flappy bird bec main goal is make as many games as possibles
#  so to learn new principles and also use previously learned lesson  I AM STARTING GAME 2!!
# time - finish in 3 days fast before teen camp
#and also coding gives more joy than gaming! so now i will leave gaming and full time think about coding!
#AND ALSO USING GIT FOR FIRST TIME IN REAL GAME

# GAME SHUTDOWN DEADLINE TILL SUNDAY OF MAY so 1 whole week to properly do this complex game bec its really good knowledge

# GAME DEV STOPPED ON MAY 3 SUNDAY, I could'nt implement a lot of features that i wanted and so this again is an unfinished broken game,
# BUT i will try to complete tutorials now and I'll come back stronger with more knowledge
# BYEE PONG!!!

import pygame
from sys import exit
import random

pygame.init()
#ALL VARIABLES AND DECLARATION/CREATION OF STUFF

gameactive = True
myFONT = pygame.font.Font(None, 70)

difficulty = 'hard'
ballserve = "player"

# WINDOW
screenw = 900
screenh = 600
screen = pygame.display.set_mode((screenw,screenh))
clock = pygame.time.Clock()

# MAIN RECTANGLES
# player and enemy adjustable x positions
playX = 750
oppX = 100
playY = oppY = 250
playerheight = enemyheight = 120
playerrect = pygame.Rect(playX,playY, 50, playerheight)
enemyrect = pygame.Rect(oppX,oppY, 50, enemyheight)

playdirec = 'still'
endirec = 'still'

ballx = (screenw / 2)
bally = (screenh / 2)
ballrad = 15
ballspeed = 5
balldirec = ballspeed #or BALL SPEED, later make this based on whoever won last round should get served ball
balldirecy = 0
ballyadd = 3.5

def ball_ai():
    global ballx,bally, balldirec,balldirecy, ballrect, ballrectx, playdirec, endirec, playX, oppX, ballspeed, ballyadd, playS, oppS, screenw

    #PLAYER based bounce back

    #moving the ball towards player only when no collision
    if ballserve == 'player':
        ballx += balldirec
        bally += balldirecy

    if playerrect.colliderect(ballrect) and ballx == playX:
        # softcoded all variables instead of hard number values now so logic is also easier to understand
        # and you don't have to keep changing all variables because of one varibale change
        ballx = playerrect.left - (ballrad * 2)

        #reverse ball direction -
        # IMP - full softcoding now bec realised now that its better and bec i want to change ball speeed  
    
        if playdirec == 'up':
            #so now ball should go up diagonally
            balldirec = -(balldirec) #reversing ball x direction
            balldirecy = -(ballyadd)  # means 2 same as og
        elif playdirec == 'down':
            #so now ball should go down diagonally
            balldirec = -(balldirec) #reversing ball x direction
            balldirecy = (ballyadd)
        elif playdirec == 'still':
            #so now ball should go straight
            balldirec = -(balldirec) #reversing ball x direction

    # ENEMY based bounce back

    #enemyrect.x += 1
    if ballserve == 'enemy':
        ballx -= balldirec
        bally += balldirecy

    if enemyrect.colliderect(ballrect) and ballx == enemyrect.right:  #enemy can only hit from its front, which is right side of its rect

        #ballx = ballx #no changes req for enemy rect

        #if oppdirec == 'still':
        #    balldirec = -(balldirec)

        if endirec == 'up':
            #so now ball should go up diagonally
            balldirec = -(balldirec) #reversing ball x direction
            balldirecy = -(ballyadd)   
        elif endirec == 'down':
            #so now ball should go down diagonally
            balldirec = -(balldirec) #reversing ball x direction
            balldirecy = ballyadd   
        elif endirec == 'still':
            #so now ball should go straight
            balldirec = -(balldirec) #reversing ball x direction

    # Game screen boundary based bounce back
    # BUG HERE - ball y is vibrating like before but now on game srufce, will try with same bugfix as before
    # fixed by avoiding problem and just using a new variable, bad method tbh

    if ballrect.top < 0:  # top boundary
        balldirecy = ballspeed
    elif ballrect.bottom > screenh:
        balldirecy = -(ballspeed)   # bottom boundary

    # SCORES SYSTEM

    if ballrect.left < 0:
        playS += 1
    elif ballrect.right > screenw:
        oppS += 1
        
        
def enemyai():
    global ballx,bally, balldirec,balldirecy, ballrect, ballrectx, endirec
    #moved all enemy ball logic to ball ai bec i realised all ball logic should be there only

    # RANDOM TRY
    test = False
    if test == True:
        # 1st test using random
        choices = ['up', 'down']
        MoveF = random.choice(choices)
        if MoveF == 'up':
            enemyrect.y -= 20
            endirec = 'up'
        elif MoveF == 'down':
            enemyrect.y += 20
            endirec = 'down'

        # 2nd test
        if ballrect.y < 300:
            #move up 
            enemyrect.y -= 20
            endirec = 'up'
        elif ballrect.y > 300:
            #move down
            enemyrect.y += 20
            endirec = 'down'
    
    

    
#MAIN GAME WHILE LOOP
while gameactive:

    #varibles that need to be constnatly updated are put inside loop and they are first
    ballrectx = ballx - ballrad
    ballrecty = bally - ballrad

    ballrect = pygame.Rect(ballrectx, ballrecty, (ballrad * 2), (ballrad * 2))

    playS = 0
    oppS = 0

    #SCORES
    playerscore = myFONT.render(f'{playS}', False, 'white')
    enemyscore = myFONT.render(f'{oppS}', False, 'white')
    

    # MAIN EVENT LOOP and CONTROLS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                playerrect.y -= 20
                playdirec = 'up'
                #print(playdirec)
            elif event.key == pygame.K_DOWN:
                playerrect.y += 20
                playdirec = 'down'
                #print(playdirec)
            elif event.key == pygame.K_w:
                enemyrect.y -= 20
                endirec = 'up'
            elif event.key == pygame.K_s:
                enemyrect.y += 20
                endirec = 'down'
            elif event.key == pygame.K_ESCAPE:
                pygame.quit
                exit()
        if event.type == pygame.MOUSEMOTION:
            mousepos = event.pos
            #print(mousepos)  # only for debug or finding correct placement, not really needed that much


    # black background and clears screen bec no bg now
    screen.fill((0, 0, 0))  

    #animations
    ball_ai()
    enemyai()

    if gameactive == True:
        #draw all entities

        # SCORES
        screen.blit(playerscore, (300, 100))
        screen.blit(enemyscore, (600, 100))

        # BALL
        pygame.draw.rect(screen, 'white', ballrect) #hitbox rect of ball
        pygame.draw.circle(screen, 'yellow', (ballx, bally), ballrad) #main ball

        # BOARDS
        pygame.draw.rect(screen, 'orange', playerrect) # player board
        pygame.draw.rect(screen, 'orange', enemyrect) # opp board
        #print("balldirec x:", balldirec)
        #print("balldirec y:", balldirecy)
        

    pygame.display.update()
    clock.tick(60)