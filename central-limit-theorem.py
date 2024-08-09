import numpy as np
import matplotlib.pyplot as plt

# Generate 100 random numbers between 0 and 1
random_d = np.random.rand(100)

# Plot the histogram of these observations
plt.hist(random_d)
plt.title('Histogram of Random Observations')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()

# Extract samples and plot histograms of sample means
def plot_sample_means(n_samples, sample_size, data):
    random_samples = [np.random.choice(data, size=(sample_size,)) for _ in range(n_samples)]
    plt.hist(np.mean(random_samples, axis=1), bins=30)
    plt.title(f'Histogram of Sample Means ({n_samples} Samples)')
    plt.xlabel('Sample Mean')
    plt.ylabel('Frequency')
    plt.show()



plot_sample_means(100, 50, random_d)
plot_sample_means(500, 50, random_d)
plot_sample_means(1000, 50, random_d)

# Conclusion
print("As demonstrated, the distribution of sample means approaches a normal distribution as the number of samples increases. This illustrates the Central Limit Theorem.")

# Why Is the Central Limit Theorem Useful?
print("The Central Limit Theorem is fundamental in statistics as it allows us to assume that the distribution of sample means will be approximately normal, aiding in statistical inference and analysis.")