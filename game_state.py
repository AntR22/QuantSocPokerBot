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