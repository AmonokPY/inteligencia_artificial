import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
import skfuzzy as fuzz

# Datos simulados de tareas anteriores
data = {
    'tipo_tarea': ['Petición', 'Evento', 'Reclamo', 'Petición', 'Reclamo', 'Evento'],
    'dias_restantes': [2, 5, 1, 0, 3, 7],
    'dependencia': ['Jurídica', 'Eventos', 'Atención', 'Jurídica', 'Atención', 'Eventos'],
    'se_retrasó': [1, 0, 1, 1, 0, 0]  # 1: sí se retrasó, 0: no
}

df = pd.DataFrame(data)

# Codificamos texto a números
le_tipo = LabelEncoder()
le_dep = LabelEncoder()
df['tipo_tarea_cod'] = le_tipo.fit_transform(df['tipo_tarea'])
df['dependencia_cod'] = le_dep.fit_transform(df['dependencia'])

# Variables independientes (X) y objetivo (y)
X = df[['tipo_tarea_cod', 'dias_restantes', 'dependencia_cod']]
y = df['se_retrasó']

# Entrenamos modelo
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
modelo = RandomForestClassifier()
modelo.fit(X_train, y_train)

# Nueva tarea ingresada por un funcionario
nueva_tarea = {
    'tipo_tarea': 'Reclamo',
    'dias_restantes': 1,
    'dependencia': 'Atención'
}

# Codificamos usando los label encoders entrenados
tarea_codificada = [
    le_tipo.transform([nueva_tarea['tipo_tarea']])[0],
    nueva_tarea['dias_restantes'],
    le_dep.transform([nueva_tarea['dependencia']])[0]
]

# Predicción
prediccion = modelo.predict([tarea_codificada])[0]
proba = modelo.predict_proba([tarea_codificada])[0][1]

# Alerta
if prediccion == 1:
    print(f"⚠️ Alerta: Esta tarea tiene alta probabilidad de retraso ({proba:.2%}). Tómala con prioridad.")
else:
    print("✅ Esta tarea está en buen tiempo.")
