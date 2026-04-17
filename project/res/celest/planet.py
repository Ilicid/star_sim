import pygame

class Planet():
    def __init__(self) -> None:
        self.radius: int = 2 # use au as units
        self.mass: int
        self.velocity: int # initial speed of the planet
        self.position: list = [0,0]

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
    
    def getPos(self):
        return [self.position[0], self.position[1]]

    def draw(self, SCREEN) -> None:
        pygame.draw.circle(SCREEN, self.color, self.position, self.radius)
