import matplotlib.pyplot as plt

def plotfixedFPR():
    # Sample data for demonstration; replace with your actual data
    sample_sizes = [50, 100, 150, 200]

    no_inf = [1.0, 1.0, 1.0, 1.0]
    naivefixedk = [0.108333333, 0.1166667, 0.133333, 0.1]
    bonferroni = [0.005555555555555334, 0.005555555555555334, 0.0, 0.0027777777776666662]
    ds = [0.04201680672, 0.0583333333333, 0.025, 0.041666666666]
    ocfixedk = [0.05834, 0.066667, 0.041666667, 0.058333333333333334]
    parafixedk = [0.0667, 0.05, 0.075, 0.0583333333]

    plt.plot(sample_sizes, no_inf, label='No inference', marker='o', color='olive')
    plt.plot(sample_sizes, naivefixedk, label='Naive', marker='o', color='cyan')
    plt.plot(sample_sizes, bonferroni, label='Bonferroni', marker='o', color='purple')
    plt.plot(sample_sizes, ds, label='Data splitting', marker='o', color='red')
    plt.plot(sample_sizes, ocfixedk, label='oc-fixedK', marker='o', color='green')
    plt.plot(sample_sizes, parafixedk, label='para-fixedK', marker='o', color='blue')

    plt.xlabel('Sample size')
    plt.ylabel('FPR')
    plt.ylim(-0.05, 1.1)
    plt.xticks(sample_sizes)
    plt.legend()
    plt.savefig('plot/FPR_fixed.pdf', format = 'pdf')
    plt.show()
def plotfixedTPR():
    true_beta_t = [1.0, 2.0, 3.0, 4.0]

    bonferroni = [0.05, 0.2, 0.45, 0.58333333]
    ds = [0.125, 0.15833333, 0.4, 0.508333]
    ocfixedk = [0.041666667, 0.091666667, 0.08333333, 0.05833333]
    parafixedk = [0.14166667, 0.358333333, 0.5333333, 0.675]
    # parafixedknonDA = [0.13333333333333333 ,0.275 ,0.5 ,0.7416666666666667]

    # Plot each series with different colors and markers
    plt.plot(true_beta_t, bonferroni, label='Bonferroni', marker='o', color='purple')
    plt.plot(true_beta_t, ds, label='Data splitting', marker='o', color='red')
    plt.plot(true_beta_t, ocfixedk, label='oc-fixedK', marker='o', color='green')
    plt.plot(true_beta_t, parafixedk, label='para-fixedK', marker='o', color='blue')


    plt.xlabel('True beta')
    plt.ylabel('TPR')

    plt.ylim(0, 1.1)
    plt.xticks(true_beta_t)
    plt.legend()
    plt.savefig('plot/TPR_fixed.pdf', format = 'pdf')
    plt.show()

def plotfixedbsFPR():
    # Sample data for demonstration; replace with your actual data
    sample_sizes = [50, 100, 150, 200]

    no_inf = [1.0, 1.0, 1.0, 1.0]
    naivefixedk = [0.141666667, 0.141666667, 0.125, 0.1167]
    bonferroni = [0, 0.0083333, 0, 0.0083333]
    ds = [0.05, 0.04166666, 0.05, 0.033333]
    ocfixedk = [0.05, 0.075, 0.025, 0.0583]
    parafixedk = [0.0583, 0.05, 0.075, 0.0583333333]

    plt.plot(sample_sizes, no_inf, label='No inference', marker='o', color='olive')
    plt.plot(sample_sizes, naivefixedk, label='Naive', marker='o', color='cyan')
    plt.plot(sample_sizes, bonferroni, label='Bonferroni', marker='o', color='purple')
    plt.plot(sample_sizes, ds, label='Data splitting', marker='o', color='red')
    plt.plot(sample_sizes, ocfixedk, label='oc-fixedK', marker='o', color='green')
    plt.plot(sample_sizes, parafixedk, label='para-fixedK', marker='o', color='blue')

    plt.xlabel('Sample size')
    plt.ylabel('FPR')
    plt.ylim(-0.05, 1.1)
    plt.xticks(sample_sizes)
    plt.legend()
    plt.savefig('plot/BS_FPR_fixed.pdf', format = 'pdf')
    plt.show()
def plotfixedbsTPR():
    true_beta_t = [1.0, 2.0, 3.0, 4.0]

    bonferroni = [0.09166666, 0.525, 0.825, 0.90833333]
    ds = [0.241666667, 0.5083333, 0.675, 0.725]
    ocfixedk = [0.05833333, 0.09166666, 0.04166667, 0.058333333]
    parafixedk = [0.308333333, 0.70833333, 0.875, 0.933333333]

    # Plot each series with different colors and markers
    plt.plot(true_beta_t, bonferroni, label='Bonferroni', marker='o', color='purple')
    plt.plot(true_beta_t, ds, label='Data splitting', marker='o', color='red')
    plt.plot(true_beta_t, ocfixedk, label='oc-fixedK', marker='o', color='green')
    plt.plot(true_beta_t, parafixedk, label='para-fixedK', marker='o', color='blue')


    plt.xlabel('True beta')
    plt.ylabel('TPR')

    plt.ylim(0, 1.1)
    plt.xticks(true_beta_t)
    plt.legend()
    plt.savefig('plot/BS_TPR_fixed.pdf', format = 'pdf')
    plt.show()

if __name__ == "__main__":
    plotfixedFPR()
    plotfixedTPR()
    plotfixedbsFPR()
    plotfixedbsTPR()