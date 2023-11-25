import pygame
import sys
import math

pygame.init()

# Paramètres de la fenêtre
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Yeux Réalistes")

# Couleurs
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
beige = (245, 245, 220)  # Couleur beige
dark_beige = (205, 183, 158)  # Couleur beige plus foncée

# Paramètres des yeux
eye_radius = 50
pupil_radius1 = 20
pupil_radius2 = 20
iris_radius = 35
eyelid_height = 10
eye_color = white
pupil_color = black
iris_color = blue
eyelid_color = black  # Couleur beige

# Position des yeux
eye1_x = width // 3
eye1_y = height // 2
eye2_x = 2 * width // 3
eye2_y = height // 2

# Boucle principale
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Simulation d'une réaction pupillaire pour les deux yeux
    mouse_x, mouse_y = pygame.mouse.get_pos()

    distance_eyes1 = ((mouse_x - eye1_x) ** 2 + (mouse_y - eye1_y) ** 2) ** 0.5
    distance_eyes2 = ((mouse_x - eye2_x) ** 2 + (mouse_y - eye2_y) ** 2) ** 0.5
    if distance_eyes1 > pupil_radius1+10:
        pupil_radius1 = min(pupil_radius1 + 1, 15)  # Limite la taille maximale de la pupille
    else:
        pupil_radius1 = max(pupil_radius1 - 1, 10)  # Limite la taille minimale de la pupille

    if distance_eyes2 > pupil_radius2+10:
        pupil_radius2 = min(pupil_radius2 + 1, 15)  # Limite la taille maximale de la pupille
    else:
        pupil_radius2 = max(pupil_radius2 - 1, 10)  # Limite la taille minimale de la pupille


    # Dessine les yeux
    screen.fill(dark_beige)

    # Œil 1
    pygame.draw.circle(screen, eye_color, (eye1_x, eye1_y), eye_radius)
    pygame.draw.circle(screen, beige, (eye1_x, eye1_y), eye_radius)
    pygame.draw.circle(screen, iris_color, (eye1_x, eye1_y), iris_radius)
    pygame.draw.circle(screen, pupil_color, (eye1_x, eye1_y), pupil_radius1)
    pygame.draw.arc(screen, eyelid_color, (eye1_x - eye_radius, eye1_y - eyelid_height-40, eye_radius * 2, eyelid_height * 2),
                    0, math.pi, 2)

    # Œil 2
    pygame.draw.circle(screen, eye_color, (eye2_x, eye2_y), eye_radius)
    pygame.draw.circle(screen, beige, (eye2_x, eye2_y), eye_radius)
    pygame.draw.circle(screen, iris_color, (eye2_x, eye2_y), iris_radius)
    pygame.draw.circle(screen, pupil_color, (eye2_x, eye2_y), pupil_radius2)
    pygame.draw.arc(screen, eyelid_color, (eye2_x - eye_radius, eye2_y - eyelid_height-40, eye_radius * 2, eyelid_height * 2),
                    0, math.pi, 2)

    pygame.display.flip()
    clock.tick(20)  # Limite le taux de rafraîchissement à 60 FPS
