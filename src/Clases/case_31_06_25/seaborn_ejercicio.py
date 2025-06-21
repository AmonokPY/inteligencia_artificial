import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="darkgrid")

# Cargando datos para graficar
fmri = sns.load_dataset("fmri")

# Graficando las series de tiempo
sns.lineplot(x="timepoint", y="signal",
             hue="region", style="event",
             data=fmri)

# Mostrar la gráfica
plt.show()
