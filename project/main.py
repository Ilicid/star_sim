import pygame
import sys
from res import display, celest, stars

pygame.init()

p1 = celest.Planet()
s1 = stars.Star()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    display.display()
    s1.draw(display.screen)
    display.display_update()