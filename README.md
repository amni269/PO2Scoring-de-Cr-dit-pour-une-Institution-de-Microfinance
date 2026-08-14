# PO2Scoring-de-Cr-dit-pour-une-Institution-de-Microfinance

# Scoring de Crédit pour une Institution de Microfinance

## Contexte et problématique métier

Les institutions de microfinance accordent des prêts à des commerçants et à de petites entreprises afin de soutenir leurs activités économiques. Cependant, certains emprunteurs peuvent ne pas rembourser leur crédit, ce qui représente un risque financier important.

L’objectif de ce projet est de développer un modèle de **scoring de crédit** capable de prédire si un commerçant du **marché de Madina (Conakry)** présente un **bon risque** ou un **mauvais risque de crédit**, afin d’aider une institution de microfinance à décider d’accorder ou de refuser un prêt.

## Source et description des données

Le jeu de données utilisé est une adaptation du dataset **Give Me Some Credit**, contextualisée pour le marché de Madina à Conakry.

### Volumétrie

* **Nombre de lignes :** 1 500
* **Nombre de colonnes :** 20
* **Variables explicatives :** 19
* **Variable cible :** `defaut_paiement`

### Dictionnaire des principales variables

| Variable                       | Description                                    |
| ------------------------------ | ---------------------------------------------- |
| `age`                          | Âge du commerçant                              |
| `genre`                        | Sexe du commerçant                             |
| `situation_matrimoniale`       | Situation matrimoniale                         |
| `nb_personnes_charge`          | Nombre de personnes à charge                   |
| `secteur_activite`             | Secteur d’activité du commerce                 |
| `anciennete_activite_annees`   | Ancienneté de l’activité                       |
| `revenu_mensuel_gnf`           | Revenu mensuel en francs guinéens              |
| `membre_tontine`               | Participation à une tontine                    |
| `possede_mobile_money`         | Possession d’un compte Mobile Money            |
| `membre_association_marchands` | Appartenance à une association de marchands    |
| `nb_credits_anterieurs`        | Nombre de crédits déjà obtenus                 |
| `a_deja_eu_retard`             | Existence d’un retard de paiement antérieur    |
| `jours_retard_max_anterieur`   | Nombre maximal de jours de retard              |
| `garant_disponible`            | Présence d’un garant                           |
| `score_bureau_credit`          | Score de crédit                                |
| `montant_pret_demande_gnf`     | Montant du prêt demandé                        |
| `duree_pret_mois`              | Durée du prêt en mois                          |
| `ratio_pret_revenu`            | Ratio entre le montant du prêt et le revenu    |
| `defaut_paiement`              | Variable cible (0 = remboursement, 1 = défaut) |

## Méthodologie (CRISP-DM)

Le projet a été réalisé selon la méthodologie **CRISP-DM**.

### 1. Compréhension métier

* Identification du problème d’octroi de crédit
* Définition de l’objectif de prédiction du risque de défaut

### 2. Compréhension des données

* Analyse exploratoire
* Étude des distributions
* Vérification des valeurs manquantes
* Analyse des corrélations

### 3. Préparation des données

* Suppression des doublons
* Encodage des variables catégorielles (One-Hot Encoding)
* Standardisation des variables numériques
* Construction d’un pipeline de prétraitement
* Séparation entraînement / test (80 % / 20 %)

### 4. Modélisation

Trois modèles de classification ont été comparés :

* Régression Logistique
* Arbre de Décision
* Gradient Boosting

### 5. Évaluation

Les modèles ont été évalués avec :

* Accuracy
* Précision
* Rappel
* Score F1
* ROC-AUC
* Matrice de confusion
* Courbe ROC

## Résultats – tableau comparatif des modèles

| Modèle                | Accuracy | Précision | Rappel | F1-score |   ROC-AUC |
| --------------------- | -------: | --------: | -----: | -------: | --------: |
| Régression Logistique |    0,783 |     0,481 |  0,667 |    0,559 | **0,822** |
| Gradient Boosting     |    0,783 |     0,491 |  0,444 |    0,466 |     0,797 |
| Arbre de Décision     |    0,717 |     0,333 |  0,349 |    0,341 |     0,627 |

Le **meilleur modèle retenu est la Régression Logistique**, car il offre le meilleur compromis entre performance, interprétabilité et capacité à détecter les clients à risque.
## Variables les plus explicatives

Les variables ayant le plus d’influence sur la prédiction du défaut de paiement sont :

* `ratio_pret_revenu`
* `a_deja_eu_retard`
* `montant_pret_demande_gnf`
* `score_bureau_credit`
* `anciennete_activite_annees`
* `garant_disponible`

Ces variables permettent d’identifier les commerçants présentant un risque élevé de défaut.
## Limites et pistes d’amélioration

### Limites

* Jeu de données simulé et adapté
* Taille relativement limitée du dataset
* Variables comportementales réelles absentes
* Évolution temporelle non prise en compte

### Pistes d’amélioration

* Utiliser des données réelles provenant d’une institution de microfinance
* Intégrer des données Mobile Money
* Tester des modèles avancés (XGBoost, LightGBM)
* Réaliser une optimisation des hyperparamètres
* Déployer une application web en ligne

---

## Comment exécuter le projet

### Installation

Créer un environnement Python puis installer les dépendances :

pip install pandas numpy matplotlib seaborn scikit-learn streamlit joblib

### Entraîner le modèle

Exécuter le notebook principal :
jupyter notebook notebooks/P02_scoring_credit.ipynb

### Lancer l’application Streamlit


streamlit run app.py
L’application sera accessible localement à l’adresse :

http://localhost:8501

## Lien vers la vidéo YouTube



**https://www.youtube.com/**

---

## Auteur

**Amni Ayouba Mhoma**

Master 1 Systèmes d’Information et Réseaux
Université Kofi Annan de Guinée
Projet réalisé dans le cadre du cours de **Fouille de Données**.
