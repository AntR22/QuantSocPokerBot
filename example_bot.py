from poker_player import poker_player
from game_state import game_state

class example_bot(poker_player):
    def __init__(self):
        self.name = "example bot"
    
    def decide_action(self, game_state: game_state):
        current_bet = game_state.get_current_bet()

        # Check if the bot has a pair in its hand
        if self.has_pair(game_state.get_my_cards()):
            # Check player stack for raise
            if game_state.get_my_stack() >= game_state.min_bet + current_bet:
                # If the bot has a pair, it decides to raise
                return ('raise', game_state.get_min_bet())
        
        # Otherwise, the bot decides to limp (call the current bet)
        if current_bet > 0:
            return ('call', current_bet)
        else:
            return ('check', 0)  # No bet to call, just check

    def has_pair(self, cards):
        """
        Check if the bot has a pair in its hand.
        :param cards: A list of the bot's hole cards.
        :return: True if the bot has a pair, False otherwise.
        """
        # Check if the two hole cards have the same rank (pair)
        return cards[0] == cards[1]