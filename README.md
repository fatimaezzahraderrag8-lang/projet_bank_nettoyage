# Projet Bank Nettoyage

## Contexte
Ce projet vise à analyser et nettoyer des données bancaires issues du fichier `bank-transactions.csv`.  
L’objectif est de préparer un jeu de données propre et exploitable pour l’analyse des risques financiers et la création de tableaux de bord.

##  Structure du dépôt
- `bank-transactions.csv` : données brutes des transactions bancaires.
- `nett_pre.ipynb` : notebook de prétraitement et d’analyse exploratoire.
- `fonc_categorie_risque.py` : fonctions pour catégoriser le risque client.
- `financecore_clean.csv` : données nettoyées et enrichies.
- `DECISIONS.md` : documentation des choix de nettoyage et de traitement.

##  Étapes de nettoyage
1. **Chargement des données** avec `pandas`.
2. **Exploration initiale** : dimensions, types de colonnes, statistiques descriptives.
3. **Gestion des doublons** : suppression des transactions dupliquées (`transaction_id`).
4. **Conversion des types** :
   - Dates (`date_transaction`) en format datetime.
   - Montants (`montant`) en float avec remplacement des virgules.
   - Solde avant (`solde_avant`) nettoyé des suffixes "EUR".
5. **Normalisation des chaînes** :
   - Devise en majuscules.
   - Segment client capitalisé.
   - Agence nettoyée des espaces.
6. **Valeurs manquantes** :
   - `score_credit_client` remplacé par la médiane.
   - `segment_client` remplacé par la modalité la plus fréquente.
   - `agence` remplacée par "Unknown".
7. **Détection des anomalies** :
   - Montants hors bornes (IQR).
   - Score crédit hors plage [0, 850].
     
8. **Enrichissement des données** :
   - Extraction d’année, mois, trimestre, jour.
   - Conversion en EUR (`montant_eur_verifie`).
   - Catégorisation du risque via `categorie_risque`.
   - Calcul du solde net par client.
   - Agrégation par client (nb transactions, montant moyen, nb produits).
   - Taux de rejet par agence.

## Visualisations
- Histogrammes des montants et des scores crédit.
