# Nettoyer et analyses les donnes dans bank-transaction
1● Supprimer les doublons selon transaction_id.
2● Convertir les colonnes de dates en type datetime.
3● Convertir les colonnes financières en float après nettoyage des symboles.
4● Uniformiser les textes :
      .Devise en majuscules.
      .Segment_client avec la première lettre en majuscule.
      .Supprimer les espaces superflus.
5● Remplacer les valeurs manquantes :
      .Par la médiane (median) pour les colonnes numériques.
      .Par le mode (mode) pour les colonnes catégoriques.
      .Par Unknown si nécessaire.
6● Tracer les graphiques pour les montants et les scores de crédit.
7● Détecter les valeurs aberrantes à l’aide de l’IQR et vérifier la plage de score_credit_client.
8● Extraire l’année, le mois, le trimestre et le jour à partir des dates.
9● Convertir les devises et calculer la classification du risque.
10● Calculer le solde net pour chaque client.
11● Agréger les données des transactions par client.
12● Calculer le taux de rejet pour chaque agence.
13● Enregistrer le fichier final au format cleaned CSV.