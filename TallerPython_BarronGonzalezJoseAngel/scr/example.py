#Ejemplo del taller, leer archivos excel
import pandas as pd
import numpy as np

df = pd.read_excel('datos.xlsx')
df.head()

df['prom'] = df[['Parcial 1', 'Parcial 2', 'Parcial 3']].mean(axis=1)
df['estatus'] = np.where(df['prom'] >= 7, 'Aprobado', 'Reprobado')

df.to_excel('datos_mod.xlsx', index=False)
