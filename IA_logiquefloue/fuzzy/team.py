import numpy as np
import fuzzylab as fl
from fuzzylab.evalfis import fuzzify_input
from core.scoring import score


TRAITS = [
    ("agreabilite", "SF_Agreabilite"),
    ("extraversion", "SF_Extraversion"),
    ("ouverture", "SF_Ouverture"),
    ("conscience", "SF_Conscience"),
    ("nevrosisme", "SF_Nevrosisme"),
]


def eval_equipe(equipe):
    """
    Évalue une équipe en agrégeant des scores flous
    sur plusieurs traits de personnalité et paires d'individus.
    """
    scores = []

    for attr, fis_name in TRAITS:
        liste_csq = []

        for i in range(len(equipe) - 1):
            for j in range(len(equipe) - 1, i, -1):

                sf = fl.readfis(fis_name)
                irr = fuzzify_input(sf, [
                    getattr(equipe[i], attr),
                    getattr(equipe[j], attr)
                ])

                deg = np.min(irr, axis=1)

                csq = np.zeros(len(sf.Outputs[0].MembershipFunctions))

                for k, r in enumerate(sf.Rules):
                    idx = r.Consequent[0] - 1
                    csq[idx] = max(csq[idx], deg[k])

                liste_csq.append(csq)

        scores.append(score(liste_csq))

    return np.mean(scores)