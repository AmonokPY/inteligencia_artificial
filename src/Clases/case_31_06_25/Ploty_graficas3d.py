# Llamando librerías
import plotly.graph_objects as go
import pandas as pd
# Leyendo datos
z_data = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/api_docs/mt_bruno_elevation.csv')
# Definiendo gráficos con Plotly
fig = go.Figure(data=[go.Surface(z=z_data.values)])

fig.update_layout(title=dict(text='Mt Bruno Elevation'), autosize=False,
                  width=500, height=500,
                  margin=dict(l=65, r=50, b=65, t=90))
fig.write_html("ploty_graficas3d.html")
import webbrowser
webbrowser.open("ploty_graficas3d.html")