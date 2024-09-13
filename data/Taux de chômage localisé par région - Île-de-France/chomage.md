# Informations à partager pour un dataset

## 1. Source du dataset
- **Lien** :  https://www.insee.fr/fr/statistiques/serie/001515843#Telechargement
- **Origine** : Fichier téléchargé 
- **Fichier** :  valeurs_trimestrielles 




## 2. Description du dataset
- **Description** : Taux de chomage par année en il de france toute la région
- **Contexte** : Objectif et contexte  économiques 


## 3. Structure des données

- **Format** : CSV et excel 

## 4. Format et taille
- **Taille du dataset** : 57  lignes 
- **Format de stockage** : Fichier plat 

## 5. Variables importantes
- **Colonnes clés** :
    periode  : par exemple 2024-T1 : pour dire 2024 trimesstre 4
    colonne sans nom : le taux de chomage 
 

- **Relations Avec elections** :  année 

## 6. Période couverte
- **Période** : Dates ou années couvertes par le dataset  : 2011 - 2023
 

## 8. Nettoyage ou transformation nécessaire
- **Transformation** :  
    - garder que les deux collones  periode  et la collone des taux qui n'a pas de nom 
    - Pour la colonne periode :     
            - Garder uniquemen le dernier trimesstre de chaque annnée pour avoir une seul ligne par année 
            - Nettoyer et formater le fichier 

## 9. Exemples d'utilisation
- **Cas d'usage** :  