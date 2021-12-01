import pygame, sys, random


pygame.init()

bounceSound = pygame.mixer.Sound("bounce noise.wav")
pygame.mixer.music.load("backgroundmusic.mp3")

score = 0
FPS = 30
fpsClock = pygame.time.Clock()

#window set up
display = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Bounce") #window name


# rgb colours
black = (0, 0, 0)
white = (255, 255, 255)
skyblue = (0,191,255) 
orange = (255, 165, 0)
green = (0, 255, 0)
red = (255, 0, 0)

#score board
mainFont = pygame.font.Font("slkscr.ttf",50)

#polygon points for the sides
leftSide = ((0, 0), (75, 75), (75,525), (0, 600))
topSide = ((0, 0), (75, 75), (525, 75), (600, 0))
bottomSide = ((0, 600), (75, 525), (525,525), (600, 600))
rightSide = ((600, 0), (525, 75), (525, 525), (600, 600))



#walls 
top = skyblue
bot = red
right = orange
left = green


#player
player = pygame.Rect(275, 200, 50, 50)
playerColour = white


class Button():
    def __init__(self, xCord, yCord, width, height, text, buttonColour, textColour):
        self.xCord = xCord
        self.yCord = yCord
        self.width = width
        self.height = height
        self.text = text
        self.buttonColour = buttonColour
        self.textColour = textColour
        self.shape = pygame.Rect(xCord, yCord, width, height)
        self.colourText =  textColour
        self.colourButton = buttonColour
    def drawButton(self):
        pygame.draw.rect(display, self.buttonColour, self.shape)
        textOutput(self.text, True, self.textColour, self.buttonColour, (self.xCord + self.width//2, self.yCord + self.height//2))
        pygame.draw.lines(display, white, True,((self.xCord,self.yCord),(self.xCord+self.width,self.yCord),(self.xCord+self.width,self.yCord+self.height),(self.xCord,self.yCord+self.height)), 3)
    def isHover(self,mousePosition):
        if (mousePosition[0] > self.xCord and mousePosition[0] < self.xCord + self.width) and (mousePosition[1] > self.yCord and mousePosition[1] < self.yCord + self.height):
            self.buttonColour = self.colourText
            self.textColour = self.colourButton
            return True
        else:
            self.buttonColour = self.colourButton
            self.textColour = self.colourText
            return False

def loadHighScores():
    highScoresFile = open("highscores.txt")
    highScore1 = highScoresFile.readline()[:-1]
    highScore2 = highScoresFile.readline()[:-1]
    highScore3 = highScoresFile.readline()
    nameScore1 = highScore1.split(" ")
    nameScore2 = highScore2.split(" ")
    nameScore3 = highScore3.split(" ")
    return (nameScore1, nameScore2, nameScore3)

def displayHighScores(highscores):
    textOutput("High Scores", False, white, black, (300,140))
    textOutput(highscores[0][1], False, white, black, (155,185))
    textOutput(highscores[1][1], False, white, black, (155,235))
    textOutput(highscores[2][1], False, white, black, (155,285))
    textOutput(highscores[0][0], True, white, black, (350,185))
    textOutput(highscores[1][0], True, white, black, (350,235))
    textOutput(highscores[2][0], True, white, black, (350,285))
    

def typeName(score, playerColour):
    place = isHighscore(score)
    highScores = loadHighScores()

    if place == 1:
        cover = pygame.Rect(100, 160, 500, 50)
        pygame.draw.rect(display,black,cover)
        textOutput(str(score), False, playerColour, black, (155,185))
        textOutput(text, False, playerColour, black, (350,185))
        highScores[0][1] = str(score)

    elif place == 2:
        cover = pygame.Rect(100, 210, 500, 50)
        pygame.draw.rect(display,black,cover)
        textOutput(str(score), False, playerColour, black, (155,235))
        textOutput(text, False, playerColour, black, (350,235))
        highScores[1][1] = str(score)
        
    elif place == 3:
        cover = pygame.Rect(100, 260, 500, 50)
        pygame.draw.rect(display,black,cover)
        textOutput(str(score), False, playerColour, black, (155,285))
        textOutput(text, False, playerColour, black, (350,285))
        highScores[2][1] = str(score)
    return text


def isHighscore(score):
    highScores = loadHighScores()
    if score >= int(highScores[0][1]):
        return 1
    elif score >= int(highScores[1][1]):
        return 2
    elif score >= int(highScores[2][1]):
        return 3
    else:
        return 4
    
def updateHighScore(name,score, place):
    score = str(score)
    highScores = loadHighScores()
    if place == 1:
        updatedHighScores = name+" "+score+"\n"+highScores[1][0]+" "+highScores[1][1]+"\n"+highScores[2][0]+" "+highScores[2][1]
    elif place == 2:
        updatedHighScores = highScores[0][0]+" "+highScores[0][1]+"\n"+name+" "+score+"\n"+highScores[2][0]+" "+highScores[2][1]
    elif place == 3:
        updatedHighScores = highScores[0][0]+" "+highScores[0][1]+"\n"+highScores[1][0]+" "+highScores[1][1]+"\n"+name+" "+score
    else:
        updatedHighScores = highScores[0][0]+" "+highScores[0][1]+"\n"+highScores[1][0]+" "+highScores[1][1]+"\n"+highScores[2][0]+" "+highScores[2][1]
    highScoreFile = open("highscores.txt", "w")    
    highScoreFile.write(updatedHighScores)



def textOutput(text, antialias, textColour, highlightColour, position):
    """text: string of text to output onto screen
anti-alias: bool enables anti-alias
textColour: RGBcolour or RGB tuple (r, g, b)
highlightColour: RGBcolour or RGB tuple (r, g, b)
position: tuple of x and y cordinate
returns nothing"""
    outputSurface = mainFont.render(text, antialias, textColour, highlightColour)
    outputRect = outputSurface.get_rect()
    outputRect.center = position
    display.blit(outputSurface, outputRect)

def menu():
    display.fill(black)
    playButton.isHover(pygame.mouse.get_pos())
    playButton.drawButton()
    quitMenuButton.isHover(pygame.mouse.get_pos())
    quitMenuButton.drawButton()
    pygame.draw.rect(display, playerColour, player)
    colourWalls(top, right, bot, left, display)
    textOutput("Bounce", True, white, black, (300,150))
    if (playButton.isHover(pygame.mouse.get_pos()) == True) and (pygame.mouse.get_pressed()[0] == 1):
        return True
    elif (quitMenuButton.isHover(pygame.mouse.get_pos()) == True) and (pygame.mouse.get_pressed()[0] == 1):
        pygame.quit()
        sys.exit()
    
def changeColour(oldColour):
    """oldColour: the current colour of the player
returns a colour other than the old colour"""
    colourList = [red, skyblue, orange, green]
    newColour = oldColour
    while (oldColour == newColour):
        num = random.randint(0,3)
        newColour = colourList[num]

    return newColour

def flip(top, right, bot, left, key):
    if key == "left":
        (top, right, bot, left) = (right, bot, left, top)
        return (top, right, bot, left)

    elif key == "up":
        (top, right, bot, left) = (bot, left, top, right)
        return (top, right, bot, left)

    elif key == "right":
        (top, right, bot, left) = (left, top, right, bot)
        return (top, right, bot, left)

def colourWalls(top, right, bot, left, surface):
    pygame.draw.polygon(surface, left, leftSide)
    pygame.draw.polygon(surface, top, topSide)
    pygame.draw.polygon(surface, bot, bottomSide)
    pygame.draw.polygon(surface, right, rightSide)
    
def scoreUpdate(score):
    textOutput("Score: " + str(score), True, white, black, (300, 150))

def gameOver(playerColour):
    display.fill(black)
    textOutput("Game Over", True, white, black, (300, 25))
    textOutput("Final Score: "+ str(score), True, playerColour, black, (300, 75))
    retryButton.isHover(pygame.mouse.get_pos())
    retryButton.drawButton()
    quitButton.isHover(pygame.mouse.get_pos())
    quitButton.drawButton()
    pygame.draw.rect(display, playerColour, pygame.Rect(275, 475, 50, 50))
    displayHighScores(loadHighScores())
    if (retryButton.isHover(pygame.mouse.get_pos()) == True) and (pygame.mouse.get_pressed()[0] == 1):
        return True
    elif (quitButton.isHover(pygame.mouse.get_pos()) == True) and (pygame.mouse.get_pressed()[0] == 1):
        pygame.quit()
        sys.exit()
    else:
        return False
        

icon = pygame.Surface((1,1))
pygame.draw.rect(icon, playerColour,(0, 0, 1, 1))
pygame.display.set_icon(icon)

retryButton = Button(175, 340, 250, 50, "Retry?", white, black)
quitButton = Button(200, 400, 200, 50, "Quit?", white, black)
playButton = Button(200, 300, 200, 50, "Play", white, black)
quitMenuButton = Button(200, 360, 200, 50, "Quit?", white, black)

play = False
text = ''
send = False
game = True
dy = 0.10
ay = 1


pygame.mixer.music.play(-1)
while True:
    
    
    if not play:
        play = menu()
        
    elif game:
        display.fill(black)
        colourWalls(top, right, bot, left, display)
        scoreUpdate(score)

        if (player.y >= 525-50):
            if (playerColour == bot or playerColour == white):
                pygame.mixer.Sound.play(bounceSound)
                score += 1
            else:
                game = False
            if game:
                playerColour = changeColour(playerColour)
                pygame.draw.rect(icon, playerColour,(0, 0, 1, 1))
                pygame.display.set_icon(icon)
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
        
    else:
        if not gameOver(playerColour):
            if (isHighscore(score) < 4 and not send):
                name = typeName(score, playerColour)
        else:
            score = 0
            playerColour = white
            ay = 1
            game = True
            send = False
            text = ''

    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            pygame.mixer.music.stop()
            pygame.quit()
            sys.exit()
        if (event.type == pygame.KEYDOWN):
            if (event.key == pygame.K_UP):
                newWalls = flip(top, right, bot, left, "up")
            elif (event.key == pygame.K_RIGHT):
                newWalls = flip(top, right, bot, left, "right")
            elif (event.key == pygame.K_LEFT):
                newWalls = flip(top, right, bot, left, "left")
            if (event.key == pygame.K_UP) or (event.key == pygame.K_RIGHT) or (event.key == pygame.K_LEFT):
                top = newWalls[0]
                right = newWalls[1]
                bot = newWalls[2]
                left = newWalls[3]
            if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                updateHighScore(name,score,isHighscore(score))
                send = True
            elif event.key == pygame.K_BACKSPACE:
                text = text[:-1]
            elif event.key == pygame.K_SPACE:
                pass
            elif len(text) < 8 and not(event.key == pygame.K_UP) or (event.key == pygame.K_RIGHT) or (event.key == pygame.K_LEFT):
                text += event.unicode

            
    pygame.display.update()
    fpsClock.tick(FPS)
