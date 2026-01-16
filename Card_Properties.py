"""
Creating the Cards as their own objects for the best possibility to work with them as well as print them    
"""
from enum import Enum, auto
from dataclasses import dataclass
import random

#creating the different faces of the cards
class Rank(Enum):
    """
    Establishing the different ranks the cards can have
    """
    Ass = 11
    Zehn = 10
    König = 4
    Dame = 3
    Bube = 2

#creating the different suites 
class Suit(Enum):
    """
    Establishing the different suits the cards can have
    """
    Herz = auto()
    Kreuz = auto()
    Karo = auto()
    Pik = auto()


#nicer options for printing
SYMBOLS = {Suit.Herz : '\u2665',
           Suit.Kreuz : '\u2663',
           Suit.Karo : '\u2666',
           Suit.Pik : '\u2660'}

#nicer options for printing
RANKS = {Rank.Ass : 'A',
         Rank.Zehn : '10',
         Rank.König : 'K',
         Rank.Dame : 'D',
         Rank.Bube : 'B'}

#creating the card itself
@dataclass(frozen = True)
class Card:
    """
    Establishing that each card has the characteristics rank and suits and adding a nice looking way for printing 
    them in the terminal
    """
    rank: Rank
    suit: Suit

    def __str__(self):
        return f"{SYMBOLS[self.suit]}{RANKS[self.rank]}"


#finally creating the deck of cards
class Deck:
    """
    Establishing that every combination of rank and suit is to be found in the deck and creating methods
    to shuffle the deck and to draw cards
    """
    def __init__(self):
        self._deck = [Card(rank, suit) for suit in Suit for rank in Rank]

    @property
    def get_deck(self):
        return self._deck
    
    @property
    def show_deck(self):
        print(f"Gegner Spielkarten: {', '.join(str(card) for card in self._deck)}")     
    

    def shuffle(self):
        """
        If this method is called, the cards in the deck are arranged in a new random order
        More "real-life" way of making sure players get random cards compared to them just drawing random cards
        """
        random.shuffle(self._deck)

    def draw(self):
        """
        If a card is drawn, it is popped from the deck as to be unavailable for the remainder of the game, so until there 
        is a new deck for the next game
        """
        if not self._deck:
            raise RuntimeError("Letzte Karte wurde schon gezogen")
        return self._deck.pop()


