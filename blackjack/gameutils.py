import pygame

CARD_WIDTH = 113
CARD_HEIGHT = 124
SPRITE_SHEET = pygame.image.load("../resources/deck_cards.png")


def get_image(pos_x, pos_y):
    image = pygame.Surface([CARD_WIDTH, CARD_HEIGHT])
    image.blit(SPRITE_SHEET, (0, 0), (pos_x, pos_y, CARD_WIDTH, CARD_HEIGHT))
    image.set_colorkey(pygame.Color(85,85,255))

    return image
