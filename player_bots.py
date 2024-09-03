from poker_player import poker_player
from game_state import game_state

class aggressive_bot(poker_player):
    def __init__(self):
        self.name = "aggressive bot"
    
    def decide_action(self, game_state: game_state):
        return ('raise', game_state.get_min_bet())

class aggressive_bot2(poker_player):
    def __init__(self):
        self.name = "aggressive bot2"
    
    def decide_action(self, game_state: game_state):
        return ('raise', game_state.get_min_bet())

