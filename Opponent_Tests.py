"""
Docstring for Opponent_Tests
"""

import unittest
from unittest.mock import MagicMock, patch
from Opponent import Opponent as Opponent

class TestOpponent(unittest.TestCase):

    def setUp(self):
        self._cards_test = MagicMock()
        self._opponent = Opponent(self._cards_test)

    
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

        self._opponent.first_draw()       
        
        self.assertEqual(5, len(self._opponent._hand))
        self.assertEqual(cards, self._opponent._hand)


    def test_normal_draw(self):
        trumpf = MagicMock()
        trumpf.rank.name = 'Ass'
        trumpf.suit.name = 'Herz'

        card = MagicMock()
        card.rank.name = 'Bube'
        card.suit.name = 'Herz'

        self._cards_test._deck = [card]
        self._cards_test.draw.return_value = card

        self._opponent.normal_draw(trumpf)

        self.assertIn(card, self._opponent._hand)

    
    def test_switches_trumpf(self):
        trumpf = MagicMock()
        trumpf.rank.name = 'Ass'
        trumpf.suit = 'Herz'

        card_1 = MagicMock()
        card_1.rank.name = 'Bube'
        card_1.suit = 'Herz'

        card_2 = MagicMock()
        card_2.rank.name = 'Dame'
        card_2.suit = 'Herz'

        card_3 = MagicMock()
        card_3.rank.name = 'König'
        card_3.suit = 'Pik' 

        cards = [card_1, card_2, card_3]
        self._opponent._hand = cards

        switch = self._opponent.switches_trumpf(trumpf)
        self.assertEqual(card_1, switch)
        self.assertIn(trumpf, self._opponent._hand)
    

    def test_cant_switch_trumpf(self):
        trumpf = MagicMock()
        trumpf.rank.name = 'Ass'
        trumpf.suit.name = 'Herz'

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
        self._opponent._hand = cards

        switch = self._opponent.switches_trumpf(trumpf)
        self.assertEqual(trumpf, switch)
        self.assertNotIn(trumpf, self._opponent._hand)


    def test_plays_first_one_pair(self):
        card_1 = MagicMock()
        card_1.rank.name = 'König'
        card_1.rank.value = 4
        card_1.suit.name = 'Herz'

        card_2 = MagicMock()
        card_2.rank.name = 'Dame'
        card_2.rank.value = 3
        card_2.suit.name = 'Herz'

        card_3 = MagicMock()
        card_3.rank.name = 'König'
        card_3.rank.value = 4
        card_3.suit.name = 'Pik'

        trumpf = MagicMock()
        trumpf.rank.name = 'Ass'
        trumpf.rank.value = 11
        trumpf.suit.name = 'Herz'

        cards = [card_1, card_2, card_3]
        self._opponent._hand = cards
        control = [card_1, card_2]
        points = 20

        played = self._opponent.plays_first(points, trumpf)
        self.assertEqual(card_2, played)
        self.assertTrue(self._opponent._plays_pair)
        self.assertNotIn(card_2, self._opponent._hand)


    def test_plays_first_multiple_pairs(self):
        card_1 = MagicMock()
        card_1.rank.name = 'König'
        card_1.rank.value = 4
        card_1.suit.name = 'Herz'

        card_2 = MagicMock()
        card_2.rank.name = 'Dame'
        card_2.rank.value = 3
        card_2.suit.name = 'Herz'

        card_3 = MagicMock()
        card_3.rank.name = 'König'
        card_3.rank.value = 4
        card_3.suit.name = 'Pik'

        card_4 = MagicMock()
        card_4.rank.name = 'Dame'
        card_4.rank.value = 3
        card_4.suit.name = 'Pik'

        card_5 = MagicMock()
        card_5.rank.name = 'Ass'
        card_5.rank.value = 11
        card_5.suit.name = 'Karo'

        trumpf = MagicMock()
        trumpf.rank.name = 'Ass'
        trumpf.rank.value = 11
        trumpf.suit.name = 'Herz'

        cards = [card_1, card_2, card_3, card_4, card_5]
        self._opponent._hand = cards
        points = 20

        played = self._opponent.plays_first(points, trumpf)
        self.assertEqual(card_2, played)
        self.assertTrue(self._opponent._plays_pair)
        self.assertNotIn(played, self._opponent._hand)
    

    def test_op_has_trumpf_pair_no_points(self):

        card_1 = MagicMock()
        card_1.rank.name = 'König'
        card_1.rank.value = 4
        card_1.suit.name = 'Herz'

        card_2 = MagicMock()
        card_2.rank.name = 'Dame'
        card_2.rank.value = 3
        card_2.suit.name = 'Herz'

        card_3 = MagicMock()
        card_3.rank.name = 'König'
        card_3.rank.value = 4
        card_3.suit.name = 'Pik'

        card_4 = MagicMock()
        card_4.rank.name = 'Dame'
        card_4.rank.value = 3
        card_4.suit.name = 'Pik'

        card_5 = MagicMock()
        card_5.rank.name = 'Ass'
        card_5.rank.value = 11
        card_5.suit.name = 'Karo'

        trumpf = MagicMock()
        trumpf.rank.name = 'Ass'
        trumpf.rank.value = 11
        trumpf.suit.name = 'Herz'

        cards = [card_1, card_2, card_3, card_4, card_5]
        self._opponent._hand = cards
        points = 0

        played = self._opponent.plays_first(points, trumpf)
        self.assertEqual(card_2, played)
        self.assertTrue(self._opponent._plays_pair)
        self.assertNotIn(played, self._opponent._hand)

    
    def test_opponent_doesnt_play_pair_he_has(self):
        
        card_1 = MagicMock()
        card_1.rank.name = 'König'
        card_1.suit.name = 'Herz'

        card_2 = MagicMock()
        card_2.rank.name = 'Dame'
        card_2.suit.name = 'Herz'

        card_3 = MagicMock()
        card_3.rank.name = 'König'
        card_3.suit.name = 'Pik'

        trumpf = MagicMock()
        trumpf.rank.name = 'Ass'
        trumpf.suit.name = 'Karo'

        cards = [card_1, card_2, card_3]
        self._opponent._hand = cards
        control = [card_1, card_2]
        points = 0

        played = self._opponent.plays_first(points, trumpf)
        self.assertEqual(card_3, played)
        self.assertFalse(self._opponent._plays_pair)
        self.assertNotIn(card_3, self._opponent._hand)


    def test_plays_no_pair(self):
        card_1 = MagicMock()
        card_1.rank.name = 'Zehn'
        card_1.rank.value = 10
        card_1.suit.name = 'Herz'

        card_2 = MagicMock()
        card_2.rank.name = 'Dame'
        card_2.rank.value = 3
        card_2.suit.name = 'Herz'

        card_3 = MagicMock()
        card_3.rank.name = 'Zehn'
        card_3.rank.value = 10
        card_3.suit.name = 'Pik'

        card_4 = MagicMock()
        card_4.rank.name = 'Dame'
        card_4.rank.value = 3
        card_4.suit.name = 'Pik'

        card_5 = MagicMock()
        card_5.rank.name = 'Ass'
        card_5.rank.value = 11
        card_5.suit.name = 'Karo'

        trumpf = MagicMock()
        trumpf.rank.name = 'Ass'
        trumpf.rank.value = 11
        trumpf.suit.name = 'Herz'

        cards = [card_1, card_2, card_3, card_4, card_5]
        self._opponent._hand = cards
        points = 20

        played = self._opponent.plays_first(points, trumpf)
        self.assertEqual(card_4, played)
        self.assertFalse(self._opponent._plays_pair)
        self.assertNotIn(played, self._opponent._hand)
    

    def test_opponent_plays_first_no_pair_enough_points(self):

        card_1 = MagicMock()
        card_1.rank.name = 'Zehn'
        card_1.rank.value = 10
        card_1.suit.name = 'Karo'

        card_2 = MagicMock()
        card_2.rank.name = 'Bube'
        card_2.rank.value = 2
        card_2.suit.name = 'Herz'

        card_3 = MagicMock()
        card_3.rank.name = 'König'
        card_3.rank.value = 4
        card_3.suit.name = 'Herz'

        card_4 = MagicMock()
        card_4.rank.name = 'Dame'
        card_4.rank.value = 3
        card_4.suit.name = 'Pik'

        card_5 = MagicMock()
        card_5.rank.name = 'Ass'
        card_5.rank.value = 11
        card_5.suit.name = 'Karo'

        trumpf = MagicMock()
        trumpf.rank.name = 'Ass'
        trumpf.rank.value = 11
        trumpf.suit.name = 'Herz'

        cards = [card_1, card_2, card_3, card_4, card_5]
        self._opponent._hand = cards
        points = 63

        played = self._opponent.plays_first(points, trumpf)
        self.assertEqual(card_3, played)
        self.assertFalse(self._opponent._plays_pair)
        self.assertNotIn(played, self._opponent._hand)


    def test_plays_second_open_can_win(self):
        trumpf = MagicMock()
        trumpf.rank.name = 'Ass'
        trumpf.rank.value = 11
        trumpf.suit.name = 'Karo'

        player_card = MagicMock()
        player_card.rank.name = 'König'
        player_card.rank.value = 4
        player_card.suit.name = 'Herz'

        zugedreht = False

        card_1 = MagicMock()
        card_1.rank.name = 'Ass'
        card_1.rank.value = 11
        card_1.suit.name = 'Herz'

        card_2 = MagicMock()
        card_2.rank.name = 'Zehn'
        card_2.rank.value = 10
        card_2.suit.name = 'Herz'

        card_3 = MagicMock()
        card_3.rank.name = 'König'
        card_3.rank.value = 4
        card_3.suit.name = 'Pik' 

        cards = [card_1, card_2, card_3]
        self._opponent._hand = cards

        played = self._opponent.plays_second(zugedreht, player_card, trumpf)
        self.assertEqual(card_2, played)


    def test_plays_second_open_cant_win(self):
        trumpf = MagicMock()
        trumpf.rank.name = 'Ass'
        trumpf.rank.value = 11
        trumpf.suit.name = 'Karo'

        player_card = MagicMock()
        player_card.rank.name = 'Zehn'
        player_card.rank.value = 10
        player_card.suit.name = 'Karo'

        zugedreht = False

        card_1 = MagicMock()
        card_1.rank.name = 'Ass'
        card_1.rank.value = 11
        card_1.suit.name = 'Herz'

        card_2 = MagicMock()
        card_2.rank.name = 'Zehn'
        card_2.rank.value = 10
        card_2.suit.name = 'Herz'

        card_3 = MagicMock()
        card_3.rank.name = 'König'
        card_3.rank.value = 4
        card_3.suit.name = 'Pik' 

        cards = [card_1, card_2, card_3]
        self._opponent._hand = cards

        played = self._opponent.plays_second(zugedreht, player_card, trumpf)
        self.assertEqual(card_3, played)


    def test_plays_second_closed_can_win(self):
        trumpf = MagicMock()
        trumpf.rank.name = 'Ass'
        trumpf.rank.value = 11
        trumpf.suit.name = 'Karo'

        player_card = MagicMock()
        player_card.rank.name = 'Dame'
        player_card.rank.value = 3
        player_card.suit.name = 'Herz'

        zugedreht = True

        card_1 = MagicMock()
        card_1.rank.name = 'Ass'
        card_1.rank.value = 11
        card_1.suit.name = 'Herz'

        card_2 = MagicMock()
        card_2.rank.name = 'Zehn'
        card_2.rank.value = 10
        card_2.suit.name = 'Herz'

        card_3 = MagicMock()
        card_3.rank.name = 'König'
        card_3.rank.value = 4
        card_3.suit.name = 'Karo' 

        cards = [card_1, card_2, card_3]
        self._opponent._hand = cards

        played = self._opponent.plays_second(zugedreht, player_card, trumpf)
        self.assertEqual(card_2, played)


    def test_plays_second_closed_cant_win(self):
        trumpf = MagicMock()
        trumpf.rank.name = 'Ass'
        trumpf.rank.value = 11
        trumpf.suit.name = 'Karo'

        player_card = MagicMock()
        player_card.rank.name = 'Dame'
        player_card.rank.value = 3
        player_card.suit.name = 'Karo'

        zugedreht = True

        card_1 = MagicMock()
        card_1.rank.name = 'Ass'
        card_1.rank.value = 11
        card_1.suit.name = 'Herz'

        card_2 = MagicMock()
        card_2.rank.name = 'Bube'
        card_2.rank.value = 2
        card_2.suit.name = 'Kreuz'

        card_3 = MagicMock()
        card_3.rank.name = 'König'
        card_3.rank.value = 4
        card_3.suit.name = 'Pik' 

        cards = [card_1, card_2, card_3]
        self._opponent._hand = cards

        played = self._opponent.plays_second(zugedreht, player_card, trumpf)
        self.assertEqual(card_2, played)


    def test_worth_system(self):

        card_1 = MagicMock()
        card_1.rank.name = 'Ass'
        card_1.rank.value = 11
        card_1.suit.name = 'Herz'

        card_2 = MagicMock()
        card_2.rank.name = 'Zehn'
        card_2.rank.value = 10
        card_2.suit.name = 'Herz'

        card_3 = MagicMock()
        card_3.rank.name = 'König'
        card_3.rank.value = 4
        card_3.suit.name = 'Herz'

        trumpf = MagicMock()
        trumpf.rank.name = 'Bube'
        trumpf.rank.value = 2
        trumpf.suit.name = 'Herz'

        cards = [card_1, card_3]
        self._opponent._hand = cards
        played_cards = [card_2]
        value = self._opponent.dynamic_value(trumpf, played_cards)
        self.assertEqual({card_1: 0, card_3: 0.4}, value)


    def test_risk_system_late_game(self):

        card_1 = MagicMock()
        card_1.rank.name = 'Ass'
        card_1.rank.value = 11
        card_1.suit.name = 'Herz'

        card_2 = MagicMock()
        card_2.rank.name = 'Zehn'
        card_2.rank.value = 10
        card_2.suit.name = 'Herz'

        card_3 = MagicMock()
        card_3.rank.name = 'König'
        card_3.rank.value = 4
        card_3.suit.name = 'Herz'

        card_4 = MagicMock()
        card_4.rank.name = 'König'
        card_4.rank.value = 4
        card_4.suit.name = 'Karo'

        card_5 = MagicMock()
        card_5.rank.name = 'Bube'
        card_5.rank.value = 2
        card_5.suit.name = 'Pik'

        card_6 = MagicMock()
        card_6.rank.name = 'König'
        card_6.rank.value = 4
        card_6.suit.name = 'Kreuz'

        trumpf = MagicMock()
        trumpf.rank.name = 'Bube'
        trumpf.rank.value = 2
        trumpf.suit.name = 'Herz'

        deck = [card_1, card_3]
        playerhand = [card_5, card_6]
        cards = [card_2, card_4]
        self._opponent._hand = cards
        value = self._opponent.risk_system_late_game(trumpf, deck, playerhand)
        self.assertEqual({card_2: 3/4, card_4: 2/4}, value)

    
    def test_risk_system_early_game(self):

        card_1 = MagicMock()
        card_1.rank.name = 'Ass'
        card_1.rank.value = 11
        card_1.suit.name = 'Herz'

        card_2 = MagicMock()
        card_2.rank.name = 'Zehn'
        card_2.rank.value = 10
        card_2.suit.name = 'Herz'

        card_3 = MagicMock()
        card_3.rank.name = 'König'
        card_3.rank.value = 4
        card_3.suit.name = 'Herz'

        card_4 = MagicMock()
        card_4.rank.name = 'König'
        card_4.rank.value = 4
        card_4.suit.name = 'Karo'

        card_5 = MagicMock()
        card_5.rank.name = 'Bube'
        card_5.rank.value = 2
        card_5.suit.name = 'Pik'

        card_6 = MagicMock()
        card_6.rank.name = 'König'
        card_6.rank.value = 4
        card_6.suit.name = 'Kreuz'

        trumpf = MagicMock()
        trumpf.rank.name = 'Bube'
        trumpf.rank.value = 2
        trumpf.suit.name = 'Herz'

        deck = [card_1, card_3]
        playerhand = [card_5, card_6]
        cards = [card_2, card_4]
        self._opponent._hand = cards
        value = self._opponent.risk_system_early_game(trumpf, deck, playerhand)
        self.assertEqual({card_2: 3/4, card_4: 1.0}, value)


    def test_part_of_pair(self):

        card_1 = MagicMock()
        card_1.rank.name = 'Ass'
        card_1.rank.value = 11
        card_1.suit.name = 'Herz'

        card_2 = MagicMock()
        card_2.rank.name = 'Dame'
        card_2.rank.value = 2
        card_2.suit.name = 'Herz'

        card_3 = MagicMock()
        card_3.rank.name = 'König'
        card_3.rank.value = 4
        card_3.suit.name = 'Herz'

        card_4 = MagicMock()
        card_4.rank.name = 'König'
        card_4.rank.value = 4
        card_4.suit.name = 'Karo'

        card_5 = MagicMock()
        card_5.rank.name = 'Dame'
        card_5.rank.value = 3
        card_5.suit.name = 'Karo'

        trumpf = MagicMock()
        trumpf.rank.name = 'Bube'
        trumpf.rank.value = 2
        trumpf.suit.name = 'Herz'

        cards = [card_1, card_2, card_3,card_4, card_5]
        self._opponent._hand = cards
        value = self._opponent.part_of_pair(trumpf)
        self.assertEqual({card_1: 0, card_2: 1.0, card_3:1.0, card_4: 0.5, card_5: 0.5}, value)


    def test_pair_possibility(self):

        card_1 = MagicMock()
        card_1.rank.name = 'König'
        card_1.rank.value = 4
        card_1.suit.name = 'Kreuz'

        card_2 = MagicMock()
        card_2.rank.name = 'Dame'
        card_2.rank.value = 3
        card_2.suit.name = 'Herz'

        card_3 = MagicMock()
        card_3.rank.name = 'König'
        card_3.rank.value = 4
        card_3.suit.name = 'Herz'

        card_4 = MagicMock()
        card_4.rank.name = 'Zehn'
        card_4.rank.value = 10
        card_4.suit.name = 'Karo'

        card_5 = MagicMock()
        card_5.rank.name = 'Dame'
        card_5.rank.value = 3
        card_5.suit.name = 'Pik'

        card_6 = MagicMock()
        card_6.rank.name = 'Dame'
        card_6.rank.value = 3
        card_6.suit.name = 'Kreuz'

        card_7 = MagicMock()
        card_7.rank.name = 'König'
        card_7.rank.value = 4
        card_7.suit.name = 'Pik'

        trumpf = MagicMock()
        trumpf.rank.name = 'Bube'
        trumpf.rank.value = 2
        trumpf.suit.name = 'Herz'

        cards = [card_1, card_2, card_3, card_4, card_5]
        played_cards = [card_7]
        self._opponent._hand = cards
        value = self._opponent.pair_possibility(trumpf, played_cards)
        self.assertEqual({card_1: 0.5, card_2: 0, card_3: 0, card_4: 0, card_5: 0}, value)


if __name__ == '__main__':
    unittest.main()