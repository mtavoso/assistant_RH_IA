# SY10 – Recrutement d’une équipe projet optimale avec logique floue

## Description

Ce projet a pour objectif d’automatiser la constitution d’une équipe projet performante et cohésive à partir d’un ensemble de candidats.

Contrairement aux approches classiques de recrutement, cette solution repose sur des systèmes d’inférence floue pour :

- Évaluer les compétences individuelles
- Mesurer la compatibilité entre les membres
- Classer les meilleures équipes possibles

L’objectif final est de sélectionner l’équipe la plus efficace et équilibrée parmi toutes les combinaisons possibles.

--

## Problématique

Comment recruter une équipe projet à la fois compétente et soudée ?

Le défi est double :
- Maximiser les capacités techniques
- Garantir une bonne cohésion humaine



## Méthodologie

Le projet repose sur deux axes principaux :

### 1. Évaluation de la capacité

Chaque candidat est évalué selon plusieurs critères :

- Expérience professionnelle
- Formation
- Score technique
- Langues parlées et score TOEIC
- Activités extra-professionnelles (sport, culture)

Ces données sont traitées via des systèmes flous afin d’obtenir un score individuel compris entre -20 et 20.



### 2. Évaluation de la cohésion

La cohésion est mesurée à partir du modèle de personnalité Big Five :

- Ouverture
- Conscience professionnelle
- Extraversion
- Agréabilité
- Névrosisme

La compatibilité est évaluée pour chaque paire de candidats, puis agrégée pour obtenir un score global d’équipe.



### 3. Classement des équipes

Toutes les équipes possibles sont générées (combinaisons de candidats).

Chaque équipe est évaluée selon :
- Sa capacité moyenne
- Sa cohésion globale

Un système flou final permet d’obtenir un score global et de classer les équipes.



## Technologies utilisées

- Python
- Bibliothèque fuzzylab
- Logique floue (systèmes d’inférence)
- Algorithmes de combinaison (itertools)



## Structure du projet

- `Candidat` : classe représentant un candidat et ses caractéristiques
- Systèmes flous :
  - Évaluation individuelle
  - Capacité technique
  - Ouverture culturelle
  - Compatibilité (Big Five)
- Génération et évaluation des équipes
- Classement final


## Exemple d’utilisation

Le programme permet de :

1. Définir une liste de candidats avec leurs caractéristiques
2. Générer toutes les équipes possibles
3. Évaluer chaque équipe
4. Retourner les meilleures équipes

---

## Résultats

Le système permet de :

- Sélectionner automatiquement les meilleures équipes
- Trouver un équilibre entre performance et compatibilité
- Illustrer l’impact des soft skills dans un recrutement

---

## Limites

- Sensibilité limitée aux petites variations de données
- Complexité algorithmique importante pour un grand nombre de candidats
- Les chemins vers les fichiers .fis sont en dur dans le code et doivent être adaptés à chaque environnement.


## Perspectives d’amélioration

- Intégration de nouveaux critères (motivation, leadership)
- Optimisation des performances pour les grandes bases de candidats
- Amélioration du système de décision final (seuils minimums)
- Dynamisation du partitionnement flou

## Auteurs

- Skander SAAD  
- Matys TAVOSO  

Projet réalisé dans le cadre de l’UV SY10 (2025)
