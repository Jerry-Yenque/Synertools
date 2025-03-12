import pandas as pd

# Cargar el archivo CSV
df = pd.read_csv("errors.csv")  # Reemplaza con la ruta de tu archivo

# Sumar la columna "Subtraction"
total_subtraction = df["Subtraction"].sum()

# Mostrar el resultado
print("Total de Subtraction:", total_subtraction)


# import pandas as pd

# # Cargar el archivo CSV
# df = pd.read_csv("errors.csv")  # Reemplaza con la ruta de tu archivo

# # Contar positivos y negativos
# positivos = (df["Subtraction"] > 0).sum()
# negativos = (df["Subtraction"] < 0).sum()

# # Mostrar los resultados
# print("Cantidad de registros con Subtraction positivo:", positivos)
# print("Cantidad de registros con Subtraction negativo:", negativos)
