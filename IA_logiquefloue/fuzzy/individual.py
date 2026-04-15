import numpy as np
import fuzzylab as fl
from fuzzylab.evalfis import fuzzify_input
from fuzzy.utils import degre_appartenance


def defuzz(sf, irr):
    """Agrège les règles floues (min/max) et retourne les sorties."""

    deg = np.min(irr, axis=1)
    csq = np.zeros(len(sf.Outputs[0].MembershipFunctions))

    for i, r in enumerate(sf.Rules):
        idx = r.Consequent[0] - 1
        csq[idx] = max(csq[idx], deg[i])

    return csq


def eval_candidat(candidat):
    """
    Évalue un candidat via un système d'inférence floue multi-étapes :
    culture, langues, ouverture, expertise, capacité, puis score final.
    """

    # CULTURE
    sf_cult = fl.readfis("data/SIF_ivestissement_ vie_culturelle_et_sportive")

    #calcul flou sur nb_heures (triangle)
    deg_heures = degre_appartenance(candidat.nb_heures,sf_cult.Inputs[0].MembershipFunctions)

    deg_heures = deg_heures / np.max(deg_heures)  # normalisation

    irr_tmp = fuzzify_input(sf_cult, [1, candidat.nb_annees_pratique, candidat.loisirs_cult])

    irr_cult = np.zeros((len(sf_cult.Rules), 3))

    for i, r in enumerate(sf_cult.Rules):
        irr_cult[i, 0] = deg_heures[r.Antecedent[0] - 1]

    irr_cult[:, 1:] = irr_tmp[:, 1:]
    csq_cult = defuzz(sf_cult, irr_cult)

    # LANGUES
    sf_lang = fl.readfis("data/SIF_langue_étrangère")
    irr_lang = fuzzify_input(sf_lang, [candidat.nb_langues, candidat.toeic])
    csq_lang = defuzz(sf_lang, irr_lang)


    # OUVERTURE
    sf_ouv = fl.readfis("data/SF_ouverture_culturelle")

    norm_cult = csq_cult / sum(csq_cult)
    norm_lang = csq_lang / sum(csq_lang)

    irr_ouv = np.zeros((len(sf_ouv.Rules), 2))
    csq_ouv = np.zeros(len(sf_ouv.Outputs[0].MembershipFunctions))

    for i, r in enumerate(sf_ouv.Rules):
        irr_ouv[i, 0] = norm_lang[r.Antecedent[0] - 1]
        irr_ouv[i, 1] = norm_cult[r.Antecedent[1] - 1]

    deg = np.min(irr_ouv, axis=1)

    for i, r in enumerate(sf_ouv.Rules):
        idx = r.Consequent[0] - 1
        csq_ouv[idx] = max(csq_ouv[idx], deg[i])

    # EXPERTISE
    sf_exp = fl.readfis("data/SIF_expertise")
    irr_exp = fuzzify_input(sf_exp, [candidat.formation, candidat.annee_xp])
    csq_exp = defuzz(sf_exp, irr_exp)

    # CAPACITÉ
    sf_capa = fl.readfis("data/SF_Capacite_technique")

    irr_capa = fuzzify_input(sf_capa, [candidat.score, 1])
    score_fuzz = irr_capa[:, 0]

    norm_exp = csq_exp / sum(csq_exp)

    irr_tmp = np.zeros((len(sf_capa.Rules), 2))
    csq_capa = np.zeros(len(sf_capa.Outputs[0].MembershipFunctions))

    for i, r in enumerate(sf_capa.Rules):
        irr_tmp[i, 0] = score_fuzz[i]
        irr_tmp[i, 1] = norm_exp[r.Antecedent[1] - 1]

    deg = np.min(irr_tmp, axis=1)

    for i, r in enumerate(sf_capa.Rules):
        idx = r.Consequent[0] - 1
        csq_capa[idx] = max(csq_capa[idx], deg[i])

    # ÉVALUATION FINALE
    sf_eval = fl.readfis("data/SF_Evaluation_individuelle")

    norm_capa = csq_capa / sum(csq_capa)
    norm_ouv = csq_ouv / sum(csq_ouv)

    irr_eval = np.zeros((len(sf_eval.Rules), 2))
    csq_eval = np.zeros(len(sf_eval.Outputs[0].MembershipFunctions))

    for i, r in enumerate(sf_eval.Rules):
        irr_eval[i, 0] = norm_capa[r.Antecedent[0] - 1]
        irr_eval[i, 1] = norm_ouv[r.Antecedent[1] - 1]

    deg = np.min(irr_eval, axis=1)

    for i, r in enumerate(sf_eval.Rules):
        idx = r.Consequent[0] - 1
        csq_eval[idx] = max(csq_eval[idx], deg[i])

    return csq_eval