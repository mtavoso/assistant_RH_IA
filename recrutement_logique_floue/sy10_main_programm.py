import numpy as np 
import fuzzylab as fl 
from fuzzylab.evalfis import fuzzify_input
from itertools import combinations
class Candidat ():

    def __init__(self, prenom, annee_xp, nb_langues, toeic, formation, score, nb_heures, nb_annees_pratique, ouverture, conscience, extraversion, agreabilite, nevrosisme, loisirs_cult):
        self.prenom=prenom
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

    def score_eval(self, csq_final): # méthode pour eval finale

        self.eval_finale= (csq_final[0]*-20+csq_final[1]*-10+csq_final[2]*10+csq_final[3]*20)/(csq_final[0]+csq_final[1] + csq_final[2]+ csq_final[3])


def equipe_selectionnee (equipes, index_equipe):
    equipe_finale=[]
    for candidat_selectionne in equipes[index_equipe]:
        equipe_finale.append(candidat_selectionne.prenom) #On va chercher les prénoms des personnes qui sont sélectionnnés pour l'équipe
    return(equipe_finale)

        
def score(liste_csq):
        
        liste_csq = np.array(liste_csq) #on transforme en np array pour faciliter le max
        csq_global=np.max(liste_csq, axis = 0) #on fait la max union
        return(csq_global[0]*(-20)+csq_global[1]*-10+csq_global[2]*10+csq_global[3]*20)/(csq_global[0]+csq_global[1] + csq_global[2]+ csq_global[3]) #On défuzzifie

def intersection_montante_descendante(a1, a2, b1, b2):
    """
    a1, a2 montante
    b1, b2 descendante
    Calcule le degré de possibilité d'un nombre flou (y compris scalaire)
    La fontion, selon l'appel, peut considérer une droite verticale comme soit montante soit descendante. Il faut donc faire les deux cas.
   """ 
    #droite montante
    if a1==a2: #permet d'éviter la division par 0
        x=a2
        y = (b2-x)/(b2-b1) #l'autre droite est descendante

    #deuxième cas: droite descendante
    elif b1==b2 :
        x=b2
        y = (x-a1)/(a2-a1) #l'autre droite est montante

    else:
        x = (b2 + a1*(b2-b1)/(a2-a1))/(1+((b2-b1)/(a2-a1)))
        y = (b2-x)/(b2-b1)

    return y  

    
#prenom, annee_xp, nb_langues, toeic, formation, score, nb_heures, nb_annees_pratique, ouverture, conscience, extraversion, agreabilite, nevrosisme, loisirs_cult



