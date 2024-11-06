import matplotlib.pyplot as plt

# Sample data for demonstration; replace with your actual data
sample_sizes = [50, 100, 150, 200]
parafixedk = [0.0667, 0.05, 0.075, 0]
# Plot each series with different colors and markers
plt.plot(sample_sizes, parafixedk, label='para-fixedK', marker='o', color='blue')


# Label the axes
plt.xlabel('Sample size')
plt.ylabel('FPR')

# Set y-axis limit
plt.ylim(0, 1)

# Add legend
plt.legend()

# Display the plot
plt.show()