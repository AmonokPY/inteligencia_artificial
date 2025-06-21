import pandas as pd
## crear base de datos con datos que ya tengo

#edades_familia = pd.Series(
#    ["mamá", "papá", "tatis", "deivith", "nana", "yoyo"],
#   index=[43, 44, 12, 11, 21, 18]
#)


#de diccionario a base de datos
edades_familia={43:"mamá",44:"papá",12:"tatis"}
edades_familia = pd.Series(edades_familia)
print(edades_familia.head(3))