#CAS 1: Candidats avec des personnalités globalement similaires: capas pros qui changent OK
"""

candidats = [Candidat("Matys", 7, 5, 800, 15, 17, [8,9,10], 10, 60, 80, 100, 100, 60, 1), Candidat("Luu Ly", 1, 1, 500, 8, 10, [1,1,1], 1, 60, 80, 100, 100, 60, 1),  
            Candidat("Zoe", 5, 3, 825, 14, 16, [2,3,4], 5, 60, 80, 100, 100, 60, 1), Candidat("Skander", 20, 5, 900, 19, 20, [7,8,9], 10, 60, 80, 100, 100, 60, 1),
            Candidat("Elio", 30, 5, 700, 17, 20, [12,14,15], 10, 60, 80, 100, 100, 60, 1), Candidat("Souleye", 2, 2, 300, 7, 8, [1,1.5,2], 1, 60, 80, 100, 100, 60, 0), 
            Candidat("Vicenzo", 8, 5, 900, 19, 20, [11,12,13], 10, 60, 80, 100, 100, 60, 1)]




#CAS 2: (matys elio Skander vicenzo) meilleur équipe en terme de capa pros (d'après cas 1): ils ne sont pas pris en premier car trop mauvaise entente. Matys et zoé proche en terme de capas pros, matys très désagréable donc zoé et prise. Luu ly et souley sont de toute façon trop peu qualifiés

candidats = [Candidat("Matys", 7, 5, 800, 15, 17, [8,9,10], 10, 20, 15, 40, 17, 10, 1), Candidat("Luu Ly", 1, 1, 500, 8, 10, [1,1,1], 1, 60, 85, 13, 15, 100, 1),  
            Candidat("Zoe", 5, 3, 825, 14, 16, [2,3,4], 5, 85, 80, 65, 100, 60, 1), Candidat("Skander", 20, 5, 900, 19, 20, [7,8,9], 10, 60, 80, 100, 100, 60, 1),
            Candidat("Elio", 30, 5, 700, 17, 20, [12,14,15], 10, 60, 80, 100, 100, 60, 1), Candidat("Souleye", 2, 2, 300, 7, 8, [1,1.5,2], 1, 20, 80, 85, 50, 90, 0), 
            Candidat("Vicenzo", 8, 5, 900, 19, 20, [11,12,13], 10, 60, 80, 100, 100, 60, 1)]



#CAS 3: Candidats globalement similaires d'un point de pro: Matys jamais pris car pas sympa du tout. zoé et elio ne sont pas ensembles dans la première équipe car conscience pro très basse;
        # Dans l'absolu ils pourraient s'entendre, mais ca ne nous convient pas dans un cadre professionnel. Zoé personnalité assez mauvaises: peu d'équipe. 6ème équipe vraiment mauvaise: 
        #matys pas agréable, zoé personnalité moyenne et luu ly et souleye haut 
        #névrosisme (entre autres: dur à détailler il faudrait pour chaque équipe détailler les relations deux à deux (6 en tout)) 
candidats = [Candidat("Souleye",  5, 3, 750, 8, 10, [9,10,11], 10, 20, 10, 60, 100, 80, 0), Candidat("Matys", 5, 5, 750, 12, 13, [9,10,11], 10, 0, 0, 20, 20, 20, 1), 
            Candidat("Luu Ly",  4, 5, 600, 12, 13, [9,10,11], 10, 15, 50, 45, 60, 100, 1), Candidat("Zoe",  6, 5, 800, 12, 13, [9,10,11], 10, 20, 12, 20, 42, 20, 1), 
            Candidat("Skander",  4, 5, 800, 12, 13, [9,10,11], 10, 73, 52, 50, 75, 10, 1),Candidat("Elio",  5, 5, 825, 12, 13, [9,10,11], 10, 80, 10, 60, 70, 50, 1),  
            Candidat("Vicenzo",  5, 5, 800, 12, 13, [9,10,11], 10, 60, 60, 80, 100, 60, 1)]
"""

#CAS 4 : D'après le 2 (zoe elio Skander vicenzo) ceux qui s'entendent le mieux, mais pas les meilleurs en termes d'éval individuelles : vicenzo pas assez bon. 
candidats = [Candidat("Matys", 7, 5, 800, 15, 17, [8,9,10], 10, 20, 15, 40, 17, 10, 1), Candidat("Luu Ly", 5, 3, 950, 12, 14, [1,1,1], 1, 60, 85, 13, 15, 100, 1),  
            Candidat("Zoe", 5, 3, 825, 14, 16, [2,3,4], 5, 85, 80, 65, 100, 60, 1), Candidat("Skander", 20, 5, 900, 19, 20, [7,8,9], 10, 60, 80, 100, 100, 60, 1),
            Candidat("Elio", 30, 5, 700, 17, 20, [12,14,15], 10, 60, 80, 100, 100, 60, 1), Candidat("Souleye", 2, 2, 300, 7, 8, [1,1.5,2], 1, 20, 80, 85, 50, 90, 0), 
            Candidat("Vicenzo", 0, 2, 650, 5, 8, [0,0.5,1], 2, 60, 80, 100, 100, 60, 1)]

"""

#CAS 5 : Cas quelconque

- Skander et Matys: en face de vous
- Zoe: ingenieure agée de l'ancienne école
- Elio: polytechnicien junior un peu condescendant
- Vicenzo: quinqua cool, bon techniquement mais sorti d'une formation moyenne
- Luu ly : utcéenne confirmée
- Souleye: sympa mais s'est trompé d'annonce

candidats = [Candidat("Matys", 0, 3, 950, 15, 16, [5,6,7], 12, 80, 60, 50, 70, 25, 1), Candidat("Luu Ly", 8, 5, 990, 11, 16, [0.1,0.1,0.1], 0, 64, 38, 24, 66, 96, 1),  
            Candidat("Zoe", 27, 2, 760, 12, 12, [1,2,3], 4, 35, 84, 65, 22, 70, 0), Candidat("Skander", 0, 5, 960, 17, 16, [2,3,4], 10, 70, 50, 60, 75, 34, 1),
            Candidat("Elio", 3, 3, 975, 18, 20, [1,1,1], 0, 40, 80, 41, 46, 54, 1), Candidat("Souleye", 7, 2, 825, 3, 4, [5,6,7], 6, 94, 81, 76, 98, 34, 0), 
            Candidat("Vicenzo", 32, 1, 485, 19, 13, [0.1,0.1,0.1], 0, 83, 43, 92, 100, 16, 1)]
"""
##sortie: ordre total non strict: ex-aequo d'ou le top 5

