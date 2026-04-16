import pygame

width, height = (900,600)

# set display mode with vsync enabled
screen = pygame.display.set_mode((width, height), vsync=1)

background_surface = pygame.Surface((width, height)).convert()
background_surface.fill((0,0,0))

fps = 60

def display():
    pygame.Surface.blit(screen, background_surface, (0, 0))
    
def display_update():
    # updates the display
    pygame.display.update()
    # sets max frame rate
    pygame.time.Clock().tick(fps)