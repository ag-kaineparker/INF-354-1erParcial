import pandas as pd
from sklearn.preprocessing import OneHotEncoder
import matplotlib.pyplot as plt

# Cargar el archivo CSV en un DataFrame de Pandas
df = pd.read_csv("tested.csv", sep=";")

# Convertir las categorías de "Embarked" a valores numéricos
embarked_mapping = {'C': 0, 'Q': 1, 'S': 2}
df['Embarked'] = df['Embarked'].map(embarked_mapping)

# Graficar antes del preprocesamiento y codificar con One-Hot Encoder
plt.figure(figsize=(15, 5))


plt.subplot(1, 2, 1)
plt.hist(df['Embarked'], bins=len(df['Embarked'].unique()), color='blue', alpha=0.7)

plt.title('Antes del preprocesamiento')
plt.xlabel('Embarked')
plt.ylabel('Frecuencia')

# Codificar con One-Hot Encoder
ohe = OneHotEncoder(sparse=False)
embarked_encoded = ohe.fit_transform(df[['Embarked']])
unique_embarked = df['Embarked'].unique()
embarked_encoded_df = pd.DataFrame(embarked_encoded, columns=[f'Embarked_{embark}' for embark in unique_embarked])

# Imprimir los datos después del preprocesamiento
print("\nDataFrame después del preprocesamiento:")
df_encoded = pd.concat([df, embarked_encoded_df], axis=1)
print(df_encoded.head())

# Renombrar las columnas codificadas para facilitar el acceso
embarked_cols = [f'Embarked_{embark}' for embark in embarked_mapping.keys()]
df_encoded.columns = list(df.columns) + embarked_cols

# Calcular las frecuencias de cada categoría de "Embarked" después del preprocesamiento
embarked_freq = df_encoded[embarked_cols].sum()

# Gráfica después del preprocesamiento
plt.subplot(1, 2, 2)
plt.bar(range(len(embarked_freq)), embarked_freq.values.tolist(), color='green')
plt.xticks(range(len(embarked_freq)), [f'{embark}_0' for embark in embarked_mapping.keys()])
plt.xlabel('Embarked')
plt.ylabel('Frecuencia')
plt.title('Después del preprocesamiento')

plt.tight_layout()
plt.show()
