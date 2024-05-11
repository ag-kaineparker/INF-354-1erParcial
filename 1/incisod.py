# -*- coding: utf-8 -*-
"""
Created on Fri May 10 19:46:47 2024

@author: Administrador
"""
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt


# Cargar el archivo CSV en un DataFrame de Pandas
df = pd.read_csv("tested.csv", sep=";")

# Crear un histograma de la columna 'Age'
plt.hist(df['Age'].dropna(), bins=20, color='skyblue', edgecolor='black')

# Agregar etiquetas y título
plt.xlabel('Edad')
plt.ylabel('Frecuencia')
plt.title('Distribución de Edades')

# Mostrar la gráfica
plt.show()

# Crear un histograma de la columna 'Fare' con un rango específico en el eje x
plt.hist(df['Fare'].dropna(), bins=80, color='lightgreen', edgecolor='black')

# Establecer el rango del eje x
plt.xlim(0, 120)  # Por ejemplo, limitar el rango de x de 0 a 100

# Agregar etiquetas y título
plt.xlabel('Tarifa')
plt.ylabel('Frecuencia')
plt.title('Distribución de Tarifas')

# Mostrar la gráfica
plt.show()