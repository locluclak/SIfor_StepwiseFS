import matplotlib.pyplot as plt

# Sample data for demonstration; replace with your actual data
# sample_sizes = [50, 100, 150, 200]

# no_inf = [1.0, 1.0, 1.0, 1.0]
# naivefixedk = [0.108333333, 0.1166667, 0.0916666666666, 0.09166666666]
# ocfixedk = [0.05834, 0.066667, 0.041666667, 0.058333333333333334]
# parafixedk = [0.0667, 0.05, 0.075, 0]

true_beta_t = [0.5, 1.0, 1.5, 2.0]

ocfixedk = [0.0583333333, 0.04166666, 0.06666666667, 0.075]
parafixedk = [0.0667, 0.05, 0.075, 0]

# Plot each series with different colors and markers
# plt.plot(sample_sizes, no_inf, label='No inference', marker='o', color='magenta')
# plt.plot(sample_sizes, naivefixedk, label='Naive', marker='o', color='red')
plt.plot(true_beta_t, ocfixedk, label='oc-fixedK', marker='o', color='green')
# plt.plot(sample_sizes, parafixedk, label='para-fixedK', marker='o', color='blue')


# Label the axes
plt.xlabel('True beta')
plt.ylabel('TPR')

# Set y-axis limit
plt.ylim(0, 1.1)
plt.xticks(true_beta_t)

# Add legend
plt.legend()
plt.savefig('plot/TPR_fixed.pdf', format = 'pdf')

# Display the plot
plt.show()