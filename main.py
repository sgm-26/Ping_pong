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
difficulty = 'hard'
ballserve = "player"

# WINDOW
screen = pygame.display.set_mode((600,600))
clock = pygame.time.Clock()

# MAIN RECTANGLES
playerrect = pygame.Rect(500,200, 50, 150)
enemyrect = pygame.Rect(50,200, 50, 150)

playdirec = 'still'
endirec = 'still'

ballx = 300
bally = 300
ballrad = 15
balldirec = 2 #or ball speed, later make this based on whoever won last round should get served ball
balldirecy = 0

def ball_ai():
    global ballx,bally, balldirec,balldirecy, ballrect, ballrectx, playdirec, endirec

    #PLAYER based bounce back

    #moving the ball towards player only when no collision
    if ballserve == 'player':
        ballx += balldirec
        bally += balldirecy

    if playerrect.colliderect(ballrect) and ballx == 500:
        # BUGFIX ^ - added another condition that ballx should be 500,
        #  so only front of player board can hit ball

        # BUGFIX below- I made it 470 bec ball diameter is 30 and player x is 500, 
        # so to avoid vibrating glitch -
        # whenever collision happens I instantly remove ball from player paddle so it doesnt vibrate and moves normally
        ballx = 470

        #reverse ball direction -
    
        if playdirec == 'up':
            #so now ball should go up diagonally
            balldirec = -(balldirec) #reversing ball x direction
            balldirecy = -2
        elif playdirec == 'down':
            #so now ball should go down diagonally
            balldirec = -(balldirec) #reversing ball x direction
            balldirecy = 2
        elif playdirec == 'still':
            #so now ball should go straight
            balldirec = -(balldirec) #reversing ball x direction

    # ENEMY based bounce back

    #enemyrect.x += 1
    if ballserve == 'enemy':
        ballx -= balldirec
        bally += balldirecy

    if enemyrect.colliderect(ballrect) and ballx == 100:  #enemy pos = 50 and width = 50 so 100

        ballx = 100 #no changes req for enemy rect

        #if oppdirec == 'still':
        #    balldirec = -(balldirec)

        if endirec == 'up':
            #so now ball should go up diagonally
            balldirec = -(balldirec) #reversing ball x direction
            balldirecy = -2    
        elif endirec == 'down':
            #so now ball should go down diagonally
            balldirec = -(balldirec) #reversing ball x direction
            balldirecy = 2   
        elif endirec == 'still':
            #so now ball should go straight
            balldirec = -(balldirec) #reversing ball x direction

    # Game screen boundary based bounce back

    if ballrect.top < 0:  # top boundary
        balldirecy = 2
    elif ballrect.bottom > 600:
        balldirecy = -2   # bottom boundary
        
        
def enemyai():
    #global ballx,bally, balldirec,balldirecy, ballrect, ballrectx, oppdirec
    #moved all enemy ball logic to ball ai bec i realised all ball logic should be there only
    pass

    
#MAIN GAME WHILE LOOP
while gameactive:

    #varibles that need to be constnatly updated are put inside loop and they are first
    ballrectx = ballx - ballrad
    ballrecty = bally - ballrad

    ballrect = pygame.Rect(ballrectx, ballrecty, (ballrad * 2), (ballrad * 2))
    

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


    # black background and clears screen bec no bg now
    screen.fill((0, 0, 0))  

    #animations
    ball_ai()
    enemyai()

    if gameactive == True:
        #draw all entities

        pygame.draw.rect(screen, 'white', ballrect) #hitbox rect of ball
        pygame.draw.circle(screen, 'yellow', (ballx, bally), ballrad)

        pygame.draw.rect(screen, 'orange', playerrect)
        pygame.draw.rect(screen, 'orange', enemyrect)
        

    pygame.display.update()
    clock.tick(60)