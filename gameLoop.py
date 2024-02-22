import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Définition des dimensions de la fenêtre de jeu
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Couleur de fond et couleur du rectangle
background_color = (0, 0, 0)
rectangle_color = (255, 0, 0)  # Rouge

# Position initiale du rectangle
rect_x = 50
rect_y = 50
# Taille du rectangle
rect_width = 60
rect_height = 40
# Vitesse du rectangle
rect_speed = 5

# Horloge pour contrôler les FPS
clock = pygame.time.Clock()
fps = 120

# Boucle de jeu principale
running = True
while running:
    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Mise à jour du jeu (logique de jeu, déplacements, etc.)
    rect_x += rect_speed
    # Rebondit sur les bords de l'écran
    if rect_x > screen_width - rect_width or rect_x < 0:
        rect_speed = -rect_speed

    # Rendu
    screen.fill(background_color)
    # Dessin du rectangle
    pygame.draw.rect(screen, rectangle_color, (rect_x, rect_y, rect_width, rect_height))

    pygame.display.flip()  # Mise à jour de l'écran

    # Limite les FPS
    clock.tick(fps)

# Quitter Pygame proprement
pygame.quit()
sys.exit()
