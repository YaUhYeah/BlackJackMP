import sys
import random

sys.path.append('../blackjack')
sys.path.append('../')

import gameutils


class Deck:
    def __init__(self, cards_in_deck):
        self.cards_in_deck = cards_in_deck
        random.shuffle(self.cards_in_deck)

    def show_card(self, index, display, pos_x, pos_y):
        display.blit(self.cards_in_deck[index].card_image, (pos_x, pos_y))


class Card:
    def __init__(self, identifier, card_name, card_value, card_pos_x, card_pos_y):
        self.identifier = identifier
        self.card_name = card_name
        self.card_value = card_value
        self.card_image = gameutils.get_image(card_pos_x, card_pos_y)


cards = [Card(0,"Ace of Clubs", 1, 0, 0), Card(1,"2 of Clubs", 2, gameutils.CARD_WIDTH, 0), Card(2,"3 of Clubs", 3, gameutils.CARD_WIDTH*2, 0),
         Card(3,"4 of Clubs", 4, gameutils.CARD_WIDTH*3, 0), Card(4,"5 of Clubs", 6, gameutils.CARD_WIDTH*4, 0), Card(5,"6 of Clubs", 6,gameutils.CARD_WIDTH*5,0),
         Card(6,"7 of Clubs", 7, gameutils.CARD_WIDTH*6, 0), Card(7,"8 of Clubs", 8, gameutils.CARD_WIDTH*7, 0), Card(8,"9 of Clubs", 9, gameutils.CARD_WIDTH*8, 0),
         Card(9,"10 of Clubs", 10, gameutils.CARD_WIDTH*9, 0), Card(10,"Jack of Clubs", 10, gameutils.CARD_WIDTH*10, 0), Card(11,"Queen of Clubs", 10, gameutils.CARD_WIDTH*11, 0),
         Card(12,"King of Clubs", 10, gameutils.CARD_WIDTH*12, 0),

         Card(13, "Ace of Diamonds", 1, 0, gameutils.CARD_HEIGHT),
         Card(14, "2 of Diamonds", 2, gameutils.CARD_WIDTH, gameutils.CARD_HEIGHT),
         Card(15, "3 of Diamonds", 3, gameutils.CARD_WIDTH * 2, gameutils.CARD_HEIGHT),
         Card(16, "4 of Diamonds", 4, gameutils.CARD_WIDTH * 3, gameutils.CARD_HEIGHT),
         Card(17, "5 of Diamonds", 6, gameutils.CARD_WIDTH * 4, gameutils.CARD_HEIGHT),
         Card(18, "6 of Diamonds", 6, gameutils.CARD_WIDTH * 5, gameutils.CARD_HEIGHT),
         Card(19, "7 of Diamonds", 7, gameutils.CARD_WIDTH * 6, gameutils.CARD_HEIGHT),
         Card(20, "8 of Diamonds", 9, gameutils.CARD_WIDTH * 7, gameutils.CARD_HEIGHT),
         Card(21, "9 of Diamonds", 9, gameutils.CARD_WIDTH * 8, gameutils.CARD_HEIGHT),
         Card(22, "10 of Diamonds", 10, gameutils.CARD_WIDTH * 9, gameutils.CARD_HEIGHT),
         Card(23, "Jack of Diamonds", 10, gameutils.CARD_WIDTH * 11, gameutils.CARD_HEIGHT),
         Card(24, "Queen of Diamonds", 10, gameutils.CARD_WIDTH * 12, gameutils.CARD_HEIGHT),
         Card(25, "King of Diamonds", 10, gameutils.CARD_WIDTH * 13, gameutils.CARD_HEIGHT),

         Card(26, "Ace of Hearts", 1, 0, gameutils.CARD_HEIGHT * 2),
         Card(27, "2 of Hearts", 2, gameutils.CARD_WIDTH, gameutils.CARD_HEIGHT * 2),
         Card(28, "3 of Hearts", 3, gameutils.CARD_WIDTH * 2, gameutils.CARD_HEIGHT * 2),
         Card(29, "4 of Hearts", 4, gameutils.CARD_WIDTH * 3, gameutils.CARD_HEIGHT * 2),
         Card(30, "5 of Hearts", 6, gameutils.CARD_WIDTH * 4, gameutils.CARD_HEIGHT * 2),
         Card(31, "6 of Hearts", 6, gameutils.CARD_WIDTH * 5, gameutils.CARD_HEIGHT * 2),
         Card(32, "7 of Hearts", 7, gameutils.CARD_WIDTH * 6, gameutils.CARD_HEIGHT * 2),
         Card(33, "8 of Hearts", 9, gameutils.CARD_WIDTH * 7, gameutils.CARD_HEIGHT * 2),
         Card(34, "9 of Hearts", 9, gameutils.CARD_WIDTH * 8, gameutils.CARD_HEIGHT * 2),
         Card(35, "10 of Hearts", 10, gameutils.CARD_WIDTH * 9, gameutils.CARD_HEIGHT * 2),
         Card(36, "Jack of Hearts", 10, gameutils.CARD_WIDTH * 11, gameutils.CARD_HEIGHT * 2),
         Card(37, "Queen of Hearts", 10, gameutils.CARD_WIDTH * 12, gameutils.CARD_HEIGHT * 2),
         Card(38, "King of Hearts", 10, gameutils.CARD_WIDTH * 13, gameutils.CARD_HEIGHT * 2),
         Card(39, "Ace of Spades", 1, 0, gameutils.CARD_HEIGHT * 3),
         Card(40, "2 of Spades", 2, gameutils.CARD_WIDTH, gameutils.CARD_HEIGHT* 3),
         Card(41, "3 of Spades", 3, gameutils.CARD_WIDTH * 2, gameutils.CARD_HEIGHT* 3),
         Card(42, "4 of Spades", 4, gameutils.CARD_WIDTH * 3, gameutils.CARD_HEIGHT* 3),
         Card(43, "5 of Spades", 6, gameutils.CARD_WIDTH * 4, gameutils.CARD_HEIGHT* 3),
         Card(44, "6 of Spades", 6, gameutils.CARD_WIDTH * 5, gameutils.CARD_HEIGHT* 3),
         Card(45, "7 of Spades", 7, gameutils.CARD_WIDTH * 6, gameutils.CARD_HEIGHT* 3),
         Card(46, "8 of Spades", 9, gameutils.CARD_WIDTH * 7, gameutils.CARD_HEIGHT* 3),
         Card(47, "9 of Spades", 9, gameutils.CARD_WIDTH * 8, gameutils.CARD_HEIGHT* 3),
         Card(48, "10 of Spades", 10, gameutils.CARD_WIDTH * 9, gameutils.CARD_HEIGHT* 3),
         Card(49, "Jack of Spades", 10, gameutils.CARD_WIDTH * 11, gameutils.CARD_HEIGHT* 3),
         Card(50, "Queen of Spades", 10, gameutils.CARD_WIDTH * 12, gameutils.CARD_HEIGHT* 3),
         Card(51, "King of Spades", 10, gameutils.CARD_WIDTH * 13, gameutils.CARD_HEIGHT* 3)
         ]

deck = Deck(cards)
