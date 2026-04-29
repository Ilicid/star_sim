import pygame

from res import celest, stars, core

pygame.init()
print("started")

window = core.display()

p1 = celest.Planet()
s1 = stars.Star()

while True:
    window.handle_events()
    window.empty()
    p1.draw(window.screen)
    s1.draw(window.screen)
    #s1.draw2(window.screen)
    window.update()