
import matplotlib.pyplot as plt

def plotAICFPR():
    # Sample data for demonstration; replace with your actual data
    sample_sizes = [50, 100, 150, 200]

    no_inf = [1.0, 1.0, 1.0, 1.0]
    naive = [0.141666666666, 0.10833333333334, 0.10833333333334, 0.0833333333]
    bonferroni = [0.0, 0.0, 0.0, 0.008333333]
    ds = [0.0588235294117, 0.075, 0.05833333333, 0.058333333333333]
    oc = [0.04166667, 0.033333333, 0.0583333333, 0.0416666666]
    para = [0.05]

    plt.plot(sample_sizes, no_inf, label='No inference', marker='o', color='olive')
    plt.plot(sample_sizes, naive, label='Naive', marker='o', color='cyan')
    plt.plot(sample_sizes, bonferroni, label='Bonferroni', marker='o', color='purple')
    plt.plot(sample_sizes, ds, label='Data splitting', marker='o', color='red')
    plt.plot(sample_sizes, oc, label='oc-fixedK', marker='o', color='green')
    plt.plot(sample_sizes[0], para, label='para-fixedK', marker='o', color='blue')

    plt.xlabel('Sample size')
    plt.ylabel('FPR')
    plt.ylim(-0.05, 1.1)
    plt.xticks(sample_sizes)
    plt.legend()
    plt.savefig('plot/FPR_AIC.pdf', format = 'pdf')
    plt.show()
def plotAICTPR():
    true_beta_t = [0.5, 1.0, 1.5, 2.0]

    bonferroni = [0.008333333333333, 0.03361344537815126, 0.05833333333333, 0.06666666666667]
    ds = [0.041666666667, 0.0916666666, 0.125, 0.158333333333]
    oc = [0.0416666667, 0.05, 0.05833333, 0.0666666667]
    para = [0.08333333333333333, 0.091666666666666, 0.2083333333333333, 0.2]

    # Plot each series with different colors and markers
    plt.plot(true_beta_t, bonferroni, label='Bonferroni', marker='o', color='purple')
    plt.plot(true_beta_t, ds, label='Data splitting', marker='o', color='red')
    plt.plot(true_beta_t, oc, label='oc-AIC', marker='o', color='green')
    plt.plot(true_beta_t, para, label='para-AIC', marker='o', color='blue')


    plt.xlabel('True beta')
    plt.ylabel('TPR')

    plt.ylim(-0.05, 1.1)
    plt.xticks(true_beta_t)
    plt.legend()
    plt.savefig('plot/TPR_AIC.pdf', format = 'pdf')
    plt.show()

if __name__ == "__main__":
    plotAICFPR()
    plotAICTPR()