import pandas as pd
import numpy as np
dict_caracteristicas = {'apellido':['Ospina', 'Zapata', 'Falcao', 'Cuadrado', 'Rodriguez'],
                       'altura':[183.0,187.0,177.0,179.0,180.0],
                       'peso':[80.0,82.0,72.0,72.0,75.0]}

seleccionColombia = pd.DataFrame(dict_caracteristicas,index=[1, 2, 9, 11, 10])

print (seleccionColombia)