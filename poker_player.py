from game_state import game_state

class poker_player:
    def __init__(self):
        """ put your name here (in the override)
        """
        self.name = "none"

    def decide_action(self, game_state: game_state): 
        """
        Method to decide the bot's next action.
        Must be implemented by all bots.
        
        Parameters:
        - gamestate: An object containing all the necessary information about the game, check methods you
          can use in the game_state file
          Inside game_state, you can use any of the methods to retrieve information needed, or access the parameters directly.
          Changing these parameters will do nothing as all are deep copies so feel free to mess around with card ordering etc.
          Cards will be an array of strings, with representation of first char rank, second char suit e.g. a river of
            - Ace of spades = "As"
            - King of clubs = "Kc"
            - Queen of hearts = "Qh"
            - Jack of clubs = "Jc"
            - 10 of diamonds = "10d"
            Would be given as ["As", "Kc", "Qh", "Jc", "10d"] 
            - if only 3 cards are on the river then ["As", "Kc", "Qh"]
            - if only 4 cards are on the river then ["As", "Kc", "Qh", "Jc"]
            A hand of
            - 3 of clubs = "3c"
            - 5 of diamonds = "5d"
            Would be given as ["3c", "5d"]
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