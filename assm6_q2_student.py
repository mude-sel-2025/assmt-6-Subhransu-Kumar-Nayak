# INFERENCE
# In this code, I understand how to compute and visualize confidence intervals for sample means.
# The code generates multiple samples from a normal distribution, calculates the sample mean and standard error,
# and constructs confidence intervals around the sample means. It also tracks how many of these intervals contain the true population mean.




import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def confidence_interval(N_samples=100, sample_size=30, true_mean=67, true_std=10, confidence=0.99):
    """
    Demonstrates 99% confidence intervals for the mean.
    Parameters:
    - N_samples: Number of independent samples (here 40)
    - sample_size: Number of observations per sample
    - true_mean: True population mean
    - true_std: True population standard deviation
    - confidence: Confidence level (default 0.99 for 99% CI)
    """
    
    # WRITE_YOUR_CODE HERE TO COMPUTE THE Z VALUE
    # Z value for the two-tailed confidence interval
    alpha = 1 - confidence 
    z = norm.ppf(1 - alpha/2)
    # this code block ends here

    # Store the lower and upper bounds of each CI
    ci_lowers = []
    ci_uppers = []
    
    # Track intervals that do NOT contain the true mean
    misses = 0
    
    # Generate samples and compute CIs
    for i in range(N_samples):
        sample = np.random.normal(loc=true_mean, scale=true_std, size=sample_size)

        # WRITE_YOUR_CODE HERE TO COMPUTE SAMPLE MEAN, SAMPLE STANDARD ERROR, AND CI BOUNDS
        sample_mean = np.mean(sample) 
        sample_se = np.std(sample, ddof=1) / np.sqrt(sample_size) 
        
        lower = sample_mean - z * sample_se 
        upper = sample_mean + z * sample_se

        print(f"Sample {i+1}: Mean={sample_mean:.2f}, SE={sample_se:.2f}, CI=({lower:.2f}, {upper:.2f})")
        # this code block ends here

        # append to CI lists        
        ci_lowers.append(lower)
        ci_uppers.append(upper)
        
        # WRITE_YOUR_CODE HERE TO CHECK IF THE TRUE MEAN IS WITHIN THE CI, INCREMENT misses IF NOT
        if not (lower <= true_mean <= upper):
            misses += 1
        # this code block ends here
    
    # WRITE_YOUR_CODE HERE TO PRINT THE NUMBER OF MISSES AND THE PERCENTAGE
    print(f"Out of {N_samples} intervals, {misses} did NOT contain the true mean.")
    print(f"This is roughly {(1 - misses / N_samples) * 100:.1f}%, close to the expected 1% for a 99% CI.")
    # this code block ends here
    
    # Plot the CIs
    plt.figure(figsize=(8, 6))
    for i, (low, up) in enumerate(zip(ci_lowers, ci_uppers)):

        # WRITE_YOUR_CODE HERE TO cOLOR THE INTERVALS THAT MISS THE TRUE MEAN IN RED, OTHERS IN BLUE
        color = 'blue' if low <= true_mean <= up else 'red'
        # this code block ends here

        plt.plot([low, up], [i, i], color=color, lw=2)
        plt.plot([np.mean([low, up])], [i], 'o', color=color)  # mark sample mean
    
    plt.axvline(true_mean, color='magenta', linestyle='-', label='True Mean', lw=3)
    plt.xlabel("Value")
    plt.ylabel("Sample #")
    plt.title(f"{confidence*100:.0f}% Confidence Intervals for Sample Means\nMissed intervals: {misses}/{N_samples}")
    plt.legend()
    plt.grid(True)
    plt.show()
    
    

# ================================
# Run main if this script is executed
# ================================
if __name__ == "__main__":
    confidence_interval()

    plt.show() # do not comment this out