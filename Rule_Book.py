"""
Module for the rules of the game, mostly for the player:
 - Deck is empty: If the deck is empty, notify the game to close the deck
 - Deck gets 'zugedreht': If the player wishes to close the deck, notify the game to close the deck
 - Who starts: It is custom that the player who dealt the cards does not start by playing first. So 
   get the input who dealt and then return True/False so the game knows who has to play first
 - Can trumpf be switched: Check if the trumpf can be switched before asking the player if he wants to do it
 - Can pair be played: Check if pair can be called before asing player if he wants to play a pair
 - legality play: check that card the player wants to play is legal
"""

from Card_Properties import Deck as Cards

class RuleBook:

    def __init__(self, cards):
        self._cards = cards
        

    def deck_empty(self):
        """
        If the deck is empty, notify the game that deck is closed
        """
        if len(self._cards._deck) == 0:
            return True
        else:
            return False

    def zudrehen(self, zugedreht):
        """
        If player wants to close the deck, notify the game to close the deck
        """
        if zugedreht == 'Ja':
            return True
        else:
            return False
    
    def who_starts(self, who_dealt):
        """
        If passed input is 'Spieler', he dealt so he doesnt play first. Therefore, notify the game that player_starts has to
        be False.
        Same principle the other way around.
        """
        if who_dealt == "Spieler":
            return False
        else:
            return True
    
    
    def can_trumpf_be_switched(self, hand, trumpf):
        """
        Trumpf can only be switched when there are more than two cards remaining so len(deck) needs to be > 1. 
        If this is true, check the players hand cards and search for a Bube of the same suit as the trumpf. If 
        one is found, notify the game that there is one and the game can ask player if he wants to switch. Else 
        notify the game that there is nothing to ask about.
        """
        if len(self._cards._deck) > 1:
            for card in hand:
                if card.rank.name == 'Bube' and card.suit.name == trumpf.suit.name:
                    return True
                else:
                    pass

    def can_pair_be_played(self, hand):
        """
        Search for pairs by searching queens and kings and compare their suits. If there are one or multiple pairs
        of kings and queens of the same suit, pass this list on to the game.
        """
        dames = []
        kings = []
        pairs = []
        for dame in hand:
            if dame.rank.name == 'Dame':
                dames.append(dame)
        for king in hand:
            if king.rank.name == 'König':
                kings.append(king)
        
        for card_a in dames:
            for card_b in kings:
                if card_a.suit.name == card_b.suit.name:
                    pairs.append([card_a, card_b])

        return pairs
    
    def legality_play(self, card, playable):
        """
        Player only decides what card to play from his hand, this methods checks the card for legality.
        """
        if card in playable:
            return True
        else:
            return False

   

        

