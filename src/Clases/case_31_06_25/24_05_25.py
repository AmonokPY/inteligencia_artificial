import numpy as np
import scipy as sp
import pandas as pd

# -------------------------------
# 1. Cargar los datos
# -------------------------------

# Opción 1: Cargar el CSV desde una URL (datos en línea)
df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/refs/heads/master/tips.csv")

# Opción 2: Cargar el CSV desde un archivo local
df_local = pd.read_csv(r"C:\Users\yuese\Downloads\tips.csv")

# Elegir cuál usar (en este caso usamos el archivo local)
df = df_local

# -------------------------------
# 2. Visualización básica
# -------------------------------

limite = 10
print(f"\n-- Primeros {limite} datos --\n")
print(df.head(limite))

print(f"\n-- Últimos {limite} datos --\n")
print(df.tail(limite))

# -------------------------------
# 3. Información de tipos de datos
# -------------------------------

print("\n-- Tipo de dato de la columna 'smoker' --")
print(df["smoker"].dtype)

# -------------------------------
# 4. Estadísticas descriptivas
# -------------------------------

print("\n-- Estadísticas generales --")
print(df.describe(include="all"))

# -------------------------------
# 5. Valores máximos y mínimos
# -------------------------------

print("\n-- Valores máximos por columna --")
print(df.max(numeric_only=True))

print("\n-- Valores mínimos por columna --")
print(df.min(numeric_only=True))

# -------------------------------
# 6. Promedios y medianas
# -------------------------------

print("\n-- Promedios (media) --")
print(df.mean(numeric_only=True))

print("\n-- Medianas --")
print(df.median(numeric_only=True))

# -------------------------------
# 7. Dimensiones del DataFrame
# -------------------------------

print("\n-- Forma del DataFrame (filas, columnas) --")
print(df.shape)

# -------------------------------
# 8. Muestra aleatoria de registros
# -------------------------------

print("\n-- Muestra aleatoria de 5 filas --")
print(df.sample(n=5))

# -------------------------------
# 9. eliminarr datos
# -------------------------------

df_clean = df.dropna()

print("\n-- DataFrame después de eliminar filas con valores faltantes --")
print(df_clean.head(10))

# -------------------------------
# 10. filtrar información
# -------------------------------

#Seleccionado solo sexo femenino

print("\n-- Filtrado por sex femenino--")

df_female = df[ df["sex"] =="Female"]

print(df_female.head())



