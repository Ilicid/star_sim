import pygame
import math

class Planet():
    def __init__(self) -> None:
        self.mass: float
        self.position: list[float] = [0,0]
        self.velocity: list[float] = [0,0]
        self.radius: int = 2 # use au as units
        self.color: tuple = (0,255,0)

    def setParams(self, R, M, V, POS, RGB) -> None:
        self.radius = R
        self.mass = M
        self.velocity = V
        self.position = POS
        self.color = RGB
        
    def updatePos(self, X, Y):
        self.position[0] += X
        self.position[1] += Y

    def draw(self, SCREEN) -> None:
        pygame.draw.circle(SCREEN, self.color, self.position, self.radius)

class gravi:
    def __init__(self) -> None:
        self.G: float = 6.67430 * (10**(-11))
        self.bodies: list = []
        self.QUEUE: list = []
        self.dt: float = 0.0001
    
    def appenedBody(self, BODY):
        self.bodies.append(BODY)

    def compute(self):
        for body1 in self.bodies:
            POS1: list[float] = body1.position
            VELOCITY: list[float] = body1.velocity
            ax: float = 0
            ay: float = 0

            for body2 in self.bodies:
                if body2 is body1:
                    continue

                POS2: list[float]= body2.position
                MASS: float = body2.mass

                dx = POS2[0] - POS1[0]
                dy = POS2[1] - POS1[1]

                dist: float = math.sqrt(dx**2 + dy**2)
                if dist == 0:
                    continue

                ax += self.G * MASS * dx / dist**3
                ay += self.G * MASS * dy / dist**3
            
                VELOCITY[0] += ax*self.dt
                VELOCITY[1] += ay*self.dt

            POS1[0] += VELOCITY[0]
            POS1[1] += VELOCITY[1]
            print(POS1[0], POS1[1])

p1 = Planet()
p1.setParams(1, 30, [0,0], [5,5], (2,2,2))
p2 = Planet()
p2.setParams(1, 26, [0,0], [10,7], (2,2,2))
p3 = Planet()
p3.setParams(1, 47, [0,0], [0,10], (2,2,2))

engine = gravi()

engine.appenedBody(p1)
engine.appenedBody(p2)
engine.appenedBody(p3)

while True:
    engine.compute()