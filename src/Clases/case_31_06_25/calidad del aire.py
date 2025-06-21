import os


import pandas as pd
import matplotlib.pyplot as plt


# Leyendo un archive de Calidad del aire
calidad_aire = pd.read_csv("https://raw.githubusercontent.com/pandas-dev/pandas/refs/heads/main/doc/data/air_quality_no2.csv")

#calidad_aire.plot() #Graficando todos los datos de Calidad del Aire

#calidad_aire["station_paris"].plot() #graficar estacion londres

#calidad_aire.plot.scatter(x="station_london", y="station_paris", alpha=0.1) # Comparando los valores de Londres vs Paris

axs = calidad_aire.plot.area(figsize=(12, 4),subplots=True)# Diagrama individual de las tres estaciones que miden Calidad del Aire

plt.show()