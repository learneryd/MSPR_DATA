# Installation et Configuration de Git Large File Storage (LFS)

## Introduction

Git Large File Storage (LFS) est une extension de Git qui permet de gérer les fichiers volumineux de manière efficace. Dans ce document, nous détaillons les étapes nécessaires pour installer et configurer Git LFS afin de gérer des fichiers de grande taille dans votre dépôt Git.

## Étapes d'Installation

### 1. Télécharger Git LFS

1. **Téléchargement :** Rendez-vous sur le site officiel de [Git LFS](https://git-lfs.github.com/) pour télécharger l'installateur approprié à votre système d'exploitation.
   
2. **Installer Git LFS :** Suivez les instructions fournies par l'installateur pour installer Git LFS sur votre machine.

### 2. Configurer Git LFS

Après avoir installé Git LFS, vous devez le configurer pour qu'il gère les fichiers volumineux dans votre dépôt Git.

1. **Initialiser Git LFS :**
   
   Ouvrez un terminal et exécutez la commande suivante pour initialiser Git LFS :

   ```bash
   git lfs install

2. **Suivre les types de fichiers:**

    Vous devez spécifier quels types de fichiers doivent être suivis par Git LFS. Par exemple, pour suivre tous les fichiers CSV volumineux, utilisez :

    ```bash
    git lfs track "*.csv"

    Ajoutez cette configuration au fichier .gitattributes dans la racine de votre dépôt

3. **Ajouter et Valider les Fichiers :**

    Ajoutez les fichiers volumineux à votre dépôt Git et validez les changements :

    ```bash
    
    git add .gitattributes
    git add path/to/large_file.csv
    git commit -m "Add large files to Git LFS"

4. **Pousser les Changements vers le Dépôt Distant :**

    Poussez vos changements vers le dépôt distant. Si vous avez déjà des fichiers volumineux dans l'historique de votre dépôt, vous devrez peut-être réécrire l'historique pour les intégrer dans Git LFS.

    ```bash
    
    git push origin main










### Explication des Commandes

- **`git lfs install`** : Configure les hooks Git pour utiliser Git LFS.
- **`git lfs track "*.csv"`** : Indique quels types de fichiers doivent être suivis par Git LFS.
- **`git add .gitattributes`** : Ajoute les configurations de Git LFS au dépôt.
- **`git commit -m "Add large files to Git LFS"`** : Valide les changements.
- **`git push origin main`** : Pousse les changements vers le dépôt distant.

Pour compléter, assurez-vous que ce fichier Markdown est enregistré dans le répertoire `Docs/` de votre projet.
