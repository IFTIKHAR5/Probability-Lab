# Objective: Implement functions to analyze relationships between 
# events 

# Instructions: 

# Create functions to determine: 

# 1. Mutually Exclusive Checker 
# def are_mutually_exclusive(eventA, eventB, sample_space): 
# # Return True if events cannot occur together 
# # Example: EventA = [1, 3, 5] (odd dice), EventB = [2, 4, 6] (even dice) 


# 2. Independent Events Checker 
# def are_independent(pA, pB, pA_and_B): 
# # Return True if P(A and B) = P(A) * P(B) 
# # Within tolerance of 0.001 for floating point errors 


# 3. Conditional Probability Calculator 
# def conditional_probability(pA_and_B, pA): 
# # Return P(B|A) = P(A and B) / P(A) 
# # Handle division by zero 


# Test Problem: 
# A deck of cards has 52 cards. Create events: 
#  Event A: Drawing a Heart (13 cards) 
#  Event B: Drawing a Face card (12 cards) 
#  Event C: Drawing a Red card (26 cards) 

# Determine which events are: 
# 1. Mutually exclusive 
# 2. Independent 
# 3. Calculate P(Face card | Heart)


                
                   #-------------- 1. Mutually Exclusive Checker -----------------#

def are_mutually_exclusive(eventA, eventB, sample_space): 

       # Loop through each item in Event A
    for item in eventA:

        # Check if this item is also in Event B
        if item in eventB:

            # If there is any common element, events are NOT mutually exclusive
            return False
        
    # If no common elements found, events are mutually exclusive
    return True
    
    
    # sample space
sample_space = [1, 2, 3, 4, 5, 6]

# Event A: Odd numbers
eventA = [1, 3, 5]

# Event B: Even numbers
eventB = [2, 4, 6]

# Event C: includes 3 and 4 (to test non-exclusive)
eventC = [3, 4]


# Check if Event A and B are mutually exclusive
print("Are A and B matually exclusive?", are_mutually_exclusive(eventA, eventB, sample_space))
print("Are A and C matually exclusive?", are_mutually_exclusive(eventA, eventC, sample_space))
print("Are B and C matually exclusive?", are_mutually_exclusive(eventB, eventC, sample_space))



               #-------------- 2. Independent Events Checker ----------------#

# Function to check if two events are independent
def are_independent(pA, pB, pA_and_B):
      
     # Step 1: Calculate P(A) * P(B) 
    product = pA * pB

    # Step 2: Compare with P(A and B) within tolerance 0.001
    # If difference is less than or equal to 0.001, consider them independent 
    if abs(pA_and_B - product) <= 0.001:  #abs is a buildin function that returns the absolute value of a number.The absolute value of a number is its distance from 0, ignoring whether it’s positive or negative. it alwasy give the numer in positive
        return True
    
    else:
        return False



     # Probabilities

# P(A) = Probability of drawing a Heart from 52 cards
pA = 13/52

# P(B) = Probability of drawing a Face card from 52 cards
pB = 12/52

# P(A and B) = Probability of drawing a Face card that is a Heart (J, Q, K of Hearts)
pA_and_B = 3/52

print("Are A and B independent?", are_independent(pA, pB, pA_and_B))




         #---------------- 3) Conditional Probability Calculator --------------#

# Function to calculate conditional probability P(B|A)
def conditional_probability(pA_and_B, pA):
    """
    P(B|A) = P(A and B) / P(A)
    Conditional probability of B given A
    """
    
    # Step 1: Check if P(A) is zero
    # Division by zero is not allowed
    if pA == 0:
        return None  # Cannot calculate, return None
    
    # Step 2: Apply formula for conditional probability
    # P(B|A) = P(A and B) / P(A)
    return pA_and_B / pA


# Example from deck of cards

# P(A) = Probability of drawing a Heart from 52 cards
pA = 13 / 52  # 13 Hearts out of 52 cards

# P(B) = Probability of drawing a Face card (we don't need it here)
# P(A and B) = Probability of drawing a Face card that is also a Heart (J, Q, K of Hearts)
pA_and_B = 3 / 52  # 3 cards are both Heart and Face cards

# Calculate P(Face card | Heart)
p_face_given_heart = conditional_probability(pA_and_B, pA)

# Print the result
print("P(Face card | Heart) =", p_face_given_heart)




       #----------- 4) Test Problem ------------#


# Check if two events are mutually exclusive
def are_mutually_exclusive(eventA, eventB):
    # If any card is common in both events, they are NOT mutually exclusive
    for card in eventA:
        if card in eventB:
            return False
    return True


# Check if two events are independent
def are_independent(pA, pB, pA_and_B):
    # Calculate P(A) * P(B)
    product = pA * pB

    # Compare with P(A and B) using tolerance
    if abs(pA_and_B - product) <= 0.001:
        return True
    else:
        return False


# Calculate conditional probability
def conditional_probability(pA_and_B, pA):
    # Avoid division by zero
    if pA == 0:
        return None
    return pA_and_B / pA


               # Step 1: Create Sample Space & Events

# Sample space: 52 cards (represented by numbers)
deck = list(range(1, 53))

# Event A: Hearts (13 cards)
eventA = list(range(1, 14))

# Event B: Face cards (J, Q, K of all suits)
eventB = [11, 12, 13, 24, 25, 26, 37, 38, 39, 50, 51, 52]

# Event C: Red cards (Hearts + Diamonds)
eventC = list(range(1, 27))


                 # Step 2: Mutually Exclusive Check

print("Mutually Exclusive Checks:")
print("A and B:", are_mutually_exclusive(eventA, eventB))
print("A and C:", are_mutually_exclusive(eventA, eventC))
print("B and C:", are_mutually_exclusive(eventB, eventC))



                # Step 3: Independent Events Check

# Probabilities
pA = len(eventA) / len(deck)   # 13/52
pB = len(eventB) / len(deck)   # 12/52

# P(A and B): Face cards that are Hearts (J♥, Q♥, K♥)
pA_and_B = 3 / 52

print("\nIndependent Check:")
print("Are A and B independent?", are_independent(pA, pB, pA_and_B))


             #  Step 4: Conditional Probability

# P(Face card | Heart)
result = conditional_probability(pA_and_B, pA)

print("\nConditional Probability:")
print("P(Face card | Heart) =", result)

