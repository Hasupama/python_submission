import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Parameters for the normal distribution
mu = 0  # Mean
sigma = 1  # Standard deviation

# Create a normal distribution object with the specified mean and standard deviation
dist = norm(mu, sigma)

# Generate a range of values for evaluating the PDF and CDF
x_values = np.linspace(-5, 5, 1000)

# Calculate the PDF and CDF values for each x in the range
pdf_values = dist.pdf(x_values)
cdf_values = dist.cdf(x_values)

# Generate 1000 random realizations from the normal distribution
samples = dist.rvs(size=1000)

# Plot the PDF
plt.figure(figsize=(15, 5))
plt.subplot(1, 3, 1)
plt.plot(x_values, pdf_values, color='blue')
plt.title('Probability Density Function (PDF)')
plt.xlabel('Value')
plt.ylabel('Probability Density')

# Plot the CDF
plt.subplot(1, 3, 2)
plt.plot(x_values, cdf_values, color='green')
plt.title('Cumulative Distribution Function (CDF)')
plt.xlabel('Value')
plt.ylabel('Cumulative Probability')

# Plot a histogram of the 1000 random realizations
plt.subplot(1, 3, 3)
plt.hist(samples, bins=30, density=True, alpha=0.6, color='red', edgecolor='black')
plt.plot(x_values, pdf_values, color='blue')  # Overlay the PDF on the histogram
plt.title('Histogram of 1000 Random Realizations')
plt.xlabel('Value')
plt.ylabel('Frequency (normalized)')

plt.tight_layout()
plt.show()