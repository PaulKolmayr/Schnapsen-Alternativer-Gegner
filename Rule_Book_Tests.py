"""
Docstring for Rule_Book_Tests
"""
import unittest
from unittest.mock import MagicMock, patch
from Rule_Book import RuleBook as Rules

class TestRuleBook(unittest.TestCase):

    def setUp(self):
        self._cards_test = MagicMock()
        self._rules = Rules(self._cards_test)
        

    def test_deck_empty(self):
        self._cards_test._deck = []
        self.assertTrue(self._rules.deck_empty())

    
    def test_deck_not_empty(self):
        self._cards_test._deck = ['Herz Ass']
        self.assertFalse(self._rules.deck_empty())


    def test_zudrehen_yes(self):
        zudrehen = 'Ja'
        self.assertTrue(self._rules.zudrehen(zudrehen))

    
    def test_who_starts(self):
        who_starts = 'Gegner'
        self.assertTrue(self._rules.who_starts(who_starts))

    
    def test_trumpf_can_be_switched(self):
        trumpf = MagicMock()
        trumpf.rank.name = 'Ass'
        trumpf.suit.name = 'Herz'

        card = MagicMock()
        card.rank.name = 'Bube'
        card.suit.name = 'Herz'
        hand = [card]

        self._cards_test._deck = ['Pik König', 'Pik Dame']
        self.assertTrue(self._rules.can_trumpf_be_switched(hand, trumpf))

    
    def test_pair_can_be_played(self):
        first_card = MagicMock()
        first_card.rank.name = 'Dame'
        first_card.suit.name = 'Herz'

        second_card = MagicMock()
        second_card.rank.name = 'König'
        second_card.suit.name = 'Herz'

        hand = [first_card, second_card]
        pairs = self._rules.can_pair_be_played(hand)

        self.assertEqual( pairs[0], [first_card, second_card])
    

    def test_more_pairs(self):
        first_card = MagicMock()
        first_card.rank.name = 'Dame'
        first_card.suit.name = 'Herz'

        second_card = MagicMock()
        second_card.rank.name = 'König'
        second_card.suit.name = 'Herz'

        card_3 = MagicMock()
        card_3.rank.name = 'König'
        card_3.suit.name = 'Pik'

        card_4 = MagicMock()
        card_4.rank.name = 'Dame'
        card_4.suit.name = 'Pik'

        hand = [first_card, second_card, card_3, card_4]
        pairs = self._rules.can_pair_be_played(hand)

        self.assertEqual(pairs[0], [first_card, second_card])
        self.assertIn([first_card, second_card], pairs)
        self.assertIn([card_4, card_3], pairs)
        self.assertEqual(2, len(pairs))
    
    def test_legal_play(self):
        playable_card = MagicMock()
        playable_card.rank.name = 'Ass'
        playable_card.suit.name = 'Herz'

        playable = [playable_card]

        card = playable_card

        self.assertTrue(self._rules.legality_play(card, playable))

    
    def test_illegal_play(self):
        playable_card = MagicMock()
        playable_card.rank.name = 'Ass'
        playable_card.suit.name = 'Herz'

        playable = [playable_card]

        card = MagicMock()
        card.rank.name = 'Zehn'
        card.suit.name = 'Herz'

        self.assertFalse(self._rules.legality_play(card, playable))


if __name__ =='__main__':
    unittest.main()