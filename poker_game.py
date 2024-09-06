from typing import List
from poker_player import poker_player
from poker_deck import poker_deck
from game_state import game_state
import copy

class poker_game:
    """ 1v1 poker game
    """
    def __init__(self, players: List[poker_player]):
        self.pot = 0
        self.deck = None
        self.players = players
        self.stacks = [1000, 1000] 
        self.bets = [0, 0] 
        self.cards = [[None, None], [None, None]] 
        self.min_bet = 40
        self.small_blind = 20
        self.big_blind = 40
        self.current_dealer_index = 0
        self.river = []
        self.winner = None
        self.has_folded = [False, False]
    
    def do_betting_round(self, small_blind, big_blind):
        (action1, amount1) = (None, None)
        (action2, amount2) = (None, None)

        while True:
            # small blind first response
            try:
                (action1, amount1) = self.players[small_blind].decide_action(game_state(small_blind, self))
            except Exception as e:
                print("error in decide_action for player: ", self.players[small_blind].get_name(), "\n\nthe error:\n", e)
                action1 = "fold"
                
            # checks correct usage of the action string, also checks bet amount is allowed
            if action1 != "fold" and action1 != "check" and action1 != "call" and action1 != "raise":
                print("invalid action for player: ", self.players[small_blind].get_name())
                action1 = "fold"
            elif amount1 > self.stacks[small_blind]:
                print("player does not have enough chips for that bet! player: ", self.players[small_blind].get_name())
                action1 = "fold"

            if amount1 != 0 and (action1 == "fold" or action1 == "check" or action1 == "call"):
                print("invalid action (bet given on a fold or check) for player: ", self.players[small_blind].get_name())
                action1 = "fold"

            if action1 == "fold":
                self.pot = self.pot + self.bets[0] + self.bets[1]
                self.stacks[big_blind] += self.pot
                self.bets = [0, 0]
                self.pot = 0
                self.has_folded[small_blind] = True
                return False
            elif action1 == "call":
                pass
            elif action1 == "raise":
                
                pass

            if action1 == "check" and action2 == "check":
                #sanity check
                if self.bets[0] != self.bets[1]:
                    #TODO treat as auto fold
                    print("!!huge error, bets are unequal when both players have checked!!\n")
                    exit(1)
                self.pot += self.bets[0]
                self.pot += self.bets[1]
                self.bets[0] = 0
                self.bets[1] = 0
                return True
                
            # dealer second response
            try:
                (action2, amount2) = self.players[big_blind].decide_action(game_state(big_blind, self))
            except Exception as e:
                print(f"error in decide_action for player: ", self.players[small_blind].get_name(), "\n\nthe error:\n", e)
                # TODO then auto fold
                
            # checks correct usage of the action string, also checks bet amount is allowed
            if action2 != "fold" and action2 != "check" and action2 != "call" and action2 != "raise":
                print("invalid action for player: ", self.players[small_blind].get_name())
                # TODO then auto fold
            elif amount2 > self.stacks[big_blind]:
                print("player does not have enough chips for that bet! player: ", self.players[small_blind].get_name())
                # TODO then auto fold

            if amount2 != 0 and (action2 == "fold" or action2 == "check" or action2 == "call"):
                print("invalid action (bet given on a fold or check) for player: ", self.players[small_blind].get_name())
                action1 = "fold"

            if action1 == "check" and action2 == "check":
                #sanity check
                if self.bets[0] != self.bets[1]:                    
                    #TODO treat as auto fold
                    print("!!huge error, bets are unequal when both players have checked!!\n")
                    exit(1)
                self.pot += self.bets[0]
                self.pot += self.bets[1]
                self.bets[0] = 0
                self.bets[1] = 0
                return True
                
    
    def play(self, num_rounds: int):
        round_num = 1
        while (self.stacks[0] != 0 and self.stacks[1] != 0 and round_num <= num_rounds):
            # make a new instance of a shuffled deck
            self.deck = poker_deck(False)
            
            # find indices of dealer and blinds
            dealer_index = self.current_dealer_index
            small_blind = int(not dealer_index)
            big_blind = dealer_index
            
            # update stacks and pot for small and big blind
            self.stacks[small_blind] -= self.small_blind
            self.stacks[big_blind] -= self.big_blind
            self.bets[small_blind] += self.small_blind
            self.bets[big_blind] += self.big_blind
            
            # deal cards
            card1 = self.deck.get_rand_card()
            self.cards[small_blind][0] = card1

            card2 = self.deck.get_rand_card()
            self.cards[dealer_index][0] = card2
            
            card3 = self.deck.get_rand_card()
            self.cards[small_blind][1] = card3
            
            card4 = self.deck.get_rand_card()
            self.cards[dealer_index][1] = card4
            
            # Pre flop betting phase actions 
            pfresult = self.do_betting_round(small_blind, big_blind)
            
            #sanity check
            if self.bets[0] != 0 or self.bets[1] != 0:
                print("error on bets at pre flop\n")
                exit(1)
            
            # Flop phase
            # burn card before flop
            self.deck.burn_card()
            
            # flop first 3 and add to river
            river1 = self.deck.get_rand_card()
            river2 = self.deck.get_rand_card()
            river3 = self.deck.get_rand_card()
            self.river.append(river1)
            self.river.append(river2)
            self.river.append(river3)
            
            # flop betting phase actions 
            if pfresult:
                fresult = self.do_betting_round(small_blind, big_blind)

            #sanity check
            if self.bets[0] != 0 or self.bets[1] != 0:
                print("error on bets at pre flop\n")
                exit(1)
                
            # Turn phase 
            # add card to river
            self.deck.burn_card()
            turncard = self.deck.get_rand_card()
            self.river.append(turncard)
            
            # turn phase betting
            if pfresult and fresult:
                tresult = self.do_betting_round(small_blind, big_blind)

            #sanity check
            if self.bets[0] != 0 or self.bets[1] != 0:
                print("error on bets at pre flop\n")
                exit(1)
                
            # River phase 
            # add card to river
            self.deck.burn_card()
            rivercard = self.deck.get_rand_card()
            self.river.append(rivercard)
            
            # river phase betting
            if pfresult and fresult and tresult:
                rresult = self.do_betting_round(small_blind, big_blind)
                if rresult == False:
                    # TODO finish up
                    pass
            
            #sanity check
            if self.bets[0] != 0 or self.bets[1] != 0:
                print("error on bets at pre flop\n")
                exit(1)
                
            #TODO finish the round logic 
            # maybe call check_winning_hand() and fix up that function
            
            # move dealer to the other person and reset pot + cards
            self.current_dealer_index = int(not self.current_dealer_index)   
            self.river = []
            self.bets = [0, 0] 
            self.cards = [[None, None], [None, None]] 
            self.has_folded = [False, False]
            self.pot = 0
            self.deck = None
            
    def check_game_winner(self):
        if self.stacks[0] > self.stacks[1]:
            return 0
        elif self.stacks[0] < self.stacks[1]:
            return 1
        else:
            return None


def check_winning_hand(hand1, hand2, river):
    hand1_cards = copy.deepcopy(hand1 + river) # copy hand1 cards into a single array
    hand2_cards = copy.deepcopy(hand2 + river) # copy hand2 cards into a single array
    
# 9 straight flushes - ranked on high card
# 13 four of a kinds - ranked on high card
# 13 full houses - ignoring the pairs, must be checked in event the ranks are equal
# 9 flushes - ranked on high card
# 9 straights - ranked on high card
# 13 three of a kinds - ranked on high card
# 13 two pairs - ranked on high card
# 13 pairs - ranked on high card
# 13 high cards
# total hand rankings from 1 (worst) to 105 (best)
def check_hand(hand, river):
    cards = copy.deepcopy(hand + river)
            

def rank_to_num(rank):
    if rank == "A":
        return 14
    elif rank == "K":
        return 13
    elif rank == "Q":
        return 12
    elif rank == "J":
        return 11
    else:
        return int(rank)
    
def get_highest_card(cards):
    highest_card = 0
    for card in cards:
        rank = rank_to_num(card[0])
        if rank > highest_card:
            highest_card = rank
    
    return highest_card
        