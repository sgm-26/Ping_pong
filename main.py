#  2nd GAME TRY!! stopped flappy bird bec main goal is make as many games as possibles
#  so to learn new principles and also use previously learned lesson  I AM STARTING GAME 2!!
# time - finish in 3 days fast before teen camp
#and also coding gives more joy than gaming! so now i will leave gaming and full time think about coding!
#AND ALSO USING GIT FOR FIRST TIME IN REAL GAME


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

#BUG HERE
def ball_ai():
    global ballx
    ballx += 1

def enemyai():
    pass

#MAIN GAME WHILE LOOP
while gameactive:

    #TEST:putting all variable here bec of local variable glitch
    

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
        pygame.draw.circle(screen, 'yellow', (ballx, bally), ballrad)

    pygame.display.update()
    clock.tick(60)