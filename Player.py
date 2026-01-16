"""
Module contains Player Moves
 - Player first draw: Player draws 5 cards
 - Player normal draw: Player draws a card after move
 - Player switches trumpf: Player gets asked if he wants to switch his Bube for trumpf
   I'm still of the opinion that this should always be done but the player has the choice
 - Player plays pair: List of players legal cards gets altered to contain only the pair he
   wants to call/play
 - Player has more pairs: Method takes in the decision which pair the player wants to call, 
   legal cards again then are this pair
 - Player plays no pair: If player doesnt have or doesnt want to play a pair, he can play each card in his hand
 - Player plays second: Another legality check for legal cards if he plays second and therefore might have to 'answer' the 
   Opponents card
 - Player plays card: Mechanism for player to play his chosen card
"""

from Card_Properties import Deck as Cards

class Player:

    def __init__(self, cards):
        """
         - Deck imported so that there is continuity with which cards are in play and in the deck etc. during the game, 
           also deck method is needed for the draw
         - Hand initialized because it needs to be accessible and store the values that are only changed by the methods
        """
        self._cards = cards
        self._hand = []

    @property
    def show_hand(self):
        print(f"Ihre Spielkarten: {', '.join(str(card) for card in self._hand)}")

    @property
    def show_playable(self):
        print(f"Spielbare Karten: {', '.join(str(card) for card in self._playable)}")

    def first_draw(self):
        """
        Player draws 5 Cards that are popped from the deck, these 5 cards are then only available in Opponents Deck
        Only used at start of the game
        """
        self._hand = [self._cards.draw() for _ in range(5)]


    def normal_draw(self, trumpf):
        """
        Simulates what happens in a real life game of Schnapsen, Player draws from the deck until there is only the
        trumpf card, then he draws that one
        No precaution for when both are empty because this is covered in the SingleGame class
        """
        if len(self._cards._deck) > 0:
            self._hand.append(self._cards.draw())
        else:
            self._hand.append(trumpf)
    

    def switch_trumpf(self, quest):
        """
        Method gets passed an input, if the input is 'Ja', signaling that Player wants to switch trumpf, returns True,
        else returns False
        Method was more relevant before I had to put all the inputs into their own class to work on a GUI. If this is still
        in the version I submit, let it be known that this was an oversight which I hopefully have corrected until then.
        """
        if quest == 'Ja':
            return True
        else:
            return False
        

    def play_pair(self, pairs):
        """
        If Player calls a pair, per the rules of Schnapsen, he has to play one of the cards of the said pair. Therefore, his
        legal cards are only the cards in the pair.
        self._playable is only initialized in each method rather than in the class because differently to the hand cards, it
        needs to be completely new every time, while on the whole, the hand cards are only manipulated by one card getting deleted
        and one being added every turn.
        """
        self._playable = []
        self._plays_pair = False
        
        for pair in pairs:
            self._playable = [card for card in self._hand if card in pair]
            self._plays_pair = True
                        

    def plays_more_pairs(self, pairs, decision2):
        """
        If more than one pair is available to be called, this method is called. It gets a decision which pair should be played
        passed, and the legal cards get updated to only contain the two cards of the pair the player wants to play
        """
        self._playable = [card for card in self._hand]
        self._plays_pair = False

        for pair in pairs:
            if decision2 == pair[0].suit.name:
                self._playable = [card for card in self._hand if card in pair]
                self._plays_pair = True
                break

    def plays_no_pair(self):
        """
        If player cant or chooses not to play a pair, the game directs to this method, which defines that the legal cards he
        can play are each card in his hand.
        This is okay since he can only call his pair if he plays first, so he doesnt have any other restrictions.
        """
        self._playable = []
        self._plays_pair = False

        self._playable = [card for card in self._hand]


    def plays_second(self, op_card, zugedreht):
        """
        If player plays second, depending on the status of the deck, there are different rules:
        If the deck is closed, he has to play a card of the same suit if he has one. If not, he is free to play any other card.
        If the deck is open, he is once again free to play any card in his hand.
        """
        self._playable = []
        if zugedreht == False:
            self._playable = [card for card in self._hand]
        else:
            for cards in self._hand:
                if cards.suit.name == op_card.suit.name:
                    self._playable.append(cards)
            
            if len(self._playable) == 0:
                self._playable = [card for card in self._hand]
        


    def plays_card(self, card):
        """
        Method gets passed Players decision to play a certain card. This input is split into its suit and rank,
        if both fit the same card, this card is returned to the game as the card the player wants to play.
        """
        card_suit, card_rank = card.split()

        for stack in self._hand:
            if card_suit == stack.suit.name and card_rank == stack.rank.name:
                return stack
    

    
                
