import pygame

class Star():
    def __init__(self) -> None:
        self.mass: int
        self.radius: int = 218 # use au as units

        x, y = pygame.display.get_window_size()
        self.position = [x // 2, y // 2] # allays makes the star the center
    
    def setParams(self, M, R):
        self.mass = M
        self.radius = R
    
    def draw(self, SCREEN):
        pygame.draw.circle(SCREEN, (255,255,255), self.position, self.radius)