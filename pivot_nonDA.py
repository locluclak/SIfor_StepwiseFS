import numpy as np
from gendata import generate
import OptimalTransport
import ForwardSelection as FS
import overconditioning 
import parametric
from scipy.linalg import block_diag
from mpmath import mp
mp.dps = 500

import time
def compute_p_value(intervals, etaT_Y, etaT_Sigma_eta):
    denominator = 0
    numerator = None

    for i in intervals:
        leftside, rightside = i
        if leftside <= etaT_Y <= rightside:
            numerator = denominator + mp.ncdf(etaT_Y / np.sqrt(etaT_Sigma_eta)) - mp.ncdf(leftside / np.sqrt(etaT_Sigma_eta))
        denominator += mp.ncdf(rightside / np.sqrt(etaT_Sigma_eta)) - mp.ncdf(leftside / np.sqrt(etaT_Sigma_eta))
    if numerator is None:
        return 999
    cdf = float(numerator / denominator)
    # print(cdf)
    # compute two-sided selective p_value
    return 2 * min(cdf, 1 - cdf)

def pvalue_SI(seed, n, p, true_betaT):
    """Return final p_value"""
    np.random.seed(seed)

    # Generate data
    Xs, X, Ys, Y, Sigma_s, Sigma = generate(1, n, p, true_betaT, true_betaT)
    # print(X)
    # print(Y)
    # Best model from 1...p models by AIC criterion
    # SELECTION_F = FS.SelectionAIC(Y, X, Sigma)
    k = 3
    SELECTION_F = FS.fixedSelection(Y, X, k)[0]
    X_M = X[:, sorted(SELECTION_F)].copy()

    # Compute eta
    jtest = np.random.choice(range(len(SELECTION_F)))
    e = np.zeros((len(SELECTION_F), 1))
    e[jtest][0] = 1

    # eta constructed on Target data
    eta = np.dot(e.T , np.dot(np.linalg.inv(np.dot(X_M.T, X_M)), X_M.T)) 
    eta = eta.reshape((-1,1))
    etaT_Sigma_eta = np.dot(np.dot(eta.T , Sigma) , eta).item()
    
    # Change y = a + bz
    I_nplusm = np.identity(n)
    b = np.dot(Sigma, eta) / etaT_Sigma_eta
    a = np.dot((I_nplusm - np.dot(b, eta.T)), Y)

    # Test statistic
    etaTY = np.dot(eta.T, Y).item()
    # print(f"etay: {etaTY}")
    # finalinterval = overconditioning.OC_fixedFS_interval(ns, nt, a, b, XsXt_, Xtilde, Ytilde, Sigmatilde, basis_var, S_, h_, SELECTION_F, GAMMA)[0]
    # finalinterval = overconditioning.OC_AIC_interval(ns, nt, a, b, XsXt_, Xtilde, Ytilde, Sigmatilde, basis_var, S_, h_, SELECTION_F, GAMMA)
    finalinterval = parametric.para_FSwithfixedK(n, a, b, X, Sigma, SELECTION_F)
    # finalinterval = parametric.para_DA_FSwithAIC(ns, nt, a, b, X, Sigma, S_, h_, SELECTION_F,seed)
    # print(f"Final interval: {finalinterval}")

    # Naive
    # finalinterval = [(-np.inf, np.inf)]
    
    selective_p_value = compute_p_value(finalinterval, etaTY, etaT_Sigma_eta)
    if selective_p_value == 999:
        print('wrong! ',seed)
        exit()
        return

    return selective_p_value
