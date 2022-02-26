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

#game loop
run = True
while run:
    #draw a background
    screen.blit(bg_image, (0, 0))
    screen.blit(char_image, (400, 300))

    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #update display window
    pygame.display.update()

pygame.quit()
