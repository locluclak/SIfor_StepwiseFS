import matplotlib.pyplot as plt

# Sample data for demonstration; replace with your actual data
sample_sizes = [50, 100, 150, 200]

no_inf = [1.0, 1.0, 1.0, 1.0]
naivefixedk = [0.108333333, 0.1166667, 0.0916666666666, 0.09166666666]
ocfixedk = [0.05834, 0.066667, 0.041666667, 0.058333333333333334]
parafixedk = [0.0667, 0.05, 0.075, 0]

# Plot each series with different colors and markers
plt.plot(sample_sizes, no_inf, label='No inference', marker='o', color='magenta')
plt.plot(sample_sizes, naivefixedk, label='Naive', marker='o', color='red')
plt.plot(sample_sizes, ocfixedk, label='oc-fixedK', marker='o', color='green')
plt.plot(sample_sizes, parafixedk, label='para-fixedK', marker='o', color='blue')


# Label the axes
plt.xlabel('Sample size')
plt.ylabel('FPR')

# Set y-axis limit
plt.ylim(0, 1.1)

# Add legend
plt.legend()

# Display the plot
plt.show()