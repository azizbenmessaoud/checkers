import pygame
from checkers.contants import WIDTH, HEIGHT
# from checkers.game import Game

# screen 
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("checkers")

def main():

    run = True
    fps = 60
    clock = pygame.time.Clock()
    # game = Game()

    while run:
        clock.tick(60)

        events = pygame.event.get()
        for event in events:

            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()

    pygame.quit()

main()