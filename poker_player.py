from game_state import game_state

class poker_player:
    def __init__(self):
        self.name = "none"

    def decide_action(self, game_state): 
        """
        Method to decide the bot's next action.
        Must be implemented by all bots.
        
        Parameters:
        - gamestate: 
        
        Returns:
        -   action: A tuple (action_type, amount), where action_type is one of 
            'fold', 'check', 'call' or 'raise', and amount is the bet amount if raising (excluding current bet).
        -   set amount to 0 if folding, checking or calling. Upon raising, make sure the raise amount value is greater than 
            minbet found in the gamestate and not greater than your current stack 
        """
        raise NotImplementedError("This method must be implemented by subclasses")
    
    def get_name(self):
        return self.name