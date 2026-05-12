import pygame

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