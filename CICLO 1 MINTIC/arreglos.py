#Definir una matriz con datos constantes   [filas][columnas]
import random

matriz = [[0,1,2,3],
          [1,2,3,4],
          [5,6,7,8]]

filas = len(matriz)
print(f'El número de filas es {filas}')

columnas = len(matriz[0])
print (f'El número de columnas es {columnas}')

#Acceso a una posición específica
print(matriz[1][2])

#imprimir los valores de la matriz uno por uno
print(matriz[0][0], end = ',')
print(matriz[0][1], end = ',')
print(matriz[0][2], end = ',')
print(matriz[0][3])

print(matriz[1][0], end = ',')
print(matriz[1][1], end = ',')
print(matriz[1][2], end = ',')
print(matriz[1][3])

#Entrada de datos de una matriz por un usuario
for i in range(filas):
    for j in range(columnas):
        matriz[i][j] = int(input())

#Creación de datos aleatorios
for i in range(filas):
    for j in range(columnas):
        matriz[i][j] = random.randint(1,100)

#Impresion de los datos de la matriz
for i in range(filas):
    for j in range(columnas):
        print(matriz[i][j], end=',')
    print()




