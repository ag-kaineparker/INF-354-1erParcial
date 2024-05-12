import pandas as pd
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Cargar el archivo CSV en un DataFrame de Pandas
df = pd.read_csv("tested.csv", sep=";")
print(df.tail())

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.hist(df['Fare'], bins=20, color='blue', alpha=0.7)
plt.title('Antes del preprocesamiento')
plt.xlabel('Fare')
plt.ylabel('Frecuencia')

# Seleccionar las características numéricas a escalar
numerical_features = ['Fare']

# Crear un objeto StandardScaler
scaler = StandardScaler()

# Escalar las características numéricas y crear una nueva columna 'Fare_scaled'
df['Fare_scaled'] = scaler.fit_transform(df[numerical_features])
print("\nTransformado\n")

# Ver los primeros registros del DataFrame
print(df.tail())

plt.subplot(1, 2, 2)
plt.hist(df['Fare_scaled'], bins=20, color='green', alpha=0.7)
plt.title('Después del preprocesamiento')
plt.xlabel('Fare (escalado)')
plt.ylabel('Frecuencia')

plt.tight_layout()
plt.show()
