import pandas as pd

print("\n-- crear nuevo DataFrame --")
df = pd.DataFrame({
    'Animal': ['Falcon', 'Falcon', 'Parrot', 'Parrot'],
    'Max Speed': [380., 370., 24., 26.]
})

print(df)

# Agrupar y sacar media
print("\n--  DataFrame para sacar media y agrupar--")
print(df.groupby(['Animal'])[['Max Speed']].mean())
