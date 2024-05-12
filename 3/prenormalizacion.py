import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer

# Cargar el conjunto de datos
df = pd.read_csv("tested.csv", sep=";")

# Seleccionar las características numéricas para la reducción de dimensionalidad
numeric_features = ['Age', 'Fare']

# Imputar valores faltantes en las características seleccionadas
imputer = SimpleImputer(strategy='mean')
df[numeric_features] = imputer.fit_transform(df[numeric_features])

# Escalar las características numéricas
scaler = StandardScaler()
scaled_features = scaler.fit_transform(df[numeric_features])

# Aplicar PCA para reducir la dimensionalidad
pca = PCA(n_components=2)  # Especificar el número de componentes principales deseados
reduced_features = pca.fit_transform(scaled_features)

# Crear un DataFrame con las características reducidas
df_reduced = pd.DataFrame(reduced_features, columns=['Reducido Age', 'Reducido Fare'])

# Concatenar las características reducidas con el DataFrame original
df_final = pd.concat([df.drop(numeric_features, axis=1), df_reduced], axis=1)

# Mostrar el DataFrame después del preprocesamiento
print("DataFrame después de la reducción de dimensionalidad:")
print(df_final.head())
import matplotlib.pyplot as plt

# Configurar la figura y los subplots
fig, axs = plt.subplots(2, 2, figsize=(12, 10))

# Graficar características 'Age' antes de la reducción de dimensionalidad
axs[0, 0].bar(df['Age'].value_counts().index, df['Age'].value_counts().values, color='blue')
axs[0, 0].set_title('Cantidad de apariciones de Age')
axs[0, 0].set_xlabel('Age')
axs[0, 0].set_ylabel('Cantidad')

# Graficar características 'Fare' antes de la reducción de dimensionalidad
axs[0, 1].bar(df['Fare'].value_counts().index, df['Fare'].value_counts().values, color='green')
axs[0, 1].set_title('Cantidad de apariciones de Fare')
axs[0, 1].set_xlabel('Fare')
axs[0, 1].set_ylabel('Cantidad')

# Graficar características reducidas 'Reducido Age' después de la reducción de dimensionalidad
axs[1, 0].bar(df_final['Reducido Age'].value_counts().index, df_final['Reducido Age'].value_counts().values, color='red')
axs[1, 0].set_title('Cantidad de apariciones de Reducido Age')
axs[1, 0].set_xlabel('Reducido Age')
axs[1, 0].set_ylabel('Cantidad')

# Graficar características reducidas 'Reducido Fare' después de la reducción de dimensionalidad
axs[1, 1].bar(df_final['Reducido Fare'].value_counts().index, df_final['Reducido Fare'].value_counts().values, color='orange')
axs[1, 1].set_title('Cantidad de apariciones de Reducido Fare')
axs[1, 1].set_xlabel('Reducido Fare')
axs[1, 1].set_ylabel('Cantidad')

# Ajustar el espaciado entre los subplots
plt.tight_layout()

# Mostrar la figura
plt.show()

