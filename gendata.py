import numpy as np 
from sklearn.preprocessing import normalize

def generate(n, m, p, true_beta_s, true_beta_t):
    """return Xs, Xt, Ys, Yt, Sigma_s, Sigma_t"""
    # Xs = np.random.rand(n, p)
    # Xt = np.random.rand(m, p)
    Xs = np.random.normal(loc = 0, scale = 1, size = (n, p))
    Xt = np.random.normal(loc = 0, scale = 1, size = (m, p))
    # # Normalize each feature
    Xs = normalize(Xs, axis=0)
    Xt = normalize(Xt, axis=0)

    mu_s = Xs.dot(true_beta_s)
    mu_t = Xt.dot(true_beta_t)

    Ys = mu_s + np.random.normal(loc = 0, scale = 1, size = (n, 1))
    Yt = mu_t + np.random.normal(loc = 0, scale = 1, size = (m, 1))

    Sigma_s = np.identity(n)
    Sigma_t = np.identity(m)

    return Xs, Xt, Ys, Yt, Sigma_s, Sigma_t

if __name__ == "__main__":
    Xs, Xt, Ys, Yt, Sigma_s, Sigma_t = generate(15, 5, 3, np.full((3,1), 2), np.full((3,1), 0))
    print(Xs)
    
    for xj in Xs.T:
        print("Norm xj:", np.linalg.norm(xj))
    print("______________")
    print(Ys)