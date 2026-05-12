import pygame
import sys

class Display:
    def __init__(self) -> None:
        self.width, self.height = (900, 600)
        self.clock = pygame.time.Clock()
        self.sim_speed = 200

        self.screen = pygame.display.set_mode((self.width, self.height), pygame.RESIZABLE) # make window thing

        self.background_surface = pygame.Surface((self.width, self.height)).convert()
        self.background_surface.fill((0, 0, 0))
    
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