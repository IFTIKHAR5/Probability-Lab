# 1. create_deck(): Returns list of 52 cards as strings "AH" (Ace of Hearts), "2S", etc. 

# 2. simulate_draws(deck, num_draws, with_replacement): 
# Simulates drawing cards 
# If with_replacement=True, card goes back after draw 
# Returns list of drawn cards
#  
# 3. calculate_experimental_probability(draws, target_condition): 
# Calculates probability based on simulation 
# target_condition is a function that takes a card and returns boolean 
# Example: lambda card: card.endswith('H') for hearts 

# 4. calculate_theoretical_probability(num_target, total_cards, draws, with_replacement): 
# Calculates what probability should be theoretically 

# Simulation Tasks: 
# 1. Draw 1000 cards with replacement, find P(Heart) 
# 2. Draw 1000 cards without replacement, find P(Ace) 
# 3. Draw two cards without replacement, find P(both are same suit) 
# 4. Compare experimental vs theoretical probabilities


# 1. Create a Deck of Cards

# Function to create a deck of 52 cards
def create_deck():
    suits = ['H', 'D', 'C', 'S']   # Hearts, Diamonds, Clubs, Spades
    ranks = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']

    deck = []

    # Create every combination of rank and suit
    for suit in suits:
        for rank in ranks:
            deck.append(rank + suit)

    return deck


# 2. Simulate Card Draws

import random

# Function to simulate drawing cards
def simulate_draws(deck, num_draws, with_replacement):
    drawn_cards = []

    # Make a copy so original deck is not changed
    temp_deck = deck.copy()

    for i in range(num_draws):
        card = random.choice(temp_deck)  # pick random card
        drawn_cards.append(card)

        # If no replacement, remove card after drawing
        if not with_replacement:
            temp_deck.remove(card)

            # Stop if deck becomes empty
            if len(temp_deck) == 0:
                break

    return drawn_cards


# 3. Experimental Probability (From Simulation)

# Calculate experimental probability
def calculate_experimental_probability(draws, target_condition):
    count = 0

    # Count how many cards satisfy the condition
    for card in draws:
        if target_condition(card):
            count += 1

    # Probability = favorable / total
    return count / len(draws)


# 4. Theoretical Probability

# Calculate theoretical probability
def calculate_theoretical_probability(num_target, total_cards, draws, with_replacement):
    
    # For one draw
    if draws == 1:
        return num_target / total_cards

    # For two draws without replacement
    if draws == 2 and not with_replacement:
        return (num_target / total_cards) * ((num_target - 1) / (total_cards - 1))




# Task 1: Draw 1000 cards WITH replacement → P(Heart)

deck = create_deck()

draws_1000 = simulate_draws(deck, 1000, with_replacement=True)

# Hearts end with 'H'
exp_prob_heart = calculate_experimental_probability(
    draws_1000,
    lambda card: card.endswith('H')
)

theo_prob_heart = calculate_theoretical_probability(13, 52, 1, True)

print("Task 1: P(Heart)")
print("Experimental:", exp_prob_heart)
print("Theoretical:", theo_prob_heart)


# Task 2: Draw 1000 cards WITHOUT replacement → P(Ace)

draws_52 = simulate_draws(deck, 52, with_replacement=False)

exp_prob_ace = calculate_experimental_probability(
    draws_52,
    lambda card: card.startswith('A')
)

theo_prob_ace = calculate_theoretical_probability(4, 52, 1, False)

print("\nTask 2: P(Ace)")
print("Experimental:", exp_prob_ace)
print("Theoretical:", theo_prob_ace)


# Task 3: Draw 2 cards WITHOUT replacement → P(same suit)

two_cards = simulate_draws(deck, 2, with_replacement=False)

# Check if both cards have same suit
same_suit = two_cards[0][-1] == two_cards[1][-1]

print("\nTask 3: Two cards drawn:", two_cards)
print("Both same suit?", same_suit)

# Theoretical probability
theo_same_suit = (13/52) * (12/51) * 4
print("Theoretical probability (same suit):", theo_same_suit)


# Task 4: Compare Experimental vs Theoretical

print("\nComparison:")
print("Heart  Experimental vs Theoretical:", exp_prob_heart, theo_prob_heart)
print("Ace  Experimental vs Theoretical:", exp_prob_ace, theo_prob_ace)
