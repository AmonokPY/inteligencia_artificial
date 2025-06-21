import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Datos simulados
data = {
    'Modelos': [1, 2, 3, 4, 5],
    'Precio': [1500, 1800, 2100, 2400, 2700]
}

# Cargar datos
df = pd.DataFrame(data)

# Separar variables
X = df[['Modelos']]  # variable independiente (2D)
y = df['Precio']     # variable dependiente

# Crear y entrenar el modelo
modelo = LinearRegression()
modelo.fit(X, y)

# Valor a predecir
modelo_bici = 15
prediccion = modelo.predict([[modelo_bici]])
print(f"✅ El precio estimado para el modelo de bicicleta número {modelo_bici} es: ${prediccion[0]:.2f}")

# Generar valores desde el modelo 1 hasta el modelo 15
x_extendido = np.arange(1, modelo_bici + 1).reshape(-1, 1)
y_extendido = modelo.predict(x_extendido)

# Visualización
plt.scatter(X, y, color='blue', label='Datos Reales')  # puntos originales
plt.plot(x_extendido, y_extendido, color='red', label='Línea de Regresión extendida')  # línea completa

# Punto de predicción
plt.scatter(modelo_bici, prediccion, color='green', s=100, label='Predicción Modelo 15')
plt.text(modelo_bici, prediccion, f' ${prediccion[0]:.2f}', fontsize=9, verticalalignment='bottom')

# Estética
plt.xlabel('Número de Modelo de Bicicleta')
plt.ylabel('Precio Estimado ($)')
plt.title('Predicción de Precio por Modelo')
plt.legend()
plt.grid(True)
plt.show()
