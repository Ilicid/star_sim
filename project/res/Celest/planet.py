import pygame

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