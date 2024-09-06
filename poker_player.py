from game_state import game_state

class poker_player:
    def __init__(self):
        self.name = "none"

    def decide_action(self, game_state: game_state): 
        """
        Method to decide the bot's next action.
        Must be implemented by all bots.
        
        Parameters:
        - gamestate: 
        
        Returns:
        -   action: A tuple (action_type, amount)
        -   action_type: action_type is one of 'fold', 'check', 'call' or 'raise' - anything else will be treated as fold.
        -   amount: amount is the bet amount if raising or calling (excluding your current bet). Set amount to 0 if folding or checking.
            Upon raising, make sure the raise amount value is greater than minbet(unless all in) found in the gamestate 
            and not greater than your current stack, to call DO NOT match your opponents bet UNLESS you have enough chips to do so, 
            otherwise you will be autofolded, just call 'all in' (the rest of your stack), the backend will adjust the opposing bet
            to match yours. Likewise if you raise above the remaining chips the opponent has left then your bet will be curtailed.
        """
        raise NotImplementedError("This method must be implemented by subclasses")
    
    def get_name(self):
        return self.name