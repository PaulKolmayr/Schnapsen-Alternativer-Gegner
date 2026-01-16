"""
Module contains Methods regarding Points, Winners and generally results:
 - Points System: Takes the played cards and evaluates who won
 - Win Counter: End of Game, checks who earned how many points
 - Pair points: Stores points derived from pairs, especially in case a player played a pair while having 0 points
 - Adding pair points: Checks if there are pair points to add/if they can be added and adds them if possible
"""

class PointSystem:

    def __init__(self):
        self._points_player = 0
        self._points_opponent = 0
        self._pair_points_player = 0
        self._pair_points_opponent = 0
        self._won_cards = []
        self._who_won = None

    
    @property
    def show_won_cards(self):
        print(f"Gewonnene Karten: {', '.join(str(card) for card in self._won_cards)}")

    def points_system(self, player_card, opponent_card, player_starts, trumpf):
        """
        Points system gets passed the players card, the opponents card, who startet and the trumpf card and on the basis 
        of these factors evaluates who won the play, also adds the won cards points to the winners tally.
        """
        if player_card.suit.name == opponent_card.suit.name:

            if player_card.rank.value > opponent_card.rank.value:
                self._points_player += player_card.rank.value
                self._points_player += opponent_card.rank.value
                self._won_cards.append(player_card)
                self._won_cards.append(opponent_card)
                self._who_won = 'Spieler'
            else:
                self._points_opponent += player_card.rank.value
                self._points_opponent += opponent_card.rank.value
                self._who_won = 'Gegner'
        
        elif player_card.suit.name != opponent_card.suit.name:
            
            if player_starts == True:

                if opponent_card.suit.name == trumpf.suit.name:
                    self._points_opponent += player_card.rank.value
                    self._points_opponent += opponent_card.rank.value
                    self._who_won = 'Gegner'
                else:
                    self._points_player += player_card.rank.value
                    self._points_player += opponent_card.rank.value
                    self._won_cards.append(player_card)
                    self._won_cards.append(opponent_card)
                    self._who_won = 'Spieler'
            
            if player_starts == False:

                if player_card.suit.name == trumpf.suit.name:
                    self._points_player += player_card.rank.value
                    self._points_player += opponent_card.rank.value
                    self._won_cards.append(player_card)
                    self._won_cards.append(opponent_card)
                    self._who_won = 'Spieler'
                else:
                    self._points_opponent += player_card.rank.value
                    self._points_opponent += opponent_card.rank.value
                    self._who_won = 'Gegner'
            
    
    def win_counter(self):
        """
        Method checks the players as well as the opponents points and decides who has to get how many points
        """
        if self._points_player >= 66 and self._points_opponent == 0:
            score = [3, 0]
         
        elif self._points_player >= 66 and self._points_opponent < 33:
            score = [2, 0]
         
        elif self._points_player >= 66 and self._points_opponent < 66:
            score = [1, 0]
            
        elif self._points_opponent >= 66 and self._points_player == 0:
            score = [0, 3]
           
        elif self._points_opponent >= 66 and self._points_player < 33:
            score = [0, 2]
           
        elif self._points_opponent >= 66 and self._points_player < 66:
            score = [0, 1]

        elif self._points_player < 66 and self._points_opponent < 66:
            if self._who_won == 'Gegner':
                score = [0, 1]

            elif self._who_won == 'Spieler':
                score = [1, 0]

        return score
        

    def pair_points(self, plays_pair, player_starts, playcard, trumpf):
        """
        In Schnapsen, the rule is that a player that has 0 points cant receive points from calling a pair until he has
        at least 1 points. So points derived from playing a pair need to be stored until they can per the rules be added.
        Also, a trumpf pair gives the player that played it 40 instead of 20 points so this method makes this distinction.
        """
        if plays_pair == True:
            if player_starts == True:
                if playcard.suit.name == trumpf.suit.name:
                    self._pair_points_player += 40
                else:
                    self._pair_points_player += 20
            elif player_starts == False:
                if playcard.suit.name == trumpf.suit.name:
                    self._pair_points_opponent += 40
                else:
                    self._pair_points_opponent += 20
    
    def adding_pair_points(self):
        """
        Method deals with the pair points and if they can be added to the points tally.
        Is called after every turn so that they get added as soon as possible.
        """
        if self._pair_points_player > 0:
            if self._points_player > 0:
                self._points_player += self._pair_points_player
                print(f"Spieler bekommt {self._pair_points_player} Punkte wegen seinem Paar.")
                self._pair_points_player = 0
            else:
                pass
        
        if self._pair_points_opponent > 0:
            if self._points_opponent > 0:
                self._points_opponent += self._pair_points_opponent
                print(f"Gegner bekommt {self._pair_points_opponent} wegen seinem Paar.")
                self._pair_points_opponent = 0

