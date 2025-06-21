import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Datos simulados
data = {
    'Años_Experiencia': [1, 2, 3, 4, 5],
    'Ingreso_Mensual': [1500, 1800, 2100, 2400, 2700]
}

# Cargar datos
df = pd.DataFrame(data)

# Separar variables
X = df[['Años_Experiencia']]  # variable independiente (2D)
y = df['Ingreso_Mensual']     # variable dependiente

# Crear y entrenar el modelo
modelo = LinearRegression()
modelo.fit(X, y)

# Hacer predicción para 6 años de experiencia
prediccion = modelo.predict([[6]])
print(f"Ingreso estimado para 6 años de experiencia: ${prediccion[0]:.2f}")

# Visualizar
plt.scatter(X, y, color='blue', label='Datos Reales')
plt.plot(X, modelo.predict(X), color='red', label='Línea de Regresión')
plt.xlabel('Años de Experiencia')
plt.ylabel('Ingreso Mensual')
plt.title('Regresión Lineal')
plt.legend()
plt.grid(True)
plt.show()
