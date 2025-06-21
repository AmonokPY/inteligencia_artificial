import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report,
    roc_curve,
    roc_auc_score
)

# Paso 1: Datos simulados
data = {
    'Edad':     [18, 22, 30, 35, 40, 45, 50, 55, 60, 65],
    'Ingreso':  [1000, 1200, 2000, 2500, 3000, 3200, 4000, 4200, 4500, 4800],
    'Visitó':   [1, 1, 1, 1, 1, 0, 0, 1, 1, 0],
    'Compró':   [0, 0, 1, 1, 1, 0, 0, 1, 1, 0]
}
df = pd.DataFrame(data)

# Paso 2: Separar variables
X = df[['Edad', 'Ingreso', 'Visitó']]
y = df['Compró']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Paso 3: Modelo
modelo = LogisticRegression()
modelo.fit(X_train, y_train)
y_pred = modelo.predict(X_test)
y_proba = modelo.predict_proba(X_test)[:, 1]  # Probabilidad de clase positiva

# Paso 4: Matriz de confusión (Gráfico)
cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(6, 4))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
plt.title("📊 Matriz de Confusión")
plt.xlabel("Predicción")
plt.ylabel("Real")
plt.show()

# Paso 5: Curva ROC
fpr, tpr, _ = roc_curve(y_test, y_proba)
auc = roc_auc_score(y_test, y_proba)

plt.figure(figsize=(6, 4))
plt.plot(fpr, tpr, label=f"AUC = {auc:.2f}", color='darkorange')
plt.plot([0, 1], [0, 1], '--', color='gray')
plt.xlabel("Tasa de Falsos Positivos")
plt.ylabel("Tasa de Verdaderos Positivos")
plt.title("🔍 Curva ROC")
plt.legend()
plt.grid(True)
plt.show()

# Paso 6: Gráfico de distribución de probabilidades
plt.figure(figsize=(6, 4))
sns.histplot(y_proba, bins=10, kde=True, color='green')
plt.title("📈 Distribución de Probabilidades de Compra")
plt.xlabel("Probabilidad de Clase 1 (Compra)")
plt.ylabel("Cantidad de Usuarios")
plt.grid(True)
plt.show()
