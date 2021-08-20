import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self): 
        self.card1 = Card("Spades", 1)
        self.card2 = Card("Hearts", 2)
        self.cards_total = [self.card1, self.card2]
        
    def test_highest_card(self):
        self.assertEqual(True,CardGame.check_for_ace(self, self.card1))

    def test_highest_card_False(self):
        self.assertEqual(False,CardGame.check_for_ace(self, self.card2))
    
    def test_highest_card1(self):
        self.assertEqual(self.card2, CardGame.highest_card(self, self.card1, self.card2))

    def test_cards_total(self):
        self.assertEqual("You have a total of 3", CardGame.cards_total(self, self.cards_total))
