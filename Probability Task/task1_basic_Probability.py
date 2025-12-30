# Create a function calculate_basic_probability(favorable, total) that: 
# 1. Takes two integers: favorable outcomes and total possible outcomes 
# 2. Returns the probability as a float between 0 and 1 
# 3. Includes error handling for invalid inputs (total = 0, negative numbers)

def calculate_basic_probability(favorable, total):
    if total == 0:
        return "Error: total cannot be 0"
    
    if favorable > total:
        return "Error: favorable cannot be greater than total"
    
    return favorable / total 

print(calculate_basic_probability(1,5)) 
print(calculate_basic_probability(4,6))
print(calculate_basic_probability(3,5))
print(calculate_basic_probability(2,3))