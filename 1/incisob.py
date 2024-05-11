import pandas as pd
import numpy as np

# Cargar el archivo CSV en un DataFrame de Pandas
df = pd.read_csv("tested.csv", sep=";")

# Calcular el último cuartil y el percentil 80 para cada columna
for column in df.columns:
    if column not in ['Sex', 'Name']:  # Excluir 'PassengerId' y 'Name'
        try:
            third_quartile = np.percentile(df[column].dropna(), 75)
            percentile_80 = np.percentile(df[column].dropna(), 80)
            print(f"Columna '{column}':")
            print(f"  Último cuartil (Q3): {third_quartile}")
            print(f"  Percentil 80: {percentile_80}\n")
        except ValueError:
            print(f"No se pudo calcular el último cuartil y el percentil 80 para la columna '{column}'")
