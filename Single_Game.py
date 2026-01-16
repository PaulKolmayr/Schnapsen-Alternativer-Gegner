"""
Module regulates the game flow during a single game:
 - Game start: Is called only once at the start, covers the original 5 card draw as well as who starts to play
 - See won Cards: In Schnapsen, for people that are not good at reading cards, they can always look at their won
   cards to at least see part of what was played. While the GUI is not done, the game is limited to certain points
   in the game where it asks if the player wants to see them.
 - Trumpf switch: Game decides when player is allowed to switch trumpf and calls the needed methods
 - Player closes deck: Game decides when player is allowed to close the deck and calls the needed methods
 - Player thinks about playing a pair: In players turn, the game checks if the possibility of playing a pair is given
 - Player plays in front: Method organizes the players turn, so that he is able to play a card and the opponent follows
 - Opponent plays in front: Method organizes Opponents turn
 - Drawing after Round: Mathod to organize the players drawing after the turn
"""

from Card_Properties import Deck as Cards
from Player import Player as Player
from Opponent import Opponent as Opponent
from Rule_Book import RuleBook as Rules
from Point_System import PointSystem as Points
from Input_Output import InputOutput as Controls

class SingleGame:

    def __init__(self):
        self._cards = Cards()
        self._player = Player(self._cards)
        self._opponent = Opponent(self._cards)
        self._rules = Rules(self._cards)
        self._points = Points()
        self._controls = Controls()


        self._trumpf = None
        self._trumpf_farbe = None
        self._player_card = None
        self._opponent_card = None
        self._player_starts = False
        self._deck_closed = False
        self._wins = [0, 0]
        self._all_played_cards = []

    @property
    def show_trumpf(self):
        self._controls.show_trumpf(self._trumpf)

    @property
    def show_trumpf_farbe(self):
        self._controls.show_trumpf_farbe(self._trumpf_farbe)
    
    @property
    def show_battleground(self):
        self._controls.show_battleground(self._battleground)
    
    def game_start(self):
        """
        Players draw their cards, the trumpf is drawn, and input on who dealt the cards is asked for. Based on this
        input, the starter is decided.
        """
        #start procedure
        self._cards.shuffle()
        self._player.first_draw()
        self._opponent.first_draw()
        
        ###########Terminal interaction
        
        dealer = self._controls.who_has_dealt()
        self._controls.starter_message(dealer)
        self._player_starts = self._rules.who_starts(dealer)
        self._controls.show_player_hand(self._player._hand)

        self._trumpf = self._cards.draw()

        self._trumpf_farbe = self._trumpf.suit.name
        self._controls.show_trumpf(self._trumpf)

    
    def see_won_cards(self):
        """
        Method calls for input if player wants to see the cards he won up to the points. Based on the answer,
        the cards are shown or not
        """
        see_won = self._controls.see_won_cards()
        if see_won == 'Ja':
            self._controls.show_won_cards(self._points._won_cards)
    
    def trumpf_switch(self):
        """
        Method calls the right methods to check legality, ask for will to and then switch the trumpf card with the
        Bube of the player
        """
        legal_switch = self._rules.can_trumpf_be_switched(self._player._hand, self._trumpf)

        if legal_switch == True:
            switch = self._controls.switch_trumpf()
            switch_wanted = self._player.switch_trumpf(switch)
        
            if switch_wanted == True:
                wanted_card = [card for card in self._player._hand if card.rank.name == 'Bube' and card.suit.name == self._trumpf.suit.name]
                self._player._hand.append(self._trumpf)
                self._player._hand.remove(wanted_card[0])
                self._trumpf = wanted_card[0]

                self._controls.show_player_hand(self._player._hand)
                self._controls.show_trumpf(self._trumpf)


    def player_closes_the_deck(self):
        """
        Method asks the player if he wants to close the deck, then acts upon his will
        """
        if self._deck_closed == False:
            self._controls.show_player_hand(self._player._hand)
            closedeck_question = self._controls.close_the_deck()
            self._deck_closed = self._rules.zudrehen(closedeck_question)
            if self._deck_closed == True:
                game_counter = 5
                self._controls.deck_is_closed()
    

    def player_thinks_about_playing_a_pair(self):
        """
        Method checks if there are pairs to play, if there is a pair to be played then asks if the player wants
        to play a pair. If the player does not want to or has no pair, he is directed to the method that deals with him
        not playing a pair.
        If he wants to play a pair and has one, he is directed to the method that dealt with him playing one pair
        If there is more than one pair to be played, he gets asked which pair he wants to play and gets directed to 
        the method for multiple pairs.
        In the end, his legal cards and the trumpf or at least the trumpf suit are shown
        """
        pairs = self._rules.can_pair_be_played(self._player._hand)
        if len(pairs) > 0:
            decision = self._controls.pair_can_be_played(pairs)

        if len(pairs) == 1 and decision == 'Ja':
            self._player.play_pair(pairs)
        elif len(pairs) > 1 and decision == 'Ja':
            decision2 = self._controls.more_pairs_can_be_played()
            self._player.plays_more_pairs(pairs, decision2)
        else:
            self._player.plays_no_pair()
        self._controls.show_playable_cards(self._player._playable)
        if self._deck_closed == True:
            self.show_trumpf_farbe
        else:
            self.show_trumpf

    
    def player_plays_in_front(self):
        """
        Player gets asked which card he wants to play, then this card is chosen, gets checked for legality and lastly,
        is placed in the battleground and removed from the players handcards
        After that, the opponent chooses his card, which again gets placed in the battleground and removed from his handcards
        """
        #Player plays a card
        legal_card = False
        while legal_card == False:
            card = self._controls.which_card_to_play()
            playcard = self._player.plays_card(card)
            legal = self._rules.legality_play(playcard, self._player._playable)
            if legal == True:
                self._battleground.append(playcard)
                self._player_card = playcard
                self._player._hand.remove(playcard)
                self._controls.playercard_played(playcard)
                legal_card = True
            else:
                self._controls.illegal_card_error()

        #Opponent plays card
        op_card = self._opponent.plays_second(self._deck_closed,playcard, self._trumpf)
        self._battleground.append(op_card)
        self._opponent_card = op_card
        self._opponent._hand.remove(op_card)
        self._controls.show_battleground(self._battleground)

    
    def opponent_plays_in_front(self):
        """
        First, the opponent playes his card, which gets placed in the battleground and removed from his hand.
        Then, it is inspected which card the player can play, he gets to choose his card and he plays it.
        """
        #Opponent plays first
        self._opponent_card = self._opponent.plays_first(self._points._points_opponent, self._trumpf)
        self._battleground.append(self._opponent_card)
        self._controls.opponentcard_played(self._opponent_card)

        #Player plays second
        if self._points._won_cards:
            self.see_won_cards()

        legal_retort = False
        while legal_retort == False:
            self._player.plays_second(self._opponent_card, self._deck_closed)
            self._controls.show_playable_cards(self._player._playable)
            if self._deck_closed == True:
                self._controls.show_trumpf_farbe(self._trumpf_farbe)
            else:
                self._controls.show_trumpf(self._trumpf)

            card = self._controls.which_card_to_play()
            pl_card = self._player.plays_card(card)
            legality = self._rules.legality_play(pl_card, self._player._playable)
            if legality == True:
                self._battleground.append(pl_card)
                self._player_card = pl_card
                self._player._hand.remove(pl_card)
                print()
                self._controls.show_battleground(self._battleground)
                legal_retort = True
            else:
                self._controls.illegal_card_error()



    def drawing_cards_after_round(self):
        """
        If the deck is not closed, the winner draws first, then the looser of the last play. This calls the methods that
        check if the player needs to draw from the deck or the trumpf card. 
        In any case, the winner plays first in the next play, so the starter is reevaluated on this basis
        """
        self._all_played_cards.append(self._player_card)
        self._all_played_cards.append(self._opponent_card)
        print(self._all_played_cards)
        if self._points._who_won == 'Spieler':
            if self._deck_closed == False:
                self._player.normal_draw(self._trumpf)
                self._opponent.normal_draw(self._trumpf)
            self._player_starts = True
        else:
            if self._deck_closed == False:
                self._opponent.normal_draw(self._trumpf)
                self._player.normal_draw(self._trumpf)
            self._player_starts = False
        
        if self._deck_closed == False:
            self._deck_closed = self._rules.deck_empty()



    def game(self):
        """
        Method controls all the elements in a single game.
        First, game start is called
        Then, while no player has more than 66 points and they still have cards, depending on who plays first,
        the method organizes what needs to happen when.
        The battleground is emptied before every round because there can only be two cards that are compared
        If Player starts:
         - Check if he wants to see his cards
         - Check if a switch is possible/wanted
         - Check if he wants to close the deck
         - Check if a pair is possible/wanted
         - Cards are played, player first
         - Update the scores
         - Let the players draw their cards
        If Opponent starts:
         - Opponent may switch card
         - Cards are played, opponent first
         - Update the scores
         - Let the players draw their cards
        If the game has ended, work out how many points who has won
        """
        self.game_start()
        game_counter = 10
        while self._points._points_player < 66 and self._points._points_opponent < 66 and len(self._player._hand) > 0:
            print(f"Runde {game_counter}")
            self._controls.break_between_games()

            self._battleground = []
            if self._player_starts == True:

                if self._points._won_cards:     #If Player wants to look at his won hands, he can
                    self.see_won_cards()

                self.trumpf_switch()            #Can Player switch the trumpf and does he want to
                self.player_closes_the_deck()   #Player can close the deck, leads to different rules for which cards to play
                self.player_thinks_about_playing_a_pair() #Does Player have a Pair and does he want to play it
                self.player_plays_in_front()    #Players play their cards

                #Determining the winner
                self._points.pair_points(self._player._plays_pair, self._player_starts, self._player_card, self._trumpf)
                self._points.points_system(self._player_card, self._opponent_card, self._player_starts, self._trumpf)
                self._points.adding_pair_points()

                self._controls.scoring_prints(self._points._who_won, self._points._points_player, self._points._points_opponent)

                #Drawing Cards and who starts the next cards
                self.drawing_cards_after_round()

                
            elif self._player_starts == False:

                card_in_question = self._opponent.switches_trumpf(self._trumpf) #Opponent can change trumpf
                if self._trumpf != card_in_question:
                    self._controls.opponent_drew_trumpf()
                self._trumpf = card_in_question
                #self._opponent_closes_deck()                                   #Opponent can close the deck
                self.opponent_plays_in_front()                                  #Players play their cards

                #Determining the winner
                self._points.pair_points(self._opponent._plays_pair, self._player_starts, self._opponent_card, self._trumpf)
                self._points.points_system(self._player_card, self._opponent_card, self._player_starts, self._trumpf)
                self._points.adding_pair_points()

                self._controls.scoring_prints(self._points._who_won, self._points._points_player, self._points._points_opponent)

                #Drawing Cards and who starts the next cards
                self.drawing_cards_after_round()

            game_counter -= 1

        self._wins = self._points.win_counter()