#####EVALUATION INDIVIDUELLE
for candidat in candidats :
    liste_y = []
    sf_cult = fl.readfis("Z:\SIF_ivestissement_ vie_culturelle_et_sportive")

    a1, a2, a3 = candidat.nb_heures[0], candidat.nb_heures[1], candidat.nb_heures[2]
        #Calcul conséquence flou culture
    for mf in sf_cult.Inputs[0].MembershipFunctions:
        param = mf.Parameters

        if mf.Type == "trimf":
            b1, b2, b3 = param[0], param[1], param[2]
    
            if  a1>=b3 or a3 <=b1:
                y =0

            elif a1<=b3 and a2>=b2:
                y = intersection_montante_descendante(a1, a2, b2, b3)
                
                #montante descendante
            elif a3>=b1 and a2<=b2:
                #descendante montante
                y = intersection_montante_descendante(b1, b2, a2, a3)
            


            #mont desc monte desc
        if mf.Type == "trapmf":

            b1, b2, b3, b4 = param[0], param[1], param[2], param[3]
    
            if  a1>=b4 or a3 <=b1:
                y =0

            elif a1<=b4 and a2>=b3:
                y = intersection_montante_descendante(a1, a2, b3, b4)
                
                #montante descendante
            elif a3>=b1 and a2<=b2:
                #descendante montante
                y = intersection_montante_descendante(b1, b2, a2, a3)
            
            elif b2<a2<b3:
                y = 1  # car toutes les hauteurs des partitions floues sont 1
        liste_y.append(y)
         

    irr_cult = fuzzify_input(sf_cult,[1, candidat.nb_annees_pratique, candidat.loisirs_cult]) 
    liste_y = np.array(liste_y)
    score_fuzz=irr_cult[:,[1,2]] 
    norm_csq_cult=liste_y/max(liste_y) #normalisation car calcul de possibilités
    nb_regles_cult = len(sf_cult.Rules)
    nb_csq_cult = len(sf_cult.Outputs[0].MembershipFunctions) 
    csq_cult = np.zeros((nb_csq_cult))
    irr_cult = np.zeros((nb_regles_cult, 3))
    irr_cult[:,(1,2)]=score_fuzz 
    for i in range(nb_regles_cult):
        irr_cult[i,0] = norm_csq_cult[sf_cult.Rules[i].Antecedent[0]-1]

    degre_declenchement_cult = np.min(irr_cult, axis=1) #min sur les lignes 
    nb_regles_cult = len(sf_cult.Rules)
    nb_csq_cult = len(sf_cult.Outputs[0].MembershipFunctions) #1 seul output defini-> donne le nombre de mf associé
    csq_cult = np.zeros((nb_csq_cult))
    for i in range (nb_regles_cult):
        csq_cult[sf_cult.Rules[i].Consequent[0]-1] = max(csq_cult[sf_cult.Rules[i].Consequent[0]-1], degre_declenchement_cult[i])#necessaire de faire moins 1 car indice de consequent sont de 1 à 4, on veut de 0 à 3

    # Calcul conséquence flou langue
    sf_langues = fl.readfis("SIF_langue_étrangère")
    irr_langues = fuzzify_input(sf_langues,[candidat.nb_langues, candidat.toeic])#équivalent à evalfis
    degre_declenchement_langues = np.min(irr_langues, axis=1) #min sur les lignes 
    nb_regles_langues = len(sf_langues.Rules)
    nb_csq_langues = len(sf_langues.Outputs[0].MembershipFunctions) 
    csq_langues = np.zeros((nb_csq_langues))
    
    for i in range (nb_regles_langues):
        csq_langues[sf_langues.Rules[i].Consequent[0]-1] = max(csq_langues[sf_langues.Rules[i].Consequent[0]-1], degre_declenchement_langues[i])         
        
    
    
    ### Calcul conséquence flou ouverture culturelle avec csq flou langue et csq flou culture
    sf_ouverture = fl.readfis("SF_ouverture_culturelle")
    nb_regles_ouverture = len(sf_ouverture.Rules)
    norm_csq_cult = csq_cult/max(csq_cult)
    norm_csq_langues = csq_langues/max(csq_langues)
    irr_ouverture = np.zeros((nb_regles_ouverture, 2))
    for i in range(nb_regles_ouverture):
        irr_ouverture[i, 0] = norm_csq_langues[sf_ouverture.Rules[i].Antecedent[0]-1]
        irr_ouverture[i, 1] = norm_csq_cult[sf_ouverture.Rules[i].Antecedent[1]-1]
    degre_declenchement_ouverture = np.min(irr_ouverture, axis=1) #min sur les lignes 
    nb_csq_ouverture = len(sf_ouverture.Outputs[0].MembershipFunctions) 
    csq_ouverture = np.zeros((nb_csq_ouverture))
    for i in range (nb_regles_ouverture):
        csq_ouverture[sf_ouverture.Rules[i].Consequent[0]-1] = max(csq_ouverture[sf_ouverture.Rules[i].Consequent[0]-1], degre_declenchement_ouverture[i])   

    #calcul csq flou expertise
    sf_exp = fl.readfis("SIF_expertise")
    irr_exp = fuzzify_input(sf_exp, [candidat.formation, candidat.annee_xp])
    degre_declenchement_exp = np.min(irr_exp, axis=1) 
    nb_regles_exp = len(sf_exp.Rules)
    nb_csq_exp = len(sf_exp.Outputs[0].MembershipFunctions) 
    csq_exp = np.zeros((nb_csq_exp))
    
    for i in range (nb_regles_exp):
        csq_exp[sf_exp.Rules[i].Consequent[0]-1] = max(csq_exp[sf_exp.Rules[i].Consequent[0]-1], degre_declenchement_exp[i])    


    # Calcul csq flou capa (sf hybride)
    sf_capa = fl.readfis("SF_Capacite_technique")
    irr_capa = fuzzify_input(sf_capa, [candidat.score, 1])
    score_fuzz=irr_capa[:,0] #premiere colonne de l'irr_capa
    norm_csq_exp=csq_exp/max(csq_exp)
    nb_regles_capa = len(sf_capa.Rules)
    nb_csq_capa = len(sf_capa.Outputs[0].MembershipFunctions) 
    csq_capa = np.zeros((nb_csq_capa))
    irr_capa = np.zeros((nb_regles_capa, 2)) #on "réaffecte" irr_capa qui désigne maintenant le tableau dans lequel on va stocker les antécédents
    irr_capa[:,0]=score_fuzz #la première colonne de l'irr 
    for i in range(nb_regles_capa):
        irr_capa[i,1] = norm_csq_exp[sf_capa.Rules[i].Antecedent[1]-1]
    degre_declenchement_capa = np.min(irr_capa, axis=1) #min sur les lignes 
    nb_csq_capa = len(sf_capa.Outputs[0].MembershipFunctions) 
    csq_capa = np.zeros((nb_csq_capa))
    for i in range (nb_regles_exp):
        csq_capa[sf_exp.Rules[i].Consequent[0]-1] = max(csq_capa[sf_exp.Rules[i].Consequent[0]-1], degre_declenchement_capa[i])    

    


    #evaluation finale
    sf_evaluation = fl.readfis("SF_Evaluation_individuelle")
    nb_regles_evaluation = len(sf_evaluation.Rules)
    norm_csq_capa = csq_capa/max(csq_capa)
    norm_csq_ouverture = csq_ouverture/max(csq_ouverture)
    irr_evaluation = np.zeros((nb_regles_evaluation, 2))
    for i in range(nb_regles_evaluation):
        irr_evaluation[i, 0] = norm_csq_capa[sf_evaluation.Rules[i].Antecedent[0]-1]
        irr_evaluation[i, 1] = norm_csq_ouverture[sf_evaluation.Rules[i].Antecedent[1]-1]
    degre_declenchement_evaluation = np.min(irr_evaluation, axis=1) #min sur les lignes 
    nb_csq_evaluation = len(sf_evaluation.Outputs[0].MembershipFunctions) 
    csq_evaluation = np.zeros((nb_csq_evaluation))

    for i in range (nb_regles_evaluation):
        csq_evaluation[sf_evaluation.Rules[i].Consequent[0]-1] = max(csq_evaluation[sf_evaluation.Rules[i].Consequent[0]-1], degre_declenchement_evaluation[i])   

    
    candidat.score_eval(csq_evaluation)
    
