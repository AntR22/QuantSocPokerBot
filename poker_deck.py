import random

class poker_deck():
    def __init__(self, pretty: bool):
        if pretty:
            suits = ["♠️", "♥️", "♦️", "♣️"]
        else:
            suits = ["s", "h", "d", "c"]
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        
        deck = []
        
        for i in suits:
            for j in ranks:
                deck.append(j+i)

        self.deck = deck
    
    def get_rand_card(self):
        """
            returns card without replacement
        Returns:
            _type_: _description_
        """
        card = self.deck[random.randint(0, len(self.deck) - 1)]
        self.deck.remove(card)
        return card
        
    def burn_card(self):
        card = self.deck[random.randint(0, len(self.deck) - 1)]
        self.deck.remove(card)

    def get_deck(self):
        return self.deck