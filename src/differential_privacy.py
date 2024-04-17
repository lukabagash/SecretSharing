import numpy as np


def laplace_noise(epsilon, sensitivity):
    """Generate noise from the Laplace distribution."""
    return np.random.laplace(loc=0, scale=sensitivity/epsilon, size=1)[0]


def differentially_private_average(data):
    """Calculate the differentially private average of the data."""
    # Privacy parameter
    epsilon = 1
    
    # Sensitivity calculations
    sensitivity_sum = max(data)
    sensitivity_count = 1
    
    # Calculate noisy sum and count
    noisy_sum = sum(data) + laplace_noise(epsilon, sensitivity_sum)
    noisy_count = len(data) + laplace_noise(epsilon, sensitivity_count)
    
    # Calculate and return the differentially private average
    return noisy_sum / noisy_count