# Keyla Paola NC = 0033 | Fecha 4/nov/2026
import pandas as pd
import os

# URL del dataset público para leer datos de iris.csv
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
# Descargar y cargar el CSV
datos = pd.read_csv(url)

print(datos)
# Guardar una copia local en la carpeta datasets 
datos.to_csv("datasets/iris.csv", index=False)

# Explorar los datos
print("PRIMERAS 5 FILAS")
print(datos.head())
print(" ")
print("\\nCANTIDAD DE FILAS Y COLUMNAS")
print(datos.shape)
print(" ")
print("Mostrando Nombre De Las Columnas")
print("\\nNOMBRES DE LAS COLUMNAS")
print(datos.columns.tolist())
print(" ")
print("\\nINFORMACION DEL DATASET (punto de datos)")
print(datos.info())
print(" ")
print("\\nCARACTERISTICAS (X)  tumba la columna especies con drop")
X = datos.drop(columns=["species"])
print(X.head())
print(" ")
print("\\nVARIABLE OBJETIVO (y)")
y = datos["species"]
print(y.head())
print(" ")
print("\\nESPECIES REGISTRADAS con la opcion unica")
print(y.unique())
print("Keyla Paola NC = 0033 | Fecha 4/nov/2026")