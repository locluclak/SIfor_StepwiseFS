import matplotlib.pyplot as plt

def plotfixedFPR():
    # Sample data for demonstration; replace with your actual data
    sample_sizes = [50, 100, 150, 200]

    no_inf = [1.0, 1.0, 1.0, 1.0]
    naivefixedk = [0.108333333, 0.1166667, 0.0916666666666, 0.09166666666]
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
    true_beta_t = [0.5, 1.0, 1.5, 2.0]

    bonferroni = [0.01666666666666, 0.03333333333, 0.075, 0.193277310924]
    ds = [0.06666666666666667, 0.11666666666666667, 0.21666666666666667, 0.225]
    ocfixedk = [0.0583333333, 0.04166666, 0.06666666667, 0.075]
    parafixedk = [0.0583333333 ,0.14166667 ,0.2 ,0.35833333333333334]
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

if __name__ == "__main__":
    plotfixedFPR()
    plotfixedTPR()