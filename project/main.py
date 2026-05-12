import pygame
from res import Celest, Core, Stars

pygame.init()

print("starting")

engine = Core.Gravi()
window = Core.Display()

p1 = Celest.Planet()
#           Rad    Mass          Velos            Pos
p1.setParams(8, 59722*10**7, [80000, 6*10**5], [200,400], (200,0,0))

p2 = Celest.Planet()
p2.setParams(8, 4072200000000.0, [-80000, 6*10**5], [850,430], (0,200,0))

s1 = Celest.Planet()
s1.setParams(100, -1.989*10**18, [0,0], [450,350], (255,255,255))

print("params set")

engine.appendBody(p1)
engine.appendBody(p2)

engine.appendBody(s1)

print("drawing window")

while True:
    window.handle_events()
    window.empty()
    engine.compute()
    p1.draw(window.screen)
    p2.draw(window.screen)
    s1.draw(window.screen)
    window.update()