import pandas as pd

# Chemin vers le fichier d'entrée
input_file = 'C:/Users/youne/Documents/data/candidats_results.csv'
# Chemin vers le fichier de sortie
output_file = 'C:/Users/youne/Documents/data/filtered_1_candidats_results.csv'

# Codes des départements pour Île-de-France
ile_de_france_departements = ['75', '92', '93', '94', '77', '78', '91', '95']

# Définir les types de données pour certaines colonnes
dtype_specification = {
    'Code du département': str,
    'Code de la commune': str,
    'Code du b.vote': str  # Ajoutez d'autres colonnes si nécessaire
}

# Lire le fichier en chunks pour gérer les très grands fichiers
chunk_size = 100000  # Ajustez en fonction de la mémoire disponible
chunks = pd.read_csv(input_file, sep=';', dtype=dtype_specification, chunksize=chunk_size, low_memory=False)

# Créer une liste pour stocker les morceaux filtrés
filtered_chunks = []

for chunk in chunks:
    # Filtrer les lignes où le Code du département est dans les départements de Île-de-France
    ile_de_france_data = chunk[chunk['Code du département'].astype(str).isin(ile_de_france_departements)]
    filtered_chunks.append(ile_de_france_data)

# Concaténer tous les morceaux filtrés en un seul DataFrame
filtered_data = pd.concat(filtered_chunks, ignore_index=True)

# Sauvegarder le résultat dans un nouveau fichier
filtered_data.to_csv(output_file, index=False, sep=';')