####EVALUATION PAR EQUIPES

liste_equipes=list(combinations(candidats,4))


liste_score_entente = []
liste_score_eval = []


for equipe in liste_equipes:
    #print(f"equipe {numcombi}")   
    #print(combi)
    liste_csq_agreabilite=[]
    liste_csq_extraversion=[]
    liste_csq_ouverture=[]
    liste_csq_conscience=[]
    liste_csq_nevrosisme=[]
    score_eval_equipe = 0
    somme=0
    for i in range(len(equipe)-1): #pour chaque indice(correspondant à un étudiant) dans chaque combinaison
       
        for j in range(len(equipe)-1,i,-1):
           #si on a deja fait Agreabilité1-Agreabilité2, permet de ne pas faire 2-1. i+1 car on ne veut pas faire Agreabilité1-Agreabilité1
            

        #agreabilite
            sf_agreabilite = fl.readfis("SF_Agreabilite")
            irr_agreabilite = fuzzify_input(sf_agreabilite,[equipe[i].agreabilite, equipe[j].agreabilite]) 
            degre_declenchement_agreabilite= np.min(irr_agreabilite, axis=1) 
            nb_regles_agreabilite = len(sf_agreabilite.Rules)
            nb_csq_agreabilite = len(sf_agreabilite.Outputs[0].MembershipFunctions) 
            csq_agreabilite= np.zeros((nb_csq_agreabilite))
            for k in range (nb_regles_agreabilite):
                csq_agreabilite[sf_agreabilite.Rules[k].Consequent[0]-1] = max(csq_agreabilite[sf_agreabilite.Rules[k].Consequent[0]-1], degre_declenchement_agreabilite[k])
            liste_csq_agreabilite.append(csq_agreabilite)

        #extraversion

            sf_extraversion = fl.readfis("SF_Extraversion")
            irr_extraversion = fuzzify_input(sf_extraversion,[equipe[i].extraversion, equipe[j].extraversion]) 
            degre_declenchement_extraversion= np.min(irr_extraversion, axis=1) 
            nb_regles_extraversion = len(sf_extraversion.Rules)
            nb_csq_extraversion = len(sf_extraversion.Outputs[0].MembershipFunctions) 
            csq_extraversion= np.zeros((nb_csq_extraversion))
            for k in range (nb_regles_extraversion):
                csq_extraversion[sf_extraversion.Rules[k].Consequent[0]-1] = max(csq_extraversion[sf_extraversion.Rules[k].Consequent[0]-1], degre_declenchement_extraversion[k])
            liste_csq_extraversion.append(csq_extraversion)
        
        #ouverture
                
            sf_ouverture = fl.readfis("SF_Ouverture")
            irr_ouverture = fuzzify_input(sf_ouverture,[equipe[i].ouverture, equipe[j].ouverture]) 
            degre_declenchement_ouverture= np.min(irr_ouverture, axis=1) 
            nb_regles_ouverture = len(sf_ouverture.Rules)
            nb_csq_ouverture = len(sf_ouverture.Outputs[0].MembershipFunctions) 
            csq_ouverture= np.zeros((nb_csq_ouverture))
            for k in range (nb_regles_ouverture):
                csq_ouverture[sf_ouverture.Rules[k].Consequent[0]-1] = max(csq_ouverture[sf_ouverture.Rules[k].Consequent[0]-1], degre_declenchement_ouverture[k])
            liste_csq_ouverture.append(csq_ouverture)

        #conscience
                
            sf_conscience = fl.readfis("SF_Conscience")
            irr_conscience = fuzzify_input(sf_conscience,[equipe[i].conscience, equipe[j].conscience]) 
            degre_declenchement_conscience= np.min(irr_conscience, axis=1) 
            nb_regles_conscience = len(sf_conscience.Rules)
            nb_csq_conscience = len(sf_conscience.Outputs[0].MembershipFunctions) 
            csq_conscience= np.zeros((nb_csq_conscience))
            for k in range (nb_regles_conscience):
                csq_conscience[sf_conscience.Rules[k].Consequent[0]-1] = max(csq_conscience[sf_conscience.Rules[k].Consequent[0]-1], degre_declenchement_conscience[k])
            liste_csq_conscience.append(csq_conscience)

        #nevrosisme
                
            sf_nevrosisme = fl.readfis("SF_Nevrosisme")
            irr_nevrosisme = fuzzify_input(sf_nevrosisme,[equipe[i].nevrosisme, equipe[j].nevrosisme]) 
            degre_declenchement_nevrosisme= np.min(irr_nevrosisme, axis=1) 
            nb_regles_nevrosisme = len(sf_nevrosisme.Rules)
            nb_csq_nevrosisme = len(sf_nevrosisme.Outputs[0].MembershipFunctions) 
            csq_nevrosisme= np.zeros((nb_csq_nevrosisme))
            for k in range (nb_regles_nevrosisme):
                csq_nevrosisme[sf_nevrosisme.Rules[k].Consequent[0]-1] = max(csq_nevrosisme[sf_nevrosisme.Rules[k].Consequent[0]-1], degre_declenchement_nevrosisme[k])
            liste_csq_nevrosisme.append(csq_nevrosisme)

    for i in range(len(equipe)): #moyenne des capacités sur l'équipe
        somme+=equipe[i].eval_finale
    score_eval_equipe=somme/len(equipe)
    liste_score_eval.append(score_eval_equipe)
                
                

    #pour chaque combinaison donnée, on a la liste des csq floues de agréabilité(1-2, 1-3, 1-4, 2-3, 2-4, 3-4), ouverture, conscience etc., il faut maintenant faire le max, puis défuzzifer des aspects sur l'équipe      
    
    score_agreabilite=score(liste_csq_agreabilite)
    score_extraversion=score(liste_csq_extraversion)
    score_ouverture=score(liste_csq_ouverture)
    score_conscience=score(liste_csq_conscience)
    score_nevrosisme=score(liste_csq_nevrosisme)
    
    score_entente=np.mean([score_agreabilite,score_extraversion,score_ouverture,score_conscience,score_nevrosisme])
    liste_score_entente.append(score_entente)

