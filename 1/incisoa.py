# Leer el archivo CSV y almacenar los datos en una lista de listas
with open("tested.csv", "r") as file:
    lines = file.readlines()

# Eliminar el primer elemento que contiene los nombres de las columnas y separar los valores con ;
lines = [line.strip().split(";") for line in lines]
header = lines.pop(0)

# Transponer filas y columnas
data_transposed = list(zip(*lines))

# Función para calcular el último cuartil
def calculate_third_quartile(column_values):
    column_values = [float(value) for value in column_values if value.strip()]
    column_values.sort()
    if column_values:
        third_quartile_index = int(0.75 * len(column_values))
        return column_values[third_quartile_index]
    else:
        return None

# Función para calcular el percentil 80
def calculate_percentile_80(column_values):
    column_values = [float(value) for value in column_values if value.strip()]
    column_values.sort()
    if column_values:
        percentile_80_index = int(0.8 * len(column_values))
        return column_values[percentile_80_index]
    else:
        return None

# Calcular el último cuartil y el percentil 80 para cada columna
for column, column_values in zip(header, data_transposed):
    try:
        third_quartile = calculate_third_quartile(column_values)
        percentile_80 = calculate_percentile_80(column_values)
        print(f"Columna '{column}':")
        print(f"  Último cuartil (Q3): {third_quartile}")
        print(f"  Percentil 80: {percentile_80}\n")
    except ValueError:
        print("")
        
