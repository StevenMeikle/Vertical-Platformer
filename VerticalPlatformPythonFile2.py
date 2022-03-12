#import libraries
import pygame

#initialize pygame
pygame.init()

#game window dimensions
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

#create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #() is called a tuple, it is a data type.
pygame.display.set_caption('Falling Game') 

#load images
bg_image = pygame.image.load('Blue.png').convert_alpha()
char_image = pygame.image.load('Character.png').convert_alpha()

#player class
class Player():
    def __init__(self, x, y):
        self.image = pygame.transform.scale(char_image, (45, 45)) #Add the jumping image here inside the scale()
        self.width = 25
        self.height = 40
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = (x, y)
    def draw(self):
        screen.blit(self.image, (self.rect.x - 12, self.rect.y - 5))
class Background():
    def __init__(self, x, y):
        self.image = pygame.transform.scale(bg_image, (400, 600))
        self.width = SCREEN_WIDTH
        self.height = SCREEN_HEIGHT
    def drawBackground(self):
        screen.blit(self.image, (0, 0))
        

jumpy = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 150 )
tileBackground = Background(0, 0)

#game loop
run = True
while run:
    #draw a background
    screen.blit(bg_image, (0, 0))
    jumpy.draw()

    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #update display window
    pygame.display.update()

pygame.quit()
