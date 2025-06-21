from bokeh.io import output_file, show
from bokeh.plotting import figure

output_file("grafico.html")  # Genera un archivo HTML con el gráfico

x = [1, 2, 3, 4, 5]
y1 = [6, 7, 2, 4, 5]
y2 = [2, 3, 4, 5, 6]
y3 = [4, 5, 5, 7, 2]

p = figure(title="Multiple glyphs example", x_axis_label="x", y_axis_label="y")
p.line(x, y1, legend_label="Temp.", color="#004488", line_width=3)
p.line(x, y2, legend_label="Rate", color="#906c18", line_width=3)
p.scatter(x, y3, legend_label="Objects", color="#bb5566", size=16)

show(p)  # Abre el archivo HTML con el gráfico en tu navegador

