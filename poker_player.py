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
            If you check when the opponent has raised, you will be auto folded.
        -   amount: amount is the bet amount if raising (excluding your current bet). Set amount to 0 if folding, checking
            or calling. Upon raising, make sure the raise amount value is greater than minbet(unless all in) found in the gamestate 
            and not greater than your current stack. To call DO NOT put an amount, you will automatically be matched to your opponents
            bet, if you cannot match your opponents bet you will be called 'all in' (the rest of your stack), the backend will adjust
            the opposing bet to match yours (a shove). (No sidepots due to it being a 1v1)
            Likewise if you raise above the remaining chips the opponent has left then your bet will be curtailed and returned to stack.
        """
        raise NotImplementedError("This method must be implemented by subclasses")
    
    def get_name(self):
        return self.name