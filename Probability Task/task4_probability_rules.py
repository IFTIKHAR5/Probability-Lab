# 1) Addition Rule
def addition_rule(pA, pB, pA_and_B):
    # pA = probability of event A
    # pB = probability of event B
    # pA_and_B = probability of both A and B
    
    # Formula: P(A or B) = P(A) + P(B) - P(A and B)
    pA_or_B = pA + pB - pA_and_B
    
    return pA_or_B


# 2) Multiplication Rule

def multiplication_rule(pA, pB, are_independent):
    # pA = probability of event A
    # pB = probability of event B (or P(B|A) if dependent)
    # are_independent = True or False
    
    if are_independent:
        # Independent events
        # Formula: P(A and B) = P(A) * P(B)
        return pA * pB
    else:
        # Dependent events
        # Formula: P(A and B) = P(A) * P(B|A)
        return pA * pB


# 3) Complement Rule

def complement_rule(pA):
    # pA = probability of event A
    
    # Formula: P(not A) = 1 - P(A)
    return 1 - pA



# Step 2: Given Data (convert to probabilities)

total_students = 60

# Convert numbers into probabilities
p_math = 30 / total_students
p_science = 25 / total_students
p_math_and_science = 10 / total_students


# 1)  Probability a student likes Math OR Science

p_math_or_science = addition_rule(
    p_math,
    p_science,
    p_math_and_science
)

print("Probability a student likes Math or Science:", p_math_or_science)


# 2) Probability a student likes NEITHER Math nor Science

p_neither = complement_rule(p_math_or_science)

print("Probability a student likes neither:", p_neither)


# 3) Probability a Math-liker also likes Science

# This is conditional probability:

# p(science / math) = p(science and math) / p(math)

p_science_given_math = p_math_and_science / p_math

print("Probability a Math-liker also likes Science:", p_science_given_math)

