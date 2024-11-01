import overconditioning
import numpy as np
import OptimalTransport
import ForwardSelection
import intersection
def para_DA_FSwithAIC(ns, nt, a, b, X, Sigma, S_, h_, SELECTION_F):
    TD = []
    detectedinter = []

    z =  -20
    zmax = 20
    while z < zmax:
        z += 0.001

        for i in range(len(detectedinter)):
            if detectedinter[i][0] <= z <= detectedinter[i][1]:
                z = detectedinter[i][1] + 0.001
                detectedinter = detectedinter[i:]
                break
        if z > zmax:
            break
        print(z)
        Ydeltaz = a + b*z

        XsXt_deltaz = np.concatenate((X, Ydeltaz), axis= 1).copy()
        GAMMAdeltaz, basis_var_deltaz = OptimalTransport.solveOT(ns, nt, S_, h_, XsXt_deltaz).values()

        Xtildeinloop = np.dot(GAMMAdeltaz, X)
        Ytildeinloop = np.dot(GAMMAdeltaz, Ydeltaz)

        Sigmatilde_deltaz = GAMMAdeltaz.T.dot(Sigma.dot(GAMMAdeltaz))
        SELECTIONinloop = ForwardSelection.SelectionAIC(Ytildeinloop, Xtildeinloop, Sigmatilde_deltaz)
        # SELECTIONinloop = FS.fixedSelection(Ytildeinloop, Xtildeinloop, 4)[0]
        lst_SELECk_deltaz, lst_P_deltaz = ForwardSelection.list_residualvec(Xtildeinloop, Ytildeinloop)


        
        intervalinloop = overconditioning.OC_AIC_interval(ns, nt, a, b, XsXt_deltaz, 
                                                            Xtildeinloop, Ytildeinloop, Sigmatilde_deltaz, 
                                                            basis_var_deltaz, S_, h_, 
                                                            SELECTIONinloop, GAMMAdeltaz)
        detectedinter = intersection.Union(detectedinter, intervalinloop)

        if sorted(SELECTIONinloop) != sorted(SELECTION_F):
            continue
        print(SELECTIONinloop)
        TD = intersection.Union(TD, intervalinloop)
    return TD

def para_DA_FSwithfixedK(ns, nt, a, b, X, Sigma, S_, h_, SELECTION_F):
    TD = []
    detectedinter = []

    z =  -20
    zmax = 20
    while z < zmax:
        z += 0.001

        for i in range(len(detectedinter)):
            if detectedinter[i][0] <= z <= detectedinter[i][1]:
                z = detectedinter[i][1] + 0.001
                detectedinter = detectedinter[i:]
                break
        if z > zmax:
            break
        # print(z)
        Ydeltaz = a + b*z

        XsXt_deltaz = np.concatenate((X, Ydeltaz), axis= 1).copy()
        GAMMAdeltaz, basis_var_deltaz = OptimalTransport.solveOT(ns, nt, S_, h_, XsXt_deltaz).values()

        Xtildeinloop = np.dot(GAMMAdeltaz, X)
        Ytildeinloop = np.dot(GAMMAdeltaz, Ydeltaz)

        Sigmatilde_deltaz = GAMMAdeltaz.T.dot(Sigma.dot(GAMMAdeltaz))
        SELECTIONinloop = ForwardSelection.fixedSelection(Ytildeinloop, Xtildeinloop, len(SELECTION_F))[0]
        # SELECTIONinloop = FS.fixedSelection(Ytildeinloop, Xtildeinloop, 4)[0]
        lst_SELECk_deltaz, lst_P_deltaz = ForwardSelection.list_residualvec(Xtildeinloop, Ytildeinloop)


        
        intervalinloop = overconditioning.OC_fixedFS_interval(ns, nt, a, b, XsXt_deltaz, 
                                                            Xtildeinloop, Ytildeinloop, Sigmatilde_deltaz, 
                                                            basis_var_deltaz, S_, h_, 
                                                            SELECTIONinloop, GAMMAdeltaz)

        # print(f"intervalinloop: {intervalinloop}")

        detectedinter = intersection.Union(detectedinter, intervalinloop)

        if sorted(SELECTIONinloop) != sorted(SELECTION_F):
            # print(f"FAIL {SELECTIONinloop} -- {SELECTION_F}")
            continue
        # print(SELECTIONinloop)
        TD = intersection.Union(TD, intervalinloop)
    return TD