# Llamando librería de Plotly
import plotly.express as px
# Cargando base de datos
df = px.data.gapminder()
# Definiendo gráfico con plotly
fig = px.scatter(df.query("year==2007"), x="gdpPercap", y="lifeExp",
          size="pop", color="continent",
                 hover_name="country", log_x=True, size_max=60)
fig.write_html("ploty_ejercicio2.html")
import webbrowser
webbrowser.open("ploty_ejercicio2.html")
