#Importing all the modules
try:
    import time, random, sys, os
except ImportError:
    print("Make sure to have the time module")
    sys.exit()
try:
    import pygame
except ImportError:
    print("Make sure you have python 3 and pygame.")
    sys.exit()
try:
    import main
except ImportError:
    print("Make sure you have all the extra files")
from pygame import freetype


#game_font = pygame.freetype.Font("Font.ttf", 75)
#text_surface, rect = game_font.render(("Programmer: 8BitToaster"), (0, 0, 0))
#gameDisplay.blit(text_surface, (150, 300))

# Initialize the game engine
pygame.init()


DisplayWidth,DisplayHeight = 1000, 800
clock = pygame.time.Clock()

gameDisplay = pygame.display.set_mode((DisplayWidth,DisplayHeight))
pygame.display.set_caption("Name")
font_100 = pygame.freetype.Font("Font.ttf", 100)
font_50 = pygame.freetype.Font("Font.ttf", 50)
font_75 = pygame.freetype.Font("Font.ttf", 75) 
SizeCheck = pygame.font.Font("Font.ttf", 50)
SizeCheck_75 = pygame.font.Font("Font.ttf", 75)

#The Buttons
class Button():
    def __init__(self, x, y, width, height, Text):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = Text

    def draw(self):
        pos = pygame.mouse.get_pos()
        if self.x <= pos[0] <= self.x + self.width and self.y <= pos[1] <= self.y + self.height:
            pygame.draw.rect(gameDisplay,(150,0,0),(self.x,self.y,self.width,self.height),0)
        else:
            pygame.draw.rect(gameDisplay,(250,0,0),(self.x,self.y,self.width,self.height),0)
        pygame.draw.rect(gameDisplay,(100,100,100),(self.x,self.y,self.width,self.height),5)

        text_surface, rect = font_50.render(str(self.text), (0, 0, 0))
        if self.text != "Options":
            gameDisplay.blit(text_surface, (self.x + int(self.width/2)+30 - int(SizeCheck.size(str(self.text))[0]), self.y + int(self.height/2) - 20))
        else:
            gameDisplay.blit(text_surface, (self.x + int(self.width/2)+43 - int(SizeCheck.size(str(self.text))[0]), self.y + int(self.height/2) - 20))

def shorten(Num):
    count = 0
    let = ""
    while Num >= 1000:
        Num /= 1000
        count += 1
    Num = str(Num)
    Num2 = ""
    if count >= 1:
        for i in range(Num.index(".")+2):
            Num2 += Num[i]
        Num = Num2
    if count == 1:
        Num += "K"
    if count == 2:
        Num += "M"
    if count == 3:
        Num += "B"
    if count == 4:
        Num += "T"
    if count == 5:
        Num += "q"
    if count == 6:
        Num += "Q"
    if count == 7:
        Num += "s"
    if count == 8:
        Num += "S"
    return Num

def HomeScreen(score=0):
    game_run = True
    Buttons = [Button(400,600,200,100,"Play")]
    
    while game_run == True:

        gameDisplay.fill((210,140,42))
        pos = pygame.mouse.get_pos()
        text_surface, rect = font_100.render(("Fruit Slasher"), (0, 0, 0))
        gameDisplay.blit(text_surface, (220, 100))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i, button in enumerate(Buttons):
                    if button.x <= pos[0] <= button.x + button.width and button.y <= pos[1] <= button.y + button.height:
                        if i == 0:
                            main.game_loop()

        if score != 0:
            text_surface, rect = font_75.render(("Score: " + shorten(score)), (0, 0, 0))
            gameDisplay.blit(text_surface, (480 - SizeCheck_75.size(shorten(score))[0], 300))


        #Updating the buttons
        for button in Buttons:
            button.draw()

        pygame.display.flip()
        clock.tick(60)



if __name__ == "__main__":
    HomeScreen()
