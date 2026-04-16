import pygame

class Planet():
    def __init__(self) -> None:
        self.radius = 10
        self.mass: int # or mass idk

        #________________________________________________________________________________________________________#
        self.angle: int # the offset from the star that the velocity is aplied, 0 and 360 would be into the star
        self.velocity: int # the start speed of the planet
        #________________________________________________________________________________________________________#

        self.position = [0,0]
        self.color = (0,255,0)

    def setPrams(self, radius, mass, angle, velocity, position, color) -> None:
        self.radius = radius
        self.mass = mass
        self.angle = angle
        self.velocity = velocity

        self.position = position
        self.color = color
        
    def updatePos(self, X, Y):
        self.position[0] += X
        self.position[1] += Y
    
    def getPos(self):
        return [self.position[0], self.position[1]]

    def draw(self, SCREEN) -> None:
        pygame.draw.circle(SCREEN, self.color, self.position, self.radius)
