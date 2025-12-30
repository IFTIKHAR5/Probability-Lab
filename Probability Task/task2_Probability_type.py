# Objective: Create a system to identify and calculate different
#  probability types

# Instructions: 

# Implement a class ProbabilityCalculator with these methods: 
# 1. classical_probability(event_outcomes, sample_space) 
#  Both parameters are lists 
#  Returns probability assuming all outcomes equally likely 
#  Example: P(even number on dice) = 3/6 = 0.5 

# 2. empirical_probability(observed_frequencies) 
#  Parameter: dictionary with outcomes as keys and counts as values 
#  Returns dictionary with probabilities for each outcome 
#  Example: {'Heads': 520, 'Tails': 480} → {'Heads': 0.52, 'Tails': 0.48} 

# 3. identify_probability_type(description) 
#  Takes a text description 
#  Returns "Classical", "Empirical", or "Subjective" 
#  Use keyword matching (equally likely, observed data, personal belief)





            # --------------- 1) classical Probability ---------------- #

class ProbabilityCalculator:
    def classical_probability(self, event_outcomes, sample_space):

        # Count how many favorable outcomes are in the event
        favorable = len(event_outcomes) 

        # Count total possible outcomes in the sample space 
        total = len(sample_space) 

        # Apply classical probability formula
        # Probability = favorable outcomes / total outcomes
        probability = favorable / total
        return probability
    
    
    
    # -------- Calling the method --------

calc = ProbabilityCalculator()

# Define sample space and event outcomes
sample_space = [1, 2, 3, 4, 5, 6]
event_outcomes = [2, 4, 6]

# Pass parameters and get result
result = calc.classical_probability(event_outcomes, sample_space)

# Print the output
print(result)







                         #------------- 2) Empirical Probability -------------- #

class ProbabilityCalculator:

    def empirical_probability(self, observed_frequencies):
        
        # Start total observations from 0
        total = 0

        # Add all frequency values to find total observations
        for value in observed_frequencies.values():
            total = total + value

        # Create an empty dictionary to store probabilities
        probabilities = {}

        # Calculate probability for each outcome
        for key in observed_frequencies:
            probabilities[key] = observed_frequencies[key] / total

        # Return final probabilities
        return probabilities

# Create object of the class
calc = ProbabilityCalculator()

# Observed frequencies (real data)
observed_frequencies = {
    "Heads": 520,
    "Tails": 480
}

# Call method and store result
result = calc.empirical_probability(observed_frequencies)

# Print the result
print(result)





                 #------------- 3) # Identify Probability Type -------------- #


class ProbabilityCalculator:

    # This method identifies the type of probability
    def identify_probability_type(self, description):

        # Convert text to lowercase so comparison becomes easy
        description = description.lower()

        # Check for classical probability keywords
        if "equally likely" in description or "all cards" in description:
            return "Classical"

        # Check for empirical probability keywords
        if "observed" in description or "data" in description or "observations" in description:
            return "Empirical"

        # Check for subjective probability keywords
        if "feel" in description or "belief" in description or "might" in description:
            return "Subjective"

        # If none of the keywords match
        return "Unknown"


# Create object of the class
calc = ProbabilityCalculator()

# Test descriptions
text1 = "Based on 1000 coin toss observations"
text2 = "All cards are equally likely to be drawn"
text3 = "I feel it might rain today"

# Call method and print outputs
print(calc.identify_probability_type(text1))
print(calc.identify_probability_type(text2))
print(calc.identify_probability_type(text3))
