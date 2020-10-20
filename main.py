import pygame
import sys
from pygame.locals import *
from constants import *
import global_functions


def main():
    #screen = pygame.display.set_mode((WIDTH, HEIGHT))
    screen = pygame.display.set_mode((1200, 960))
    pygame.display.set_caption('Mastermind') #Nombre de la ventana
    BAR = load_image('images/bar.png', True)

    while True:
        keys = pygame.key.get_pressed()
        for events in pygame.event.get():
            if events.type == QUIT:
                sys.exit(0)
        screen.blit(BAR, (580, 340))
        screen.blit(BLUE_CIRCLE, (0, 800))
        screen.blit(GREEN_CIRCLE, (140, 800))
        screen.blit(RED_CIRCLE, (280, 800))
        screen.blit(YELLOW_CIRCLE, (420, 800))

        pygame.display.flip() # Actualiza la ventana
    return 0



if __name__ == '__main__':
    pygame.init()
    main()