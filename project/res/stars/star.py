import pygame

class Star():
    def __init__(self) -> None:
        self.mass: int
        self.radius = 30

        x, y = pygame.display.get_window_size()
        self.position = [x // 2, y // 2]
    
    def draw(self, SCREEN):
        pygame.draw.circle(SCREEN, (252, 219, 3), self.position, self.radius)