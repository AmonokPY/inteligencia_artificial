import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(style="whitegrid")
planets = sns.load_dataset("planets")
# Graficando cada objeto de forma individual
cmap = sns.cubehelix_palette(rot=-.2, as_cmap=True)
g = sns.relplot(data=planets,
    x="distance", y="orbital_period",
    hue="year", size="mass",
    palette=cmap, sizes=(10, 200),)
# Configurando ejes
g.set(xscale="log", yscale="log")
g.ax.xaxis.grid(True, "minor", linewidth=.25)
g.ax.yaxis.grid(True, "minor", linewidth=.25)
g.despine(left=True, bottom=True)
plt.show()