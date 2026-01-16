"""
Docstring for Card_Properties_Tests
"""

import unittest
from Card_Properties import Deck as Deck

class TestCards(unittest.TestCase):

    def test_deck_length(self):
        cards = Deck()
        self.assertEqual(20, len(cards._deck))
    
    def test_deck_individuality(self):
        cards = Deck()
        original_cards = cards._deck
        unique_cards = set(original_cards)
        self.assertEqual(len(original_cards), len(unique_cards))
    
   

if __name__ == '__main__':
    unittest.main()
    
