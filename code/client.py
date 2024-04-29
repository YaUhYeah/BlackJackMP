import sys

import pygame

from network import Connection

sys.path.append('../blackjack')

clock = pygame.time.Clock()
width = 500
height = 500
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

clientNumber = 0


def main():
    pygame.init()
    run = True
    c = Connection()
    player = c.get_p()
    while run:
        clock.tick(60)
        pygame.display.update()
        player2 = c.send(player)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()


if __name__ == '__main__':
    main()
