import pandas as pd

# 1. Leer el CSV (ajusta el separador si es necesario, aquí se asume que es tabulador)
df = pd.read_csv(r"data\input\Receipts.csv", sep="\t")

# 2. Extraer la parte numérica del campo "number"
# Se asume que el formato es "B908-00462090": se separa por el guion y se convierte a entero
df['num'] = df['number'].apply(lambda x: int(x.split('-')[1]))

duplicados = df[df.duplicated(subset=['number'], keep=False)]

# 3. Ordenar el DataFrame según la parte numérica en orden ascendente
df_sorted = df.sort_values(by='num').reset_index(drop=True)
num_min = df_sorted['num'].min()
num_max = df_sorted['num'].max()
print(f"min {num_min}")
print(f"max {num_max}")
todos_los_numeros = set(range(num_min, num_max + 1))
numeros_existentes = set(df_sorted['num'])
numeros_faltantes = sorted(list(todos_los_numeros - numeros_existentes))

print("Números faltantes en la secuencia:")
print(numeros_faltantes)

if not duplicados.empty:
    print("\n🚨 Números duplicados en 'number':")
    print(duplicados)
else:
    print("\n✅ No hay números duplicados en 'number'.")
