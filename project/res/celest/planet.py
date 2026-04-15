import pygame

class Planet():
    def __init__(self) -> None:
        self.radius: int
        self.mass: int # or mass idk

        #________________________________________________________________________________________________________#
        self.angle: int # the offset from the star that the velocity is aplied, 0 and 360 would be into the star
        self.velocity: int # the start speed of the planet
        #________________________________________________________________________________________________________#

        self.position = [0,0]
        self.color: int

        width, height = [20,20]

        self.surface = pygame.Surface((width, height)).convert()
        self.surface.fill((255, 0, 242))
        self.rect = self.surface.get_rect()

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
        x_pos, y_pos = self.position
        self.rect.center = (x_pos, y_pos)
        SCREEN.blit(self.surface, self.rect)
