
import pandas as pd
import numpy as np

# Cargar datos desde el archivo CSV exportado de la base de datos (ejemplo)
# Cambiar el nombre del archivo a tu archivo de datos
df = pd.read_csv('ad_campaign_data.csv')

# Verificar los primeros registros del dataframe
print("Primeros registros del dataframe:")
print(df.head())

# Limpieza de datos
# Eliminar filas con valores nulos
df_clean = df.dropna()

# Rellenar valores nulos en columnas específicas (por ejemplo, con la media de la columna)
# df['revenue'] = df['revenue'].fillna(df['revenue'].mean())

# Eliminar columnas no necesarias
df_clean = df_clean.drop(columns=['column_name_to_drop'])

# Corregir valores erróneos, por ejemplo, asegurarse de que las impresiones y clics sean valores positivos
df_clean['impressions'] = df_clean['impressions'].apply(lambda x: max(x, 0))
df_clean['clicks'] = df_clean['clicks'].apply(lambda x: max(x, 0))

# Verificar el resultado de la limpieza
print("Datos después de la limpieza:")
print(df_clean.head())

# Guardar el DataFrame limpio en un nuevo archivo CSV
df_clean.to_csv('ad_campaign_data_clean.csv', index=False)
