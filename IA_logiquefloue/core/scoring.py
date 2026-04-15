import numpy as np

def score(liste_csq):
    liste_csq = np.array(liste_csq)
    csq_global = np.max(liste_csq, axis=0)

    total = sum(csq_global)
    return (
        csq_global[0] * -20 +
        csq_global[1] * -10 +
        csq_global[2] * 10 +
        csq_global[3] * 20
    ) / total