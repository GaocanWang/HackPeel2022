import pygame
from pygame.locals import (
    K_SPACE
)

pygame.init

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))

running = True

while running:
    for event in pygame.event.get():

        if event.type == quit:
            running = False
            
screen.fill((255, 255, 255))

surf = pygame.Surface((50, 50))

surf.fill((0, 0, 0))
rect = surf.get_rect()

screen.blit(surf, (screen_width/2, screen_height/2))
pygame.display.flip()
