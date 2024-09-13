import pandas as pd
import matplotlib.pyplot as plt

# Lire les données depuis le fichier CSV en spécifiant le séparateur comme point-virgule
file_path = 'C:\\Users\\adsbouzidia\\Documents\\contexte\\Ahmed\\inflation\\WEBSTAT-observations-2024-09-13T17_37_58.291+02_00.csv'
data = pd.read_csv(file_path, delimiter=';')

# Afficher les premières lignes du DataFrame pour vérifier que les données sont correctement chargées
print(data.head())

# Vérifier les noms de colonnes disponibles pour identifier celles qui contiennent les informations nécessaires
print(data.columns)

# Assurer que les colonnes nécessaires existent
if 'time_period' in data.columns and 'obs_value' in data.columns:
    # Convertir la colonne 'time_period' en format datetime (si nécessaire) ou la convertir en entier
    data['time_period'] = pd.to_datetime(data['time_period'], format='%Y', errors='coerce').dt.year

    # Créer un graphique
    plt.figure(figsize=(12, 6))
    plt.plot(data['time_period'], data['obs_value'], marker='o', linestyle='-', color='b')
    plt.title('Inflation over Time')
    plt.xlabel('Year')
    plt.ylabel('Inflation Value')
    plt.grid(True)
    plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
    plt.tight_layout()  # Adjust layout to fit labels

    # Afficher le graphique
    plt.show()
else:
    print("Les colonnes nécessaires 'time_period' et 'obs_value' ne sont pas présentes dans les données.")
