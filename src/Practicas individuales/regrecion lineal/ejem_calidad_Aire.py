import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# 1. Cargar los datos desde la URL
url = "https://raw.githubusercontent.com/pandas-dev/pandas/refs/heads/main/doc/data/air_quality_no2.csv"
df = pd.read_csv(url)

# 2. Ver las primeras filas y columnas disponibles
print("Columnas:", df.columns)
print(df.head())

# 3. Eliminar valores faltantes
df = df.dropna()

# 4. Convertir la columna de fecha a tipo datetime (la columna se llama 'datetime', no 'date.utc')
df['datetime'] = pd.to_datetime(df['datetime'])

# 5. Crear nuevas variables temporales
df['hour'] = df['datetime'].dt.hour
df['day_of_week'] = df['datetime'].dt.dayofweek  # 0=Lunes, 6=Domingo

# 6. Selección de características y objetivo
# Construimos X e y para la estación de París
X = df[['hour', 'day_of_week']]
y = df['station_paris']

# 7. Separar en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 8. Crear y entrenar el modelo
modelo = LinearRegression()
modelo.fit(X_train, y_train)

# 9. Hacer predicciones
y_pred = modelo.predict(X_test)

# 10. Evaluar el modelo
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"\nEvaluación del modelo para 'station_paris':")
print(f"Error cuadrático medio (MSE): {mse:.2f}")
print(f"Coeficiente de determinación (R²): {r2:.2f}")

# 11. Visualización: Predicción vs Real
plt.figure(figsize=(8, 5))
sns.scatterplot(x=y_test, y=y_pred, alpha=0.6)
plt.xlabel("Valor Real de NO₂ - París")
plt.ylabel("Valor Predicho")
plt.title("Predicción de NO₂ en París vs Valor Real")

# Añadir línea de referencia perfecta
max_val = max(y_test.max(), y_pred.max())
min_val = min(y_test.min(), y_pred.min())
plt.plot([min_val, max_val], [min_val, max_val], 'r--')

plt.grid(True)
plt.show()

# Opcional: Mostrar coeficientes del modelo
print("\nCoeficientes del modelo:")
print(f"Intercepto: {modelo.intercept_:.2f}")
for i, col in enumerate(X.columns):
    print(f"{col}: {modelo.coef_[i]:.2f}")