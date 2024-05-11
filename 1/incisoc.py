import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt


# Cargar el archivo CSV en un DataFrame de Pandas
df = pd.read_csv("tested.csv", sep=";")

# Calcular estadísticas descriptivas
statistics = {}

for column in df.columns:
    if column not in ['Sex', 'Name', 'PassengerId']:  # Excluir 'Sex', 'Name', 'PassengerId', 'Fare'
        try:
            # Calcular moda
            mode = df[column].value_counts().idxmax()

            
            # Calcular media
            mean = np.mean(df[column].dropna())
            
            # Calcular mediana
            median = np.median(df[column].dropna())
            
            # Calcular media geométrica
            geometric_mean = stats.gmean(df[column].dropna())
            
            statistics[column] = {
                'Media': mean,
                'Mediana': median,
                'Moda': mode,
                'Media geométrica': geometric_mean
            }
        except ValueError:
            print(f"No se pudieron calcular todas las estadísticas para la columna '{column}'")

# Imprimir resultados
for column, stats in statistics.items():
    print(f"Estadísticas para la columna '{column}':")
    for stat, value in stats.items():
        print(f"{stat}: {value}")
    print()
    
