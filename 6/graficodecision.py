import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.metrics import accuracy_score
import graphviz

# Cargar el conjunto de datos
data = pd.read_csv("tested.csv", sep=";")

# Eliminar filas con valores faltantes
data.dropna(inplace=True)

# Seleccionar características (X) y variable objetivo (y)
X = data[['Pclass', 'Sex', 'Age', 'Fare', 'Embarked']]
y = data['Survived']

# Convertir variables categóricas en variables dummy
X = pd.get_dummies(X)

# Dividir el conjunto de datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=60)

# Crear el clasificador de árbol de decisión con una profundidad de por lo menos 3 niveles
clf = DecisionTreeClassifier(max_depth=5)

# Entrenar el clasificador
clf.fit(X_train, y_train)

# Predecir en el conjunto de prueba
y_pred = clf.predict(X_test)

# Calcular la precisión
accuracy = accuracy_score(y_test, y_pred)
print("Precisión del modelo en el conjunto de prueba:", accuracy)

# Exportar el árbol de decisión en formato Graphviz
dot_data = export_graphviz(clf, out_file=None, filled=True, feature_names=X.columns, class_names=['Not Survived', 'Survived'])

# Visualizar el árbol de decisión
graph = graphviz.Source(dot_data)
graph.render("decision_tree")  # Optional: Save the tree as PDF or PNG
graph.view()
