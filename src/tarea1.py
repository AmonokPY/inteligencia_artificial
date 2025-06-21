import matplotlib.pyplot as plt
import numpy as np

# Crear la figura y los subgráficos
fig = plt.figure(figsize=(15, 5))

# --- 1D: Vector ---
ax1 = fig.add_subplot(1, 3, 1)
vector = np.array([1, 2, 3, 4, 5])
ax1.scatter(range(len(vector)), [0]*len(vector), c='skyblue', s=500, edgecolors='black')
for i, val in enumerate(vector):
    ax1.text(i, 0, str(val), ha='center', va='center', fontsize=12)
ax1.set_title("1D – Vector (eje X)", fontsize=14)
ax1.set_xlim(-1, len(vector))
ax1.set_ylim(-1, 1)
ax1.axis('off')
ax1.annotate('→', xy=(0.5, 0.2), xytext=(-0.5, 0.2), fontsize=20)

# --- 2D: Matriz ---
ax2 = fig.add_subplot(1, 3, 2)
matriz_2d = np.array([[1, 2], [3, 4]])
for i in range(2):
    for j in range(2):
        ax2.scatter(j, -i, c='lightgreen', s=1200, edgecolors='black')
        ax2.text(j, -i, str(matriz_2d[i, j]), ha='center', va='center', fontsize=14)
ax2.set_title("2D – Matriz (ejes X, Y)", fontsize=14)
ax2.set_xlim(-0.5, 2)
ax2.set_ylim(-2, 0.5)
ax2.axis('off')
ax2.annotate('→ X', xy=(1.5, 0.2), xytext=(0.5, 0.2), fontsize=12, arrowprops=dict(arrowstyle="->"))
ax2.annotate('↓ Y', xy=(-0.3, -1.5), xytext=(-0.3, -0.5), fontsize=12, arrowprops=dict(arrowstyle="->"))

# --- 3D: Matriz tridimensional ---
ax3 = fig.add_subplot(1, 3, 3, projection='3d')
matriz_3d = np.array([
    [[1, 2],
     [3, 4]],
    
    [[5, 6],
     [7, 8]]
])

colors = ['lightcoral', 'lightskyblue']
for z in range(2):  # capas (Z)
    for y in range(2):  # filas (Y)
        for x in range(2):  # columnas (X)
            ax3.bar3d(x, y, -z, 1, 1, 1, color=colors[z], alpha=0.6, edgecolor='black')
            ax3.text(x + 0.5, y + 0.5, -z + 0.5, str(matriz_3d[z, y, x]), color='black', ha='center', va='center', fontsize=10)

ax3.set_title("3D – Matriz tridimensional (ejes X, Y, Z)", fontsize=14)
ax3.set_xticks([0.5, 1.5])
ax3.set_yticks([0.5, 1.5])
ax3.set_zticks([-0.5, -1.5])
ax3.set_xlabel("X (columnas)")
ax3.set_ylabel("Y (filas)")
ax3.set_zlabel("Z (capas)")
ax3.view_init(elev=20, azim=235)

plt.tight_layout()
plt.show()
