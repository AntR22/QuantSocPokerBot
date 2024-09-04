from poker_player import poker_player
from game_state import game_state

# Create new bot class that inherits from poker_player
class caller_bot(poker_player):
    def __init__(self):
        self.name = "caller bot"
    
    def decide_action(self, game_state: game_state):
        # Always call the current bet
        current_bet_to_call = game_state.get_current_bet()
        if current_bet_to_call > 0:
            return ('call', current_bet_to_call)
        else:
            return ('check', 0)