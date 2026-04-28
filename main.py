#  2nd GAME TRY!! stopped flappy bird bec main goal is make as many games as possibles
#  so to learn new principles and also use previously learned lesson  I AM STARTING GAME 2!!
# time - finish in 3 days fast before teen camp
#and also coding gives more joy than gaming! so now i will leave gaming and full time think about coding!
#AND ALSO USING GIT FOR FIRST TIME IN REAL GAME

# GAME SHUTDOWN DEADLINE TILL SUNDAY OF MAY so 1 whole week to properly do this complex game bec its really good knowledge

import pygame
from sys import exit

#ALL VARIABLES AND DECLARATION/CREATION OF STUFF

gameactive = True
screen = pygame.display.set_mode((600,600))
clock = pygame.time.Clock()

playerrect = pygame.Rect(500,200, 50, 150)
enemyrect = pygame.Rect(50,200, 50, 150)

ballx = 300
bally = 300
ballrad = 15
balldirec = 2 #or ball speed


#BUG HERE
def ball_ai():
    global ballx, balldirec, ballrect, ballrectx

    ballx += balldirec

    #if playerrect.collidepoint((ballx, bally)):
    #    balldirec = -(balldirec)

    if playerrect.colliderect(ballrect):
        # BUGFIX - I made it 470 bec ball diameter is 30 and player x is 500, 
        # so to avoid vibrating glitch -
        # whenever collision happens I instantly remove ball from player paddle so it doesnt vibrate and moves normally
        ballx = 470

        #reverse ball direction -
        balldirec = -(balldirec)
        #print('collision')
        #print(balldirec)
    


def enemyai():
    pass

#MAIN GAME WHILE LOOP
while gameactive:

    #varibles that need to be constnatly updated are put inside loop and they are first
    ballrectx = ballx - ballrad
    ballrecty = bally - ballrad

    ballrect = pygame.Rect(ballrectx, ballrecty, (ballrad * 2), (ballrad * 2))
    

    #MAIN EVENT LOOP
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                playerrect.y -= 20
            elif event.key == pygame.K_DOWN:
                playerrect.y += 20

    # black background and clears screen bec no bg now
    screen.fill((0, 0, 0))  

    #animations
    ball_ai()
    


    if gameactive == True:
        #draw all entities

        pygame.draw.rect(screen, 'orange', playerrect)
        pygame.draw.rect(screen, 'orange', enemyrect)

        pygame.draw.rect(screen, 'white', ballrect) #hitbox rect of ball
        pygame.draw.circle(screen, 'yellow', (ballx, bally), ballrad)
        

    pygame.display.update()
    clock.tick(60)