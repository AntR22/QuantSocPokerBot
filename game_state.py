from poker_game import poker_game
import copy

class game_state():
    def __init__(self, player_index: int, poker_game: poker_game):
        self.pot = copy.deepcopy(poker_game.pot)
        self.stacks = copy.deepcopy(poker_game.stacks)
        self.bets = copy.deepcopy(poker_game.bets)
        self.cards = copy.deepcopy(poker_game.cards[player_index])
        self.min_bet = copy.deepcopy(poker_game.min_bet)
        self.small_blind = copy.deepcopy(poker_game.small_blind)
        self.big_blind = copy.deepcopy(poker_game.big_blind)
        self.current_dealer_index = copy.deepcopy(poker_game.current_dealer_index)
        self.river = copy.deepcopy(poker_game.river)
        self.player_index = player_index
        
    def get_my_stack(self):
        return self.stacks[self.player_index]
    
    def get_opponents_stack(self):
        return self.stacks[int(not self.player_index)]
    
    def get_my_cards(self):
        return self.cards
    
    def get_min_bet(self):
        return self.min_bet
    
    def get_big_blind(self):
        return self.big_blind
    
    def get_small_blind(self):
        return self.small_blind
    
    def get_river(self):
        return self.river
    
    def get_pot(self):
        return self.pot
    
    def get_my_bet(self):
        return self.bets[self.player_index]
    
    def get_opponents_bet(self):
        return self.bets[int(not self.player_index)]
    
    def get_current_bet(self):
        opponent_bet = self.get_opponents_bet()
        my_bet = self.get_my_bet()
        return opponent_bet - my_bet if opponent_bet > my_bet else 0