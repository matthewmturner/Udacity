import numpy as np

# Write a function that takes as input two lists Y, P,
# and returns the float corresponding to their cross-entropy.
def cross_entropy(Y, P):
    print(Y)
    print(P)
    probs = []
    for i, c in enumerate(Y):
        if c == 1:
            probs.append(P[i])
        else:
            probs.append(1 - P[i])
    return np.sum(-np.log(probs))


import numpy as np

# Write a function that takes as input two lists Y, P,
# and returns the float corresponding to their cross-entropy.
def cross_entropy_solution(Y, P):
    print(Y)
    print(P)
    probs = []
    for i, c in enumerate(Y):
        if c == 1:
            probs.append(P[i])
        else:
            probs.append(1 - P[i])
    return np.sum(-np.log(probs))
