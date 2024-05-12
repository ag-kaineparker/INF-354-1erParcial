import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Cargar el conjunto de datos
data = pd.read_csv("tested.csv", sep=";")

# Eliminar filas con valores faltantes
data.dropna(inplace=True)
print(data.head())

# Seleccionar características (X) y variable objetivo (y)
X = data[['Pclass', 'Sex', 'Age', 'Fare', 'Embarked']]
y = data['Survived']

# Eliminar la columna 'Embarked' antes de convertir variables categóricas en variables dummy
if 'Embarked' in X.columns:
    X = X.drop(columns=['Embarked'])
#Embarked se divide en Q S y C , no se imprime por espacio en la impresion

# Convertir variables categóricas en variables dummy
X = pd.get_dummies(X)

# Dividir el conjunto de datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=60)

# Imprimir los datos del conjunto de prueba
print("\nDatos del conjunto de prueba (sin 'Embarked'):")
print(X_test.head())

# Crear el clasificador de árbol de decisión con una profundidad de por lo menos 3 niveles
clf = DecisionTreeClassifier(max_depth=5)

# Entrenar el clasificador
clf.fit(X_train, y_train)

# Predecir en el conjunto de prueba
y_pred = clf.predict(X_test)

# Calcular la precisión
accuracy = accuracy_score(y_test, y_pred)
print("\nPrecisión del modelo en el conjunto de prueba:", accuracy)

# Verificar algunas predicciones
print("\nAlgunas predicciones:")
for i in range(7):
    print("Predicción, Sobrevivio?:", y_pred[i], "Realidad, Sobrevivio?:", y_test.iloc[i])
