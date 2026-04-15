class Candidat:
    def __init__(self, prenom, annee_xp, nb_langues, toeic, formation, score,
                 nb_heures, nb_annees_pratique, ouverture, conscience,
                 extraversion, agreabilite, nevrosisme, loisirs_cult):

        self.prenom = prenom
        self.annee_xp = annee_xp
        self.nb_langues = nb_langues
        self.toeic = toeic
        self.formation = formation
        self.score = score
        self.nb_heures = nb_heures
        self.nb_annees_pratique = nb_annees_pratique
        self.ouverture = ouverture
        self.conscience = conscience
        self.extraversion = extraversion
        self.agreabilite = agreabilite
        self.nevrosisme = nevrosisme
        self.loisirs_cult = loisirs_cult

        self.eval_finale = 0

    def score_eval(self, csq_final):
        total = sum(csq_final)
        self.eval_finale = (
            csq_final[0] * -20 +
            csq_final[1] * -10 +
            csq_final[2] * 10 +
            csq_final[3] * 20
        ) / total