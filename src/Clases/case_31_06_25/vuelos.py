import pandas as pd
vuelos = pd.read_csv(" https://raw.githubusercontent.com/mwaskom/seaborn-data/refs/heads/master/flights.csv")
# Seleccionando las filas que tienen por lo menos 1 valor faltante
print(vuelos[vuelos.isnull().any(axis=1)].head())