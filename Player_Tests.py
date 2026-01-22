"""
Docstring for Player_Tests
"""

import unittest
from unittest.mock import MagicMock, patch
from Player import Player as Player

class TestPlayer(unittest.TestCase):

    def setUp(self):
        self._cards_test = MagicMock()
        self._player = Player(self._cards_test)


    def test_first_draw(self):
        card_1 = MagicMock()
        card_1.rank.name = 'Ass'
        card_1.suit.name = 'Herz'

        card_2 = MagicMock()
        card_2.rank.name = 'König'
        card_2.suit.name = 'Herz'

        card_3 = MagicMock()
        card_3.rank.name = 'Zehn'
        card_3.suit.name = 'Herz'

        card_4 = MagicMock()
        card_4.rank.name = 'Dame'
        card_4.suit.name = 'Herz'

        card_5 = MagicMock()
        card_5.rank.name = 'Bube'
        card_5.suit.name = 'Herz'

        cards = [card_1, card_2, card_3, card_4, card_5]
        self._cards_test.draw.side_effect = cards

        self._player.first_draw()       
        
        self.assertEqual(5, len(self._player._hand))
        self.assertEqual(cards, self._player._hand)


    def test_normal_draw(self):
        trumpf = MagicMock()
        trumpf.rank.name = 'Ass'
        trumpf.suit.name = 'Herz'

        card = MagicMock()
        card.rank.name = 'Bube'
        card.suit.name = 'Herz'

        self._cards_test._deck = [card]
        self._cards_test.draw.return_value = card

        self._player.normal_draw(trumpf)

        self.assertIn(card, self._player._hand)
    

    def test_draw_trumpf(self):
        trumpf = MagicMock()
        trumpf.rank.name = 'Ass'
        trumpf.suit.name = 'Herz'

        self._cards_test._deck = []

        self._player.normal_draw(trumpf)

        self.assertIn(trumpf, self._player._hand)


    def test_trumpf_switch(self):
        answer = 'Ja'
        self.assertTrue(self._player.switch_trumpf(answer))

    
    def test_one_pair(self):
        card_1 = MagicMock()
        card_1.rank.name = 'König'
        card_1.suit.name = 'Herz'

        card_2 = MagicMock()
        card_2.rank.name = 'Dame'
        card_2.suit.name = 'Herz'

        card_3 = MagicMock()
        card_3.rank.name = 'König'
        card_3.suit.name = 'Pik' 

        cards = [card_1, card_2, card_3]
        self._player._hand = cards

        pairs = [[card_1, card_2]]
        self._player.play_pair(pairs)
        self.assertIn(card_1, self._player._playable)
        self.assertIn(card_2, self._player._playable)
        self.assertEqual(2, len(self._player._playable))
        self.assertTrue(self._player._plays_pair)
    

    def test_more_pairs(self):

        card_1 = MagicMock()
        card_1.rank.name = 'König'
        card_1.suit.name = 'Herz'

        card_2 = MagicMock()
        card_2.rank.name = 'Dame'
        card_2.suit.name = 'Herz'

        card_3 = MagicMock()
        card_3.rank.name = 'König'
        card_3.suit.name = 'Pik' 

        card_4 = MagicMock()
        card_4.rank.name = 'Dame'
        card_4.suit.name = 'Pik'

        card_5 = MagicMock()
        card_5.rank.name = 'Ass'
        card_5.suit.name = 'Karo'

        cards = [card_1, card_2, card_3, card_4, card_5]
        self._player._hand = cards

        decision = 'Pik'

        pairs = [[card_1, card_2], [card_3, card_4]]
        self._player.plays_more_pairs(pairs, decision)
        self.assertIn(card_3, self._player._playable)
        self.assertIn(card_4, self._player._playable)
        self.assertEqual(2, len(self._player._playable))
        self.assertTrue(self._player._plays_pair)

    
    def test_wants_no_pair(self):
        card_1 = MagicMock()
        card_1.rank.name = 'König'
        card_1.suit.name = 'Herz'

        card_2 = MagicMock()
        card_2.rank.name = 'Dame'
        card_2.suit.name = 'Herz'

        card_3 = MagicMock()
        card_3.rank.name = 'König'
        card_3.suit.name = 'Pik' 

        cards = [card_1, card_2, card_3]
        self._player._hand = cards

        pairs = [[card_1, card_2]]
        self._player.plays_no_pair()
        self.assertEqual(cards, self._player._playable)
        self.assertFalse(self._player._plays_pair)


    def test_has_no_pair(self):
        card_1 = MagicMock()
        card_1.rank.name = 'Ass'
        card_1.suit.name = 'Herz'

        card_2 = MagicMock()
        card_2.rank.name = 'Dame'
        card_2.suit.name = 'Herz'

        card_3 = MagicMock()
        card_3.rank.name = 'König'
        card_3.suit.name = 'Pik' 

        cards = [card_1, card_2, card_3]
        self._player._hand = cards

        pairs = []
        self._player.plays_no_pair()
        self.assertEqual(cards, self._player._playable)
        self.assertFalse(self._player._plays_pair)

    
    def test_plays_second_open(self):
        op_card = MagicMock()
        op_card.rank.name = 'König'
        op_card.suit.name = 'Herz'

        zugedreht = False

        card_1 = MagicMock()
        card_1.rank.name = 'Ass'
        card_1.suit.name = 'Herz'

        card_2 = MagicMock()
        card_2.rank.name = 'Dame'
        card_2.suit.name = 'Herz'

        card_3 = MagicMock()
        card_3.rank.name = 'König'
        card_3.suit.name = 'Pik' 

        trumpf = MagicMock()
        trumpf.rank.name = 'König'
        trumpf.suit.name = 'Karo'

        cards = [card_1, card_2, card_3]
        self._player._hand = cards

        self._player.plays_second(op_card, zugedreht, trumpf)
        self.assertEqual(cards, self._player._playable)


    def test_plays_second_closed(self):
        op_card = MagicMock()
        op_card.rank.name = 'König'
        op_card.suit.name = 'Herz'

        zugedreht = True

        card_1 = MagicMock()
        card_1.rank.name = 'Ass'
        card_1.suit.name = 'Herz'

        card_2 = MagicMock()
        card_2.rank.name = 'Dame'
        card_2.suit.name = 'Herz'

        card_3 = MagicMock()
        card_3.rank.name = 'König'
        card_3.suit.name = 'Pik' 

        trumpf = MagicMock()
        trumpf.rank.name = 'König'
        trumpf.suit.name = 'Karo'

        cards = [card_1, card_2, card_3]
        control = [card_1, card_2]
        self._player._hand = cards

        self._player.plays_second(op_card, zugedreht, trumpf)
        self.assertEqual(control, self._player._playable)


    def test_plays_card(self):
        card_1 = MagicMock()
        card_1.rank.name = 'Ass'
        card_1.suit.name = 'Herz'

        card_2 = MagicMock()
        card_2.rank.name = 'Dame'
        card_2.suit.name = 'Herz'

        card_3 = MagicMock()
        card_3.rank.name = 'König'
        card_3.suit.name = 'Pik' 

        cards = [card_1, card_2, card_3]
        self._player._hand = cards

        decision = 'Herz Dame'

        played_card = self._player.plays_card(decision)
        self.assertEqual(card_2, played_card)


if __name__ == '__main__':
    unittest.main()