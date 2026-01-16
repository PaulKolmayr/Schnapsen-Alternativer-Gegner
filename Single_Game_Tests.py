"""
Docstring for Single_Game_Tests
"""

import unittest
from unittest.mock import MagicMock, patch
from Single_Game import SingleGame as Game

class TestSingleGame(unittest.TestCase):


    @patch('builtins.input', return_value = 'Gegner')
    @patch('Single_Game.Cards')
    @patch('Single_Game.Rules.who_starts', return_value = True)
    def test_game_start(self, mock_rules, mock_cards, mock_input):
        game = Game()

        test_card_instance = mock_cards.return_value
        trumpf = MagicMock()
        trumpf.rank.name = 'Ass'
        trumpf.suit.name = 'Herz'
        test_card_instance.draw.return_value = trumpf

        game.game_start()
        self.assertEqual(5, len(game._player._hand))
        self.assertEqual(5, len(game._opponent._hand))
        self.assertEqual(trumpf, game._trumpf)
        self.assertEqual(game._player_starts, True)
    

    @patch('Single_Game.Cards')
    def test_trumpf_switch(self, mock_cards):
        game = Game()

        card_1 = MagicMock()
        card_1.rank.name = 'Ass'
        card_1.suit.name = 'Herz'

        card_2 = MagicMock()
        card_2.rank.name = 'Bube'
        card_2.suit.name = 'Herz'

        card_3 = MagicMock()
        card_3.rank.name = 'König'
        card_3.suit.name = 'Pik' 

        cards = [card_1, card_2, card_3]
        game._player._hand = cards

        trumpf = MagicMock()
        trumpf.rank.name = 'Ass'
        trumpf.suit.name = 'Herz'

        game._trumpf = trumpf

        with patch('Single_Game.Rules.can_trumpf_be_switched', return_value=True), patch('Single_Game.Controls.switch_trumpf', return_value=True), patch('Single_Game.Player.switch_trumpf', return_value=True):
            game.trumpf_switch()

        self.assertIn(trumpf, game._player._hand)


    @patch('Single_Game.Cards')
    def test_player_closes_deck(self, mock_cards):

        game = Game()
        game._deck_closed = False

        with patch('Single_Game.Controls.close_the_deck', return_value = 'Ja'), patch('Single_Game.Rules.zudrehen', return_value = True):
            game.player_closes_the_deck()
        
        self.assertEqual(game._deck_closed, True)


    @patch('Single_Game.Cards')
    def test_playing_a_pair(self, mock_cards):

        game = Game()
        
        card_1 = MagicMock()
        card_1.rank.name = 'Ass'
        card_1.suit.name = 'Herz'

        card_2 = MagicMock()
        card_2.rank.name = 'Dame'
        card_2.suit.name = 'Pik'

        card_3 = MagicMock()
        card_3.rank.name = 'König'
        card_3.suit.name = 'Pik' 

        cards = [card_1, card_2, card_3]
        game._player._hand = cards
        control = [card_2, card_3]

        with patch('Single_Game.Controls.pair_can_be_played', return_value = 'Ja'):
            game.player_thinks_about_playing_a_pair()
        
        self.assertEqual(game._player._playable, control)
        self.assertTrue(game._player._plays_pair)
        
    
    @patch('Single_Game.Cards')
    def test_able_to_play_more_pairs(self, mock_cards):

        game = Game()
        
        card_1 = MagicMock()
        card_1.rank.name = 'Ass'
        card_1.suit.name = 'Herz'

        card_2 = MagicMock()
        card_2.rank.name = 'Dame'
        card_2.suit.name = 'Pik'

        card_3 = MagicMock()
        card_3.rank.name = 'König'
        card_3.suit.name = 'Pik' 

        card_4 = MagicMock()
        card_4.rank.name = 'König'
        card_4.suit.name = 'Herz'

        card_5 = MagicMock()
        card_5.rank.name = 'Dame'
        card_5.suit.name = 'Herz'

        #pairs = [[card_2, card_3], [card_4, card_5]]
        cards = [card_1, card_2, card_3, card_4, card_5]
        game._player._hand = cards
        control = [card_2, card_3]

        with patch('Single_Game.Controls.pair_can_be_played', return_value = 'Ja'), patch('Single_Game.Controls.more_pairs_can_be_played', return_value = 'Pik'):
            game.player_thinks_about_playing_a_pair()
        
        self.assertEqual(control, game._player._playable)
        self.assertTrue(game._player._plays_pair)
    

    @patch('Single_Game.Cards')
    def test_play_no_pair(self, mock_cards):
        game = Game()
        
        card_1 = MagicMock()
        card_1.rank.name = 'Ass'
        card_1.suit.name = 'Herz'

        card_2 = MagicMock()
        card_2.rank.name = 'Dame'
        card_2.suit.name = 'Karo'

        card_3 = MagicMock()
        card_3.rank.name = 'König'
        card_3.suit.name = 'Pik' 

        cards = [card_1, card_2, card_3]
        game._player._hand = cards

        game.player_thinks_about_playing_a_pair()

        self.assertEqual(game._player._hand, game._player._playable)


    @patch('Single_Game.Cards')
    def test_player_plays_first(self, mock_cards):

        game = Game()

        card_1 = MagicMock()
        card_1.rank.name = 'Ass'
        card_1.rank.value = 11
        card_1.suit.name = 'Kreuz'

        card_2 = MagicMock()
        card_2.rank.name = 'König'
        card_2.rank.value = 4
        card_2.suit.name = 'Kreuz'

        trumpf = MagicMock()
        trumpf.rank.name = 'Zehn'
        trumpf.rank.value = 10
        trumpf.suit.name = 'Karo'

        game._player._hand = [card_1]
        game._player._playable = [card_1]
        game._opponent._hand = [card_2]
        game._opponent._playable = [card_2]
        game._battleground = []
        game._deck_closed = False
        game._trumpf = trumpf

        game._controls.which_card_to_play = MagicMock(return_value = card_1)
        game._player.plays_card = MagicMock(return_value = card_1)
        game._rules.legality_play = MagicMock(return_value = True)

        game._opponent.plays_second = MagicMock(return_value = card_2)

        game.player_plays_in_front()

        self.assertIn(card_1, game._battleground)
        self.assertIn(card_2, game._battleground)
        self.assertNotIn(card_1, game._player._hand)
        self.assertNotIn(card_2, game._opponent._hand)
        self.assertEqual(card_1, game._player_card)
        self.assertEqual(card_2, game._opponent_card)
    

    @patch('Single_Game.Cards')
    def test_opponent_plays_first(self, mock_cards):

        game = Game()

        card_1 = MagicMock()
        card_1.rank.name = 'Ass'
        card_1.rank.value = 11
        card_1.suit.name = 'Kreuz'

        card_2 = MagicMock()
        card_2.rank.name = 'König'
        card_2.rank.value = 4
        card_2.suit.name = 'Kreuz'

        trumpf = MagicMock()
        trumpf.rank.name = 'Zehn'
        trumpf.rank.value = 10
        trumpf.suit.name = 'Karo'

        game._player._hand = [card_1]
        game._player._playable = [card_1]
        game._opponent._hand = [card_2]
        game._opponent._playable = [card_2]
        game._battleground = []
        game._deck_closed = False
        game._trumpf = trumpf

        game._opponent.plays_first = MagicMock(return_value = card_2)

        game._controls.which_card_to_play = MagicMock(return_value = card_1)
        game._player.plays_card = MagicMock(return_value = card_1)
        game._rules.legality_play = MagicMock(return_value = True)

        game.player_plays_in_front()

        self.assertIn(card_1, game._battleground)
        self.assertIn(card_2, game._battleground)
        self.assertNotIn(card_1, game._player._hand)
        self.assertNotIn(card_2, game._opponent._hand)
        self.assertEqual(card_1, game._player_card)
        self.assertEqual(card_2, game._opponent_card)
    

    @patch('Single_Game.Cards')
    def test_drawing_after_play_player_first(self, mock_cards):
        
        game = Game()

        game._points._who_won = 'Spieler'

        card_1 = MagicMock()
        card_1.rank.name = 'Ass'
        card_1.rank.value = 11
        card_1.suit.name = 'Kreuz'

        card_2 = MagicMock()
        card_2.rank.name = 'König'
        card_2.rank.value = 4
        card_2.suit.name = 'Kreuz'

        trumpf = MagicMock()
        trumpf.rank.name = 'Ass'
        trumpf.rank.value = 11
        trumpf.suit.name = 'Herz'

        game._cards.draw.side_effect = [card_1, card_2]
        game._cards._deck = [card_1, card_2]
        game._trumpf = trumpf
        game._deck_closed = False

        game._player._hand = []
        game._opponent._hand = []

        game._rules.deck_empty = MagicMock(return_value=False)

        game.drawing_cards_after_round()

        self.assertTrue(game._player_starts)
        self.assertIn(card_1, game._player._hand)
        self.assertIn(card_2, game._opponent._hand)
    

    @patch('Single_Game.Cards')
    def test_drawing_after_play_opponent_first(self, mock_cards):
        
        game = Game()

        game._points._who_won = 'Gegner'

        card_1 = MagicMock()
        card_1.rank.name = 'Ass'
        card_1.rank.value = 11
        card_1.suit.name = 'Kreuz'

        card_2 = MagicMock()
        card_2.rank.name = 'König'
        card_2.rank.value = 4
        card_2.suit.name = 'Kreuz'

        trumpf = MagicMock()
        trumpf.rank.name = 'Ass'
        trumpf.rank.value = 11
        trumpf.suit.name = 'Herz'

        game._cards.draw.side_effect = [card_1, card_2]
        game._cards._deck = [card_1, card_2]
        game._trumpf = trumpf
        game._deck_closed = False

        game._player._hand = []
        game._opponent._hand = []

        game._rules.deck_empty = MagicMock(return_value=False)

        game.drawing_cards_after_round()

        self.assertFalse(game._player_starts)
        self.assertIn(card_2, game._player._hand)
        self.assertIn(card_1, game._opponent._hand)
    

if __name__ == '__main__':
    unittest.main()