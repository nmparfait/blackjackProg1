#Create a deal_card() function that uses the List below to *return* a random card.

import random 

def deal_card():
  """Return the random cards from the dec"""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calculate_score(cards):
  """Take a list of cards and return the score calculated from the cards"""
  # Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  
  # Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().
  
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)

  return sum(cards)

#Deal the user and computer 2 cards using deal_card
user_cards = []
computer_cards = []
is_game_over = False

for _ in range(2):
  user_cards.append(deal_card())
  computer_cards.append(deal_card())

user_score = calculate_score(user_cards)
computer_score = calculate_score(computer_cards)

print(f"   Your cards: {user_cards}, current score: {user_score}")
print(f"   Computer's first card: {computer_cards[0]}")

if user_score == 0 or computer_score == 0 or user_score > 21: 
  is_game_over = True

#Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

