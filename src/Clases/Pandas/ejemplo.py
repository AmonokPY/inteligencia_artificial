import folium

# Crear el mapa centrado en Bogotá
mapa = folium.Map(location=[4.7110, -74.0721], zoom_start=12)

# Agregar un marcador
folium.Marker([4.7110, -74.0721], popup="Bogotá").add_to(mapa)

# Guardar el mapa en un archivo HTML
mapa.save("mapa_bogota.html")

print("Mapa guardado como 'mapa_bogota.html'")
