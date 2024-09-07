from poker_game import poker_game
from player_bots import aggressive_bot, aggressive_bot2
from poker_deck import poker_deck
bot1_wins = 0
bot2_wins = 0
num_rounds_max = 7

bot1 = aggressive_bot()
bot2 = aggressive_bot2()

for i in range(0, 10):
    game = poker_game([bot1, bot2])
    game.play(num_rounds_max)
    
    winner = game.check_game_winner()
    if winner == None:
        print("No winner this round")
    elif winner == 1:
        bot1_wins += 1
        print("bot1 wins this round")
    elif winner == 2:
        bot2_wins += 1
        print("bot2 wins wins this round")
        
    print(f"Current score:\n bot1 = {bot1_wins}\n bot2 = {bot2_wins}")

if bot1_wins > bot2_wins: 
    winner = bot1.get_name() 
else: 
    winner = bot2.get_name()

print("\n\n||| WINNER |||\n  ", winner)