import pygame
import sys

def main():
    # Initialisation de pygame
    pygame.init()

    # Paramètres de la fenêtre
    screen_width = 640
    screen_height = 400
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Jeu d'Aventure Point-and-Click")

    # Couleurs
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    # Définition des zones de l'interface
    action_area_height = 320
    text_area_height = 40
    command_area_height = screen_height - (action_area_height + text_area_height)

    # Définition de la police et de la taille
    font_size = 18
    font = pygame.font.Font(None, font_size)

    # Liste des verbes
    verbs = ["Aller", "Ouvrir", "Prendre", "Allumer", "O-Serrure", "Tirer",
             "Fermer", "Pousser", "Eteindre", "Lire", "Donner", "Changer",
             "Réparer", "Utiliser"]

    # Fonction pour afficher les verbes
    def draw_verbs():
        verb_padding = 5  # Espace entre les verbes
        verb_area_width = screen_width / len(verbs)
        for index, verb in enumerate(verbs):
            verb_surface = font.render(verb, True, WHITE)
            verb_x = verb_area_width * index + verb_padding
            verb_y = action_area_height + text_area_height + (command_area_height - font_size) // 2
            screen.blit(verb_surface, (verb_x, verb_y))

    # Initialisation de l'horloge
    clock = pygame.time.Clock()

    # Boucle principale
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # Ajouter la gestion des événements de clic ici si nécessaire

        # Remplir le fond
        screen.fill(BLACK)

        # Dessiner les zones de l'interface
        action_area = pygame.Rect(0, 0, screen_width, action_area_height)
        text_area = pygame.Rect(0, action_area_height, screen_width, text_area_height)
        command_area = pygame.Rect(0, action_area_height + text_area_height, screen_width, command_area_height)

        pygame.draw.rect(screen, WHITE, action_area, 1)
        pygame.draw.rect(screen, WHITE, text_area, 1)
        pygame.draw.rect(screen, WHITE, command_area, 1)

        # Dessiner les verbes
        draw_verbs()

        # Mise à jour de l'affichage
        pygame.display.flip()

        # 60 images par seconde
        clock.tick(60)

    # Quitter pygame
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
