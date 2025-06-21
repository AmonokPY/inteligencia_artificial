import pandas as pd

# Cargar el archivo desde URL
df = pd.read_csv("https://raw.githubusercontent.com/Apress/data-analysis-and-visualization-using-python/master/Ch07/Salaries.csv")

# Salario mayor a 120000
print("\nSalario mayor a 120000\n")
df_salario = df[df["salary"] > 120000]
print(df_salario.head())

# Filtrar columnas 'rank' y 'salary'
print("\nFiltrar columnas 'rank' y 'salary'\n")
df_rank_salary = df[["rank", "salary"]]
print(df_rank_salary.head())

# Rango de filas de la 10 a la 19 (recuerda que el final es exclusivo)
print("\nRango de filas 10 a 19\n")
print(df[10:20])

# loc se usa para dterminar rangos de filas y columnas
print("\nRango de filas 10 a 19 y de las columnas rank y salary\n")
print(df.loc[10:20,["rank", "salary"]])

#iloc pa traer filas o culumnas con diferentes rangos
print("\nDe de fila 10 a la fila 20 me mestras los dados de todas las columnas menos la 1 y 2 \n")
print(df.iloc[10:20,[0, 3, 4,5]])