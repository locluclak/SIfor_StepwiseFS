import numpy as np
from sklearn.linear_model import LinearRegression

def SelectionBIC(Y,X,Sigma):
    BIC = np.inf
    n, p = X.shape
    
    for i in range(1, p+1):
        sset, rsdv = fixedSelection(Y, X, i)
        bic = rsdv.T.dot(Sigma.dot(rsdv)) + i*np.log(n)
        if bic < BIC:
            bset = sset
            BIC = bic
    return bset

def SelectionAdjR2(Y,X):
    # lRSS = np.inf
    # n, p = X.shape
    # for i in range(1, p+1):
    #     sset, rsdv = fixedSelection(Y, X, i)
    #     lrss = (n-1)/(n-i-1)*rsdv.T.dot(rsdv)
    #     if lrss < lRSS:
    #         bset = sset
    #         lRSS = lrss
    # return bset
    AdjR2 = -np.inf
    n, p = X.shape
    TSS = np.linalg.norm(Y - np.mean(Y))**2
    for i in range(1, p+1):
        sset, rsdv = fixedSelection(Y, X, i)
        RSS = np.linalg.norm(rsdv)**2

        adjr2 = 1 - (RSS/(n-i-1))/(TSS/(n-1))
        if adjr2 > AdjR2:
            bset = sset
            AdjR2 = adjr2
    return bset
def SelectionAIC(Y,X,Sigma):
    AIC = np.inf
    n, p = X.shape

    for i in range(1, p + 1):
        sset, rsdv = fixedSelection(Y, X, i)
        aic = rsdv.T.dot(Sigma.dot(rsdv)) + 2*i
        # print(aic)
        if aic < AIC:
            bset = sset
            AIC = aic
    return bset

def fixedSelection(Y, X, k):
    selection = []
    rest = list(range(X.shape[1]))
    rss = np.linalg.norm(Y)**2
    rsdv = None 
    for i in range(1, k+1):
        rss = np.inf
        sele = selection.copy()
        selection.append(None)
        for feature in rest:
            if feature not in selection:
                #select nessesary data
                X_temp = X[:, sorted(sele + [feature])].copy()
                #create linear model

                #calculate rss of model
                rss_temp, rsdv_temp = RSS(Y, X_temp)
                
                # choose feature having minimum rss and append to selection
                if rss > rss_temp:
                    rss = rss_temp
                    rsdv = rsdv_temp
                    selection.pop()
                    selection.append(feature)
        # print("RSS of selected feature:", rss)
    return selection, rsdv   

def RSS(Y, X):
    rss = 0
    coef = np.dot(np.dot(np.linalg.inv(np.dot(X.T, X)), X.T) , Y)
    yhat = np.dot(X, coef)
    residual_vec = Y - yhat
    rss = np.linalg.norm(residual_vec)**2
    # print("RSS:", RSS)
    return rss, residual_vec

def list_residualvec(X, Y) -> list:
    # Create 1 ... p matrixes which multiplies Y to get "residual vector of best k-subset"
    lst_Portho = []
    lst_SELEC_k = []
    n = Y.shape[0]
    for k in range(0, X.shape[1] + 1):
        selec_k = fixedSelection(Y, X, k)[0]
        lst_SELEC_k.append(selec_k)
        X_Mk = X[:, sorted(selec_k)].copy()
        lst_Portho.append(np.identity(n) - np.dot(np.dot(X_Mk, np.linalg.inv(np.dot(X_Mk.T, X_Mk))), X_Mk.T))
    return lst_SELEC_k, lst_Portho