import pygame

from res import Celest, Engine, Stars, Window

pygame.init()

window = Window.display()
window2 = Window.display()

engine = Engine.gravi()

print("started")

while True:
    window.handle_events()
    window.empty() 

    window.update()