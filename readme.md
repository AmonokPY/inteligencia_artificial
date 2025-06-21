
# Inteligencia Artificial – Proyecto Base

> Un proyecto de muestra en Python 3.12.6 para experimentar con modelos y pipelines de IA.

---

## 📋 Índice

1. [Descripción](#descripción)  
2. [Requisitos](#requisitos)  
3. [Instalación](#instalación)  
4. [Estructura del proyecto](#estructura-del-proyecto)  
5. [Uso](#uso)  
6. [Contribuir](#contribuir)  
7. [Licencia](#licencia)  

---

## 📖 Descripción

Este repositorio contiene el esqueleto de un proyecto de **Inteligencia Artificial** en Python 3.12.6.  
Incluye ejemplos de:

- Preparación de datos (preprocesamiento, limpieza).  
- Definición de modelos (scikit-learn, TensorFlow o PyTorch).  
- Entrenamiento y evaluación.  
- Exportación de modelos (pickle u ONNX).  
- Ejecución de inferencia.

Ideal para prototipos rápidos y como base para experimentación.

---

## ⚙️ Requisitos

- **Python** 3.12.6  
- **pip** (≥ 23.x)  
- Entorno virtual (recomendado)

---

## 🚀 Instalación

```bash
# 1. Clonar el repositorio
git clone https://github.com/AmonokPY/inteligencia_artificial.git
cd inteligencia_artificial

# 2. Crear y activar entorno virtual
# Linux/macOS
python3.12 -m venv .venv
source .venv/bin/activate

# Windows (PowerShell)
python -m venv .venv
.\.venv\Scripts\Activate

# 3. Instalar dependencias
pip install --upgrade pip
pip install -r requirements.txt

# 4. Verificar
python --version   # Debe mostrar Python 3.12.6
pip list           # Confirma paquetes instalados
