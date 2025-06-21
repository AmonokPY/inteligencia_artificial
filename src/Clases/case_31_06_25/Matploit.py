#import os

# Asignar rutas correctas a TCL y TK
#os.environ['TCL_LIBRARY'] = r'C:\Users\yuese\AppData\Local\Programs\Python\Python313\tcl\tcl8.6'
#os.environ['TK_LIBRARY'] = r'C:\Users\yuese\AppData\Local\Programs\Python\Python313\tcl\tk8.6'

import matplotlib.pyplot as plt
import numpy as np

# Datos para graficar
x = np.linspace(0, 10, 100)
y = 4 + 1 * np.sin(2 * x)
x2 = np.linspace(0, 10, 25)
y2 = 4 + 1 * np.sin(2 * x2)

# Crear figura y ejes
fig, ax = plt.subplots()
ax.plot(x2, y2 + 2.5, 'x', markeredgewidth=2)  # Con X
ax.plot(x, y, linewidth=2.0)                   # Línea
ax.plot(x2, y2 - 2.5, 'o-', linewidth=2)       # Línea con puntos

# Configurar ejes
ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
       ylim=(0, 8), yticks=np.arange(1, 8))

# Mostrar ventana con gráfica
plt.show()
