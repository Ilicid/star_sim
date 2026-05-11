from contextlib import nullcontext
import pygame
import sys
import math

var = 0

pygame.init()

class display:
    def __init__(self) -> None:
        self.width, self.height = (900, 600)
        self.clock = pygame.time.Clock()
        self.sim_speed = 200

        self.screen = pygame.display.set_mode((self.width, self.height), pygame.RESIZABLE) # make window thing

        #----------background stuff----------#

        self.background_surface = pygame.Surface((self.width, self.height)).convert()
        self.background_surface.fill((0, 0, 255))
    
    def empty(self):
        self.screen.blit(self.background_surface, (0, 0))

    def update(self):
        pygame.display.update()
        self.clock.tick(self.sim_speed)
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("shutting down")
                pygame.quit()
                sys.exit()

            elif event.type == pygame.VIDEORESIZE:
                self.width, self.height = event.size

                # redraw background, so it doesnt make that ulgy thingy
                self.background_surface = pygame.Surface((self.width, self.height)).convert()
                self.background_surface.fill((0, 0, 0))

class Planet():
    def __init__(self) -> None:
        self.mass: float
        self.position: list[float] = [0,0]
        self.velocity: list[float] = [0,0]
        self.radius: int = 2 # use au as units
        self.color: tuple = (0,255,0)

    def setParams(self, RADIUS, MASS, VELOCITY, POSITION, RGB) -> None:
        self.radius = RADIUS
        self.mass = MASS
        self.velocity = VELOCITY
        self.position = POSITION
        self.color = RGB
        
    def updatePos(self, X, Y):
        self.position[0] += X
        self.position[1] += Y

    def draw(self, SCREEN) -> None:
        pygame.draw.circle(SCREEN, self.color, self.position, self.radius)
        
class Star():
    def __init__(self) -> None:
        self.mass: float # why am i type hinting??
        self.radius: int = 218 # default radius so it dont give error
        self.position: tuple[int,int]

        self.color = (255,255,255)
    
    def setParams(self, R: int, M: float):
        self.radius = R
        self.mass = M

    def draw(self, SCREEN):
        x, y = pygame.display.get_window_size()
        self.position = (x // 2, y // 2) # just here for now
        pygame.draw.circle(SCREEN, self.color, self.position, self.radius)

    def draw2(self, SCREEN): # cuz nicklas
        x, y = pygame.display.get_window_size()
        self.position = (x // 2, y // 2)
        pygame.draw.circle(SCREEN, (255, 174, 0), self.position, self.radius)

class gravi:
    def __init__(self) -> None:
        self.G: float =  1 #6.67430 * (10**(-11))
        self.bodies: list = []
        self.QUEUE: list = []
        self.dt: float = 1*10**-15
    
    def appenedBody(self, BODY):
        self.bodies.append(BODY)
    def compute(self):
        for body1 in self.bodies:
            POS1 = body1.position
            VELOCITY = body1.velocity

            ax = 0
            ay = 0

            for body2 in self.bodies:
                if body2 is body1:
                    continue

                POS2 = body2.position
                MASS = body2.mass

                dx = POS2[0] - POS1[0]
                dy = POS2[1] - POS1[1]

                dist = math.sqrt(dx**2 + dy**2)

                if dist < 1:
                    continue

                ax += self.G * MASS * dx / dist**3
                ay += self.G * MASS * dy / dist**3

            VELOCITY[0] += ax
            VELOCITY[1] += ay

            #print(VELOCITY[0], VELOCITY[1])
            body1.updatePos(
                VELOCITY[0] * self.dt,
                VELOCITY[1] * self.dt
            )

engine = gravi()
window = display()

p1 = Planet()
#           Rad Mass                Velos                    Pos
p1.setParams(8, 5972200000000.0, [0.5, 3.5], [200,400], (200,0,0))


s1 = Planet()
s1.setParams(100, 1.9890000000000003e+18, [0,0], [450,350], (255,255,255))

engine.appenedBody(p1)

engine.appenedBody(s1)


while True:
    window.handle_events()
    window.empty()
    engine.compute()
    p1.draw(window.screen)
    print(p1.velocity[0],p1.velocity[1])
    s1.draw(window.screen)
    window.update()