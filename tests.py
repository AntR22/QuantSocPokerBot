from poker_game import *

print("\n\n|||||| test 1 for low straight ||||||")
straight = ["Ac", "2s", "3d", "4h", "5c"]
print(straight)
print("highest card:", get_highest_card(straight))
print("straight: ", check_straight(straight))
print("flush: ", check_flush(straight))
print("straight flush: ", check_straight_flush(straight))
print("4 of kind: ", check_four_of_kind(straight))
print("pairs: ", check_pairs(straight))
print("trips: ", check_trips(straight))
print("hand eval: ", check_hand(straight[0:2], straight[2:5]))

print("\n\n|||||| test 2 for pair ||||||")
straight = ["Ad", "3d", "3d", "4d", "5d", "7c"]
print(straight)
print("highest card:", get_highest_card(straight))
print("straight: ", check_straight(straight))
print("flush: ", check_flush(straight))
print("straight flush: ", check_straight_flush(straight))
print("4 of kind: ", check_four_of_kind(straight))
print("pairs: ", check_pairs(straight))
print("trips: ", check_trips(straight))
print("hand eval: ", check_hand(straight[0:2], straight[2:5]))

print("\n\n|||||| test 3 for high straight ||||||")
straight = ["Ac", "Ks", "Qd", "Jh", "10c"]
print(straight)
print("highest card:", get_highest_card(straight))
print("straight: ", check_straight(straight))
print("flush: ", check_flush(straight))
print("straight flush: ", check_straight_flush(straight))
print("4 of kind: ", check_four_of_kind(straight))
print("pairs: ", check_pairs(straight))
print("trips: ", check_trips(straight))
print("hand eval: ", check_hand(straight[0:2], straight[2:5]))

print("\n\n|||||| test 4 for mid straight ||||||")
# Test 4: Straight - 5 mid straight (3, 4, 5, 6, 7)
straight = ["7c", "6s", "3d", "4h", "5c"]
print(straight)
print("highest card:", get_highest_card(straight))  # Should return 5 (since Ace is counted as 1)
print("straight: ", check_straight(straight))      # Should return True (this is a straight)
print("flush: ", check_flush(straight))            # Should return False (not all same suit)
print("straight flush: ", check_straight_flush(straight))  # Should return False (not all same suit)
print("4 of kind: ", check_four_of_kind(straight))  # Should return False (no four of a kind)
print("pairs: ", check_pairs(straight))            # Should return 0 (no pairs)
print("trips: ", check_trips(straight))            # Should return False (no three of a kind)
print("hand eval: ", check_hand(straight[0:2], straight[2:5]))

print("\n\n|||||| test 5 for flush ||||||")
# Test 5: Flush - (all cards of same suit, but no straight)
flush_hand = ["Ad", "7c",  "3d", "4d", "5d", "7d", "5h"]
print(flush_hand)
print("highest card:", get_highest_card(flush_hand))  # Should return Ace (A is high)
print("straight: ", check_straight(flush_hand))       # Should return False (not a straight)
print("flush: ", check_flush(flush_hand))             # Should return True (all cards are diamonds)
print("straight flush: ", check_straight_flush(flush_hand))  # Should return False (no straight)
print("4 of kind: ", check_four_of_kind(flush_hand))  # Should return False (no four of a kind)
print("pairs: ", check_pairs(flush_hand))             # Should return 0 (no pairs)
print("trips: ", check_trips(flush_hand))             # Should return False (no three of a kind)
print("hand eval: ", check_hand(straight[0:2], straight[2:5]))

print("\n\n|||||| test 6 for 4ofaK ||||||")
# Test 6: Four of a kind - 4 Aces
four_of_kind = ["Kd", "Ac", "Ad", "Ah", "As", "5d"]
print(four_of_kind)
print("highest card:", get_highest_card(four_of_kind))  # Should return Ace (A is high)
print("straight: ", check_straight(four_of_kind))       # Should return False (no straight)
print("flush: ", check_flush(four_of_kind))             # Should return False (different suits)
print("straight flush: ", check_straight_flush(four_of_kind))  # Should return False (different suits)
print("4 of kind: ", check_four_of_kind(four_of_kind))  # Should return True (four Aces)
print("pairs: ", check_pairs(four_of_kind))             # Should return 0 (no pairs, just four of a kind)
print("trips: ", check_trips(four_of_kind))             # Should return False (four of a kind, not trips)
print("hand eval: ", check_hand(straight[0:2], straight[2:5]))

print("\n\n|||||| test 7 for two pairs ||||||")
# Test 7: Two Pairs - Kings and 7s
two_pairs = ["Qc", "Kd", "3d", "Kh", "7s", "7h", "2c"]
print(two_pairs)
print("highest card:", get_highest_card(two_pairs))     # Should return King (K is high)
print("straight: ", check_straight(two_pairs))          # Should return False (no straight)
print("flush: ", check_flush(two_pairs))                # Should return False (different suits)
print("straight flush: ", check_straight_flush(two_pairs))  # Should return False (different suits)
print("4 of kind: ", check_four_of_kind(two_pairs))     # Should return False (no four of a kind)
print("pairs: ", check_pairs(two_pairs))                # Should return 2 (two pairs: Kings and 7s)
print("trips: ", check_trips(two_pairs))                # Should return False (no three of a kind)
print("hand eval: ", check_hand(straight[0:2], straight[2:5]))

print("\n\n|||||| test 8 for trips ||||||")
# Test 8: Three of a kind - Three Queens
three_of_kind = ["Ac", "Qc", "Kh", "Qd", "Qh", "7s", "2c"]
print(three_of_kind)
print("highest card:", get_highest_card(three_of_kind))  # Should return Queen (Q is high)
print("straight: ", check_straight(three_of_kind))       # Should return False (no straight)
print("flush: ", check_flush(three_of_kind))             # Should return False (different suits)
print("straight flush: ", check_straight_flush(three_of_kind))  # Should return False (different suits)
print("4 of kind: ", check_four_of_kind(three_of_kind))  # Should return False (no four of a kind)
print("pairs: ", check_pairs(three_of_kind))             # Should return 0 (no pairs, just trips)
print("trips: ", check_trips(three_of_kind))             # Should return True (three Queens)
print("hand eval: ", check_hand(straight[0:2], straight[2:5]))

exit(0)