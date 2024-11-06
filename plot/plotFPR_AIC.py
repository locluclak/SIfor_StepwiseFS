import matplotlib.pyplot as plt

# Sample data for demonstration; replace with your actual data
sample_sizes = [50, 100, 150, 200]

no_inf = [1.0, 1.0, 1.0, 1.0]
naiveAIC = [0.141666666666, 0.10833333333334, 0.10833333333334, 0.0833333333]
ocAIC = [0.04166667, 0.033333333, 0.0583333333, 0.0416666666]
parafixedk = [0.0667, 0.05, 0.075, 0]

# Plot each series with different colors and markers
plt.plot(sample_sizes, no_inf, label='No inference', marker='o', color='magenta')
plt.plot(sample_sizes, naiveAIC, label='Naive', marker='o', color='red')
plt.plot(sample_sizes, ocAIC, label='oc-AIC', marker='o', color='green')
# plt.plot(sample_sizes, parafixedk, label='para-fixedK', marker='o', color='blue')


# Label the axes
plt.xlabel('Sample size')
plt.ylabel('FPR')

# Set y-axis limit
plt.ylim(0, 1.1)

# Add legend
plt.legend()

# Display the plot
plt.show()