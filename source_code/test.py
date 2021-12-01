import pygame, sys, random
from pygame.locals import *

FPS = 30
pygame.init()

score = 0
FPS = 30
fpsClock = pygame.time.Clock()

#window set up
display = pygame.display.set_mode((600, 600))

# rgb colours
black = (0, 0, 0)
white = (255, 255, 255)
skyblue = (0,191,255) 
orange = (255, 165, 0)
green = (0, 255, 0)
red = (255, 0, 0)

mainFont = pygame.font.Font("slkscr.ttf",50)

top = skyblue
bot = red
right = orange
left = green



leftSide = ((0, 0), (75, 75), (75,525), (0, 600))
topSide = ((0, 0), (75, 75), (525, 75), (600, 0))
bottomSide = ((0, 600), (75, 525), (525,525), (600, 600))
rightSide = ((600, 0), (525, 75), (525, 525), (600, 600))

player = Rect(275, 200, 50, 50)
playerColour = white
ay = 1

def bounceAnimation(


while True:
    display.fill(black)
    pygame.draw.polygon(display, left, leftSide)
    pygame.draw.polygon(display, top, topSide)
    pygame.draw.polygon(display, bot, bottomSide)
    pygame.draw.polygon(display, right, rightSide)
    if (player.y >= 525-50):
        if (playerColour == bot or playerColour == white):
            score += 1
        else:
            game = False
            playerColour = changeColour(playerColour)
        if ay > 46:
            dy = -50
        else:
            ay += 0.5
            dy = -4 - ay
        
    if (player.y <= 200):
        if ay > 46:
            dy = 50
        else:
            dy = 4 + ay
    player.y += dy
    pygame.draw.rect(display, playerColour, player)
            

    

    for event in pygame.event.get():
        if (event.type == QUIT):
            pygame.quit()
            sys.exit()



    pygame.display.update()
    fpsClock.tick(FPS)
