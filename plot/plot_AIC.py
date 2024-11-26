
import matplotlib.pyplot as plt

def plotAICFPR():
    # Sample data for demonstration; replace with your actual data
    sample_sizes = [50, 100, 150, 200]

    no_inf = [1.0, 1.0, 1.0, 1.0]
    naive = [0.141666666666, 0.125, 0.10833333333334, 0.1333333333]
    bonferroni = [0.0, 0.0, 0.0, 0.008333333]
    ds = [0.0588235294117, 0.075, 0.05833333333, 0.058333333333333]
    oc = [0.04166667, 0.033333333, 0.0583333333, 0.0416666666]
    para = [0.05, 0.0167, 0.05, 0.03333]

    plt.plot(sample_sizes, no_inf, label='No inference', marker='o', color='olive')
    plt.plot(sample_sizes, naive, label='Naive', marker='o', color='cyan')
    plt.plot(sample_sizes, bonferroni, label='Bonferroni', marker='o', color='purple')
    plt.plot(sample_sizes, ds, label='Data splitting', marker='o', color='red')
    plt.plot(sample_sizes, oc, label='oc-fixedK', marker='o', color='green')
    plt.plot(sample_sizes, para, label='para-fixedK', marker='o', color='blue')

    plt.xlabel('Sample size')
    plt.ylabel('FPR')
    plt.ylim(-0.05, 1.1)
    plt.xticks(sample_sizes)
    plt.legend()
    plt.savefig('plot/FPR_AIC.pdf', format = 'pdf')
    plt.show()
def plotAICTPR():
    true_beta_t = [1.0, 2.0, 3.0, 4.0]

    bonferroni = [0.016666667, 0.091666667, 0.158333333, 0.45]
    ds = [0.066667, 0.125, 0.26666666, 0.275]
    oc = [0.03333333, 0.05, 0.05, 0.025]
    para = [0.091666667, 0.2, 0.533333333, 0.783333333]

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
def plotAICbsFPR():
    # Sample data for demonstration; replace with your actual data
    sample_sizes = [50, 100, 150, 200]

    no_inf = [1.0, 1.0, 1.0, 1.0]
    naive = [0.1667, 0.1084, 0.1, 0.1]
    bonferroni =[0, 0, 0, 0]
    ds =[0.05, 0.05833333, 0.0666667, 0.075]
    oc = [0.04167, 0.058333, 0.05833, 0.05]

    para = [0.075, 0.05, 0.0416666667, 0.041666667]

    plt.plot(sample_sizes, no_inf, label='No inference', marker='o', color='olive')
    plt.plot(sample_sizes, naive, label='Naive', marker='o', color='cyan')
    plt.plot(sample_sizes, bonferroni, label='Bonferroni', marker='o', color='purple')
    plt.plot(sample_sizes, ds, label='Data splitting', marker='o', color='red')
    plt.plot(sample_sizes, oc, label='oc-fixedK', marker='o', color='green')
    plt.plot(sample_sizes, para, label='para-fixedK', marker='o', color='blue')

    plt.xlabel('Sample size')
    plt.ylabel('FPR')
    plt.ylim(-0.05, 1.1)
    plt.xticks(sample_sizes)
    plt.legend()
    plt.savefig('plot/BS_FPR_AIC.pdf', format = 'pdf')
    plt.show()
def plotAICbsTPR():
    true_beta_t = [1.0, 2.0, 3.0, 4.0]

    bonferroni = [0.016666667, 0.09167, 0.2, 0.3833333]
    ds = [0.146166667, 0.191666667, 0.28333333, 0.425]
    oc = [0.0583333, 0.0583333, 0.0583333, 0.033333]
    para = [0.175, 0.35833333, 0.583333, 0.75]


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
    plt.savefig('plot/BS_TPR_AIC.pdf', format = 'pdf')
    plt.show()
if __name__ == "__main__":
    plotAICFPR()
    plotAICTPR()
    plotAICbsFPR()
    plotAICbsTPR()