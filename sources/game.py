# Pygame import and initialization
import pygame
import sys

# Pygame initialization
pygame.init()

# Window settings
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Window title
pygame.display.set_caption("My Pygame Game")

# Clock for controlling FPS
clock = pygame.time.Clock()

# Colors
BLACK = (0, 0, 0)

# Example game module
class GameModule:
    def __init__(self):
        # Initialize module variables here
        pass
    
    def update(self):
        # Update logic
        pass
    
    def draw(self, screen):
        # Draw game elements on the screen
        pass

# Initializing modules
game_module = GameModule()

# Main game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Updating modules
    game_module.update()

    # Filling the screen
    screen.fill(BLACK)

    # Drawing modules
    game_module.draw(screen)

    # Updating the display
    pygame.display.flip()

    # Calculating and displaying FPS
    fps = clock.get_fps()
    pygame.display.set_caption("My Pygame Game - FPS: {:.2f}".format(fps))
    
    # Limiting FPS
    clock.tick(120)

# Properly quitting Pygame
pygame.quit()
sys.exit()