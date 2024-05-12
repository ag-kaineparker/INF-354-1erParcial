import pandas as pd
from sklearn.preprocessing import OneHotEncoder
import matplotlib.pyplot as plt

# Cargar el archivo CSV en un DataFrame de Pandas
df = pd.read_csv("tested.csv", sep=";")
print(df.head())

# Graficar la columna 'Sex' antes de One-Hot Encoding
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.hist(df['Sex'], color='blue', alpha=0.7)
plt.title('Antes de One-Hot Encoding')
plt.xlabel('Sexo')
plt.ylabel('Frecuencia')

# Aplicar One-Hot Encoding a la columna 'Sex'
onehot_encoder = OneHotEncoder(drop='first', sparse=False)
sex_encoded = onehot_encoder.fit_transform(df[['Sex']])
sex_encoded_df = pd.DataFrame(sex_encoded, columns=['Sex_encoded'])
df = pd.concat([df, sex_encoded_df], axis=1)

# Contar la frecuencia de los valores codificados
sex_encoded_counts = df['Sex_encoded'].value_counts()
print(df.head())
# Graficar la columna 'Sex_encoded' después de One-Hot Encoding
plt.subplot(1, 2, 2)
plt.bar(sex_encoded_counts.index, sex_encoded_counts.values, color='green', alpha=0.7)
plt.xticks([0, 1], labels=['0','1' ])
plt.title('Después de One-Hot Encoding')
plt.xlabel('Sex_encoded')
plt.ylabel('Frecuencia')

plt.tight_layout()
plt.show()
