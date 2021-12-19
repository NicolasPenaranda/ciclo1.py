import pandas as pd

archivo = pd.read_csv(r'C:\Users\nicol\PycharmProjects\MisionTic\Clases MinTic\productos.csv', encoding="utf-8")
print(archivo.mode)
