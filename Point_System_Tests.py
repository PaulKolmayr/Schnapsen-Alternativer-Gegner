"""
Docstring for Point_System_Tests
"""

import unittest
from unittest.mock import MagicMock, patch
from Point_System import PointSystem as Points

class TestPointSystem(unittest.TestCase):

    def setUp(self):
        self._cards_test = MagicMock()
        self._points = Points()


    def test_pointsystem_player_plays_and_wins_same_colour(self):
        player_card = MagicMock()
        player_card.rank.name = 'Ass'
        player_card.rank.value = 11
        player_card.suit.name = 'Herz'

        opponent_card = MagicMock()
        opponent_card.rank.name = 'Zehn'
        opponent_card.rank.value = 10
        opponent_card.suit.name = 'Herz'
        
        trumpf = MagicMock()
        trumpf.rank.name = 'König'
        trumpf.rank.value = 4
        trumpf.suit.name = 'Herz'

        player_starts = True

        self._points.points_system(player_card, opponent_card, player_starts, trumpf)
        self.assertEqual('Spieler', self._points._who_won)
        self.assertEqual([player_card, opponent_card], self._points._won_cards)
        self.assertEqual(21, self._points._points_player)
        self.assertEqual(0, self._points._points_opponent)

    
    def test_pointsystem_player_plays_and_wins_different_colour(self):
        player_card = MagicMock()
        player_card.rank.name = 'König'
        player_card.rank.value = 4
        player_card.suit.name = 'Karo'

        opponent_card = MagicMock()
        opponent_card.rank.name = 'Zehn'
        opponent_card.rank.value = 10
        opponent_card.suit.name = 'Pik'
        
        trumpf = MagicMock()
        trumpf.rank.name = 'König'
        trumpf.rank.value = 4
        trumpf.suit.name = 'Herz'

        player_starts = True

        self._points.points_system(player_card, opponent_card, player_starts, trumpf)
        self.assertEqual('Spieler', self._points._who_won)
        self.assertEqual([player_card, opponent_card], self._points._won_cards)
        self.assertEqual(14, self._points._points_player)
        self.assertEqual(0, self._points._points_opponent)
    
     
    def test_pointsystem_player_plays_and_loses_same_colour(self):
        player_card = MagicMock()
        player_card.rank.name = 'Zehn'
        player_card.rank.value = 10
        player_card.suit.name = 'Herz'

        opponent_card = MagicMock()
        opponent_card.rank.name = 'Ass'
        opponent_card.rank.value = 11
        opponent_card.suit.name = 'Herz'
        
        trumpf = MagicMock()
        trumpf.rank.name = 'König'
        trumpf.rank.value = 4
        trumpf.suit.name = 'Herz'

        player_starts = True

        self._points.points_system(player_card, opponent_card, player_starts, trumpf)
        self.assertEqual('Gegner', self._points._who_won)
        self.assertEqual([], self._points._won_cards)
        self.assertEqual(0, self._points._points_player)
        self.assertEqual(21, self._points._points_opponent)

    
    def test_pointsystem_player_plays_and_loses_different_colour(self):
        player_card = MagicMock()
        player_card.rank.name = 'Ass'
        player_card.rank.value = 11
        player_card.suit.name = 'Karo'

        opponent_card = MagicMock()
        opponent_card.rank.name = 'Zehn'
        opponent_card.rank.value = 10
        opponent_card.suit.name = 'Herz'
        
        trumpf = MagicMock()
        trumpf.rank.name = 'König'
        trumpf.rank.value = 4
        trumpf.suit.name = 'Herz'

        player_starts = True

        self._points.points_system(player_card, opponent_card, player_starts, trumpf)
        self.assertEqual('Gegner', self._points._who_won)
        self.assertEqual([], self._points._won_cards)
        self.assertEqual(0, self._points._points_player)
        self.assertEqual(21, self._points._points_opponent)


    def test_pointsystem_opponent_starts_and_loses_same_colors(self):
        player_card = MagicMock()
        player_card.rank.name = 'Ass'
        player_card.rank.value = 11
        player_card.suit.name = 'Herz'

        opponent_card = MagicMock()
        opponent_card.rank.name = 'Zehn'
        opponent_card.rank.value = 10
        opponent_card.suit.name = 'Herz'
        
        trumpf = MagicMock()
        trumpf.rank.name = 'König'
        trumpf.rank.value = 4
        trumpf.suit.name = 'Herz'

        player_starts = False

        self._points.points_system(player_card, opponent_card, player_starts, trumpf)
        self.assertEqual('Spieler', self._points._who_won)
        self.assertEqual([player_card, opponent_card], self._points._won_cards)
        self.assertEqual(21, self._points._points_player)
        self.assertEqual(0, self._points._points_opponent)


    def test_pointsystem_opponent_plays_and_loses_different_colour(self):
        player_card = MagicMock()
        player_card.rank.name = 'Dame'
        player_card.rank.value = 3
        player_card.suit.name = 'Herz'

        opponent_card = MagicMock()
        opponent_card.rank.name = 'Zehn'
        opponent_card.rank.value = 10
        opponent_card.suit.name = 'Pik'
        
        trumpf = MagicMock()
        trumpf.rank.name = 'König'
        trumpf.rank.value = 4
        trumpf.suit.name = 'Herz'

        player_starts = False

        self._points.points_system(player_card, opponent_card, player_starts, trumpf)
        self.assertEqual('Spieler', self._points._who_won)
        self.assertEqual([player_card, opponent_card], self._points._won_cards)
        self.assertEqual(13, self._points._points_player)
        self.assertEqual(0, self._points._points_opponent)

    
    def test_pointsystem_opponent_plays_and_wins_same_colour(self):
        player_card = MagicMock()
        player_card.rank.name = 'Zehn'
        player_card.rank.value = 10
        player_card.suit.name = 'Herz'

        opponent_card = MagicMock()
        opponent_card.rank.name = 'Ass'
        opponent_card.rank.value = 11
        opponent_card.suit.name = 'Herz'
        
        trumpf = MagicMock()
        trumpf.rank.name = 'König'
        trumpf.rank.value = 4
        trumpf.suit.name = 'Herz'

        player_starts = False

        self._points.points_system(player_card, opponent_card, player_starts, trumpf)
        self.assertEqual('Gegner', self._points._who_won)
        self.assertEqual([], self._points._won_cards)
        self.assertEqual(0, self._points._points_player)
        self.assertEqual(21, self._points._points_opponent)
    

    def test_pointsystem_opponent_plays_and_wins_different_colour(self):
        player_card = MagicMock()
        player_card.rank.name = 'Ass'
        player_card.rank.value = 11
        player_card.suit.name = 'Pik'

        opponent_card = MagicMock()
        opponent_card.rank.name = 'Zehn'
        opponent_card.rank.value = 10
        opponent_card.suit.name = 'Karo'
        
        trumpf = MagicMock()
        trumpf.rank.name = 'König'
        trumpf.rank.value = 4
        trumpf.suit.name = 'Herz'

        player_starts = False

        self._points.points_system(player_card, opponent_card, player_starts, trumpf)
        self.assertEqual('Gegner', self._points._who_won)
        self.assertEqual([], self._points._won_cards)
        self.assertEqual(0, self._points._points_player)
        self.assertEqual(21, self._points._points_opponent)
     

    def test_win_counter_player_wins_3(self):
        self._points._points_player = 67
        self._points._points_opponent = 0
        score = self._points.win_counter()
        self.assertEqual([3, 0], score)
    

    def test_win_counter_player_wins_2(self):
        self._points._points_player = 67
        self._points._points_opponent = 1
        score = self._points.win_counter()
        self.assertEqual([2, 0], score)


    def test_win_counter_player_wins_1(self):
        self._points._points_player = 67
        self._points._points_opponent = 34
        score = self._points.win_counter()
        self.assertEqual([1, 0], score)

    
    def test_win_counter_opponent_wins_3(self):
        self._points._points_player = 0
        self._points._points_opponent = 67
        score = self._points.win_counter()
        self.assertEqual([0, 3], score)


    def test_win_counter_opponent_wins_2(self):
        self._points._points_player = 1
        self._points._points_opponent = 67
        score = self._points.win_counter()
        self.assertEqual([0, 2], score)


    def test_win_counter_opponent_wins_1(self):
        self._points._points_player = 34
        self._points._points_opponent = 67
        score = self._points.win_counter()
        self.assertEqual([0, 1], score)


    def test_win_counter_no_over_66_opponent_wins(self):
        self._points._points_player = 34
        self._points._points_opponent = 50
        self._points._who_won = 'Gegner'
        score = self._points.win_counter()
        self.assertEqual([0, 1], score)

    
    def test_win_counter_no_over_66_player_wins(self):
        self._points._points_player = 34
        self._points._points_opponent = 50
        self._points._who_won = 'Spieler'
        score = self._points.win_counter()
        self.assertEqual([1, 0], score)


    def test_pair_points_player_has_pair(self):
        plays_pair = True
        player_starts = True

        playcard = MagicMock()
        playcard.suit.name = 'Herz'
        
        trumpf = MagicMock()
        trumpf.suit.name = 'Karo'
        self._points.pair_points(plays_pair, player_starts, playcard, trumpf)
        self.assertEqual(20, self._points._pair_points_player)

    
    def test_pair_points_player_has_trumpf_pair(self):
        plays_pair = True
        player_starts = True

        playcard = MagicMock()
        playcard.suit.name = 'Herz'
        
        trumpf = MagicMock()
        trumpf.suit.name = 'Herz'
        self._points.pair_points(plays_pair, player_starts, playcard, trumpf)
        self.assertEqual(40, self._points._pair_points_player)
    

    def test_pair_points_opponent_has_pair(self):
        plays_pair = True
        player_starts = False

        playcard = MagicMock()
        playcard.suit.name = 'Herz'
        
        trumpf = MagicMock()
        trumpf.suit.name = 'Karo'
        self._points.pair_points(plays_pair, player_starts, playcard, trumpf)
        self.assertEqual(20, self._points._pair_points_opponent)

    
    def test_pair_points_opponent_has_trumpf_pair(self):
        plays_pair = True
        player_starts = False

        playcard = MagicMock()
        playcard.suit.name = 'Herz'
        
        trumpf = MagicMock()
        trumpf.suit.name = 'Herz'
        self._points.pair_points(plays_pair, player_starts, playcard, trumpf)
        self.assertEqual(40, self._points._pair_points_opponent)

    
    def test_adding_pair_points_no_points(self):
        self._points._points_player = 0
        self._points._pair_points_player = 20
        self._points._points_opponent = 0
        self._points._pair_points_opponent = 20

        self._points.adding_pair_points()
        self.assertEqual(0, self._points._points_player)
        self.assertEqual(0, self._points._points_opponent)
    
    def test_adding_pair_points(self):
        self._points._points_player = 1
        self._points._pair_points_player = 40
        self._points._points_opponent = 13
        self._points._pair_points_opponent = 20

        self._points.adding_pair_points()
        self.assertEqual(41, self._points._points_player)
        self.assertEqual(33, self._points._points_opponent)
    












if __name__ == '__main__':
    unittest.main()