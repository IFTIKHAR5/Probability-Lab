# Step 1: BayesianUpdater Class

class BayesianUpdater:
    
    def __init__(self, prior, likelihood):
        # prior: dictionary of hypotheses and their probabilities
        # Example: {"Disease": 0.02, "No Disease": 0.98}
        
        # likelihood: dictionary of P(evidence | hypothesis)
        # Example: {"Disease": 0.95, "No Disease": 0.03}
        
        self.prior = prior
        self.likelihood = likelihood
    
    def update(self):
        # This function applies Bayes' theorem
        # Posterior ∝ Prior × Likelihood
        
        posterior = {}
        
        for hypothesis in self.prior:
            # Bayes formula (without normalization)
            posterior[hypothesis] = (
                self.prior[hypothesis] * self.likelihood[hypothesis]
            )
        
        # Normalize so probabilities sum to 1
        posterior = self.normalize(posterior)
        
        # Update prior with posterior for next update
        self.prior = posterior
        
        return posterior
    
    def normalize(self, probabilities):
        # This function ensures total probability = 1
        
        total = sum(probabilities.values())
        
        for key in probabilities:
            probabilities[key] = probabilities[key] / total
        
        return probabilities
    

# Step 2: Medical Diagnosis Problem (Given Data)
# Disease prevalence (prior)

prior = {
    "Disease": 0.02,
    "No Disease": 0.98
}


# Step 3: Positive Test Result

# Likelihood for positive test

# P(Positive | Disease) = 0.95 (true positive)

# P(Positive | No Disease) = 0.03 (false positive)

positive_test_likelihood = {
    "Disease": 0.95,
    "No Disease": 0.03
}

# Create Bayesian updater object
bayes = BayesianUpdater(prior, positive_test_likelihood)

# Update probabilities after positive test
posterior_positive = bayes.update()

print("After positive test:")
print(posterior_positive)



# Step 4: Negative Test Result (After Positive)

# Likelihood for negative test

# P(Negative | Disease) = 0.05

# P(Negative | No Disease) = 0.97

negative_test_likelihood = {
    "Disease": 0.05,
    "No Disease": 0.97
}

# Update likelihood for negative test
bayes.likelihood = negative_test_likelihood

# Update probabilities after negative test
posterior_negative = bayes.update()

print("\nAfter negative test (after positive):")
print(posterior_negative)


# Step 5: Multiple Tests (See Probability Change)

# Another positive test

# Another positive test likelihood
bayes.likelihood = positive_test_likelihood

posterior_second_positive = bayes.update()

print("\nAfter second positive test:")
print(posterior_second_positive)

