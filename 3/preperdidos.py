import pandas as pd
from sklearn.impute import SimpleImputer
import matplotlib.pyplot as plt

# Cargar el conjunto de datos
df = pd.read_csv("tested.csv", sep=";")

# Verificar si hay valores perdidos en la columna 'Age'
if df['Age'].isnull().any():
    # Seleccionar el método de imputación (por ejemplo, la media)
    imputer = SimpleImputer(strategy='mean')

    # Aplicar el método de imputación a la columna 'Age'
    df['Age_imputed'] = imputer.fit_transform(df[['Age']])

    # Guardar el conjunto de datos imputado si es necesario
    df.to_csv("dataset_imputed.csv", index=False)
    print("Valores perdidos en la columna 'Age' imputados exitosamente.")
else:
    print("No se encontraron valores perdidos en la columna 'Age'.")

# Graficar la distribución de la edad antes y después del proceso de imputación
plt.figure(figsize=(10, 5))

# Antes de la imputación
plt.subplot(1, 2, 1)
plt.hist(df['Age'], bins=20, color='blue', alpha=0.7)
plt.title('Antes de la imputación')
plt.xlabel('Age')
plt.ylabel('Frecuencia')

# Después de la imputación
plt.subplot(1, 2, 2)
plt.hist(df['Age_imputed'], bins=20, color='green', alpha=0.7)
plt.title('Después de la imputación')
plt.xlabel('Age (Imputado)')
plt.ylabel('Frecuencia')

plt.tight_layout()
plt.show()

# Mostrar los valores imputados
print("\nValores imputados en la columna 'Age':")
print(df[df['Age'].isnull()][['PassengerId', 'Age', 'Age_imputed']])