#EVALUATION GLOBALE
liste_score_eval_sorted = sorted(liste_score_eval, reverse=True) #tri décroissant
liste_score_entente_sorted = sorted(liste_score_entente, reverse= True)

liste_csq_eval_finale = []
for i in range (len(liste_equipes)):

    score_eval = liste_score_eval[i]
    place_eval = liste_score_eval_sorted.index(score_eval)+1

    score_entente = liste_score_entente[i]
    place_entente = liste_score_entente_sorted.index(score_entente)+1   

    sf_eval_finale = fl.readfis("SF_classement_final")
    irr_eval_finale = fuzzify_input(sf_eval_finale,[place_eval, place_entente]) 
    degre_declenchement_eval_finale= np.min(irr_eval_finale, axis=1) 
    nb_regles_eval_finale = len(sf_eval_finale.Rules)
    nb_csq_eval_finale = len(sf_eval_finale.Outputs[0].MembershipFunctions) 
    csq_eval_finale= np.zeros((nb_csq_eval_finale))
    for k in range (nb_regles_eval_finale):
        csq_eval_finale[sf_eval_finale.Rules[k].Consequent[0]-1] = max(csq_eval_finale[sf_eval_finale.Rules[k].Consequent[0]-1], degre_declenchement_eval_finale[k])

    liste_csq_eval_finale.append((csq_eval_finale[0]*(-20)+csq_eval_finale[1]*-10+csq_eval_finale[2]*10+csq_eval_finale[3]*20)/(csq_eval_finale[0]+csq_eval_finale[1] + csq_eval_finale[2]+ csq_eval_finale[3]))
    
classement_final = sorted(liste_csq_eval_finale, reverse= True)


for i in range(5):
    num_equipe = liste_csq_eval_finale.index(classement_final[i]) 
    print(f'Equipe {i+1}')
    print(equipe_selectionnee(liste_equipes, num_equipe))
    print(f"Appréciation de l'équipe: {classement_final[i]}")
    print(f'Classement evaluation: {liste_score_eval_sorted.index(liste_score_eval[num_equipe])+1}')
    print(f'Classement entente: {liste_score_entente_sorted.index(liste_score_entente[num_equipe])+1}')
    liste_csq_eval_finale[num_equipe]=False


