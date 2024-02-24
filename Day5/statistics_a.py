import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

# Define the mean number of events (lambda) for the Poisson distribution
lambda_ =4

# Create a Poisson distribution object with the specified lambda
dist = poisson(lambda_)

# Generate a range of integer values for evaluating the PMF and CDF
x_values = np.arange(0, 20)

# Calculate the PMF and CDF values for each x in the range
pmf_values = dist.pmf(x_values)
cdf_values = dist.cdf(x_values)

# Generate 1000 random realizations from the Poisson distribution
samples = dist.rvs(size=1000)

# Plot the PMF
plt.figure(figsize=(15, 5))
plt.subplot(1, 3, 1)
plt.stem(x_values, pmf_values, linefmt='b-', markerfmt='bo', basefmt='w-')
plt.title('Probability Mass Function (PMF)')
plt.xlabel('Number of Events')
plt.ylabel('Probability')

# Plot the CDF
plt.subplot(1, 3, 2)
plt.step(x_values, cdf_values, where='mid', color='g')
plt.title('Cumulative Distribution Function (CDF)')
plt.xlabel('Number of Events')
plt.ylabel('Cumulative Probability')

# Plot a histogram of the 1000 random realizations
plt.subplot(1, 3, 3)
plt.hist(samples, bins=range(np.min(samples), np.max(samples) + 2), density=True, alpha=0.6, color='r', edgecolor='black')
plt.title('Histogram of 1000 Random Realizations')
plt.xlabel('Number of Events')
plt.ylabel('Frequency (normalized)')

plt.tight_layout()
plt.show()
