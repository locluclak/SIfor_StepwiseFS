import pivot
import numpy as np
def run(iter = 0):    
    seed = int(np.random.rand() * (2**32 - 1))
    # seed = 487771846 
    np.random.seed(seed)
    # print("Seed:",seed)

    #___________________________________________________________
    ns = 50
    nt = 10
    p = 5
    betat = 0
    true_beta_s = np.full((p,1), 2) #source's beta
    true_beta_t = np.full((p,1), betat) #target's beta
    #___________________________________________________________

    pvalue = pivot.pvalue_SI(seed, ns, nt, p, true_beta_s, true_beta_t)

    # Save pvalue into file
    OCorPARA_FIXorAIC_FPRorTPR = 'para_AIC'
    filename = f'Experiment/Listpvalue_{OCorPARA_FIXorAIC_FPRorTPR}_{ns}_{p}.txt'
    # filename = f'Experiment/Listpvalue_{OCorPARA_FIXorAIC_FPRorTPR}_{ns}_{p}_{betat}.txt'
    with open(filename, 'a') as f:
        f.write(str(pvalue)+ '\n')
    return pvalue

if __name__ == "__main__":
    for i in range(1):
        # st = time.time()
        print(run())
        # en = time.time()
        # print(f"Time of 1 pvalue {i}: {en - st}")