contador = 0
contadorCiclo = 0

print("Ciclo while")  # El contador se imprime cuando es 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
while contadorCiclo < 5:
    while contador < 10:
        print(contador)
        contador += 1  # contador = contador + 1
    contador = 0
    contadorCiclo += 1

contador = 0

print("Ciclo for")  # El contador se imprime cuando es 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
for contador in range(0, 10):  # contador = contador + 1 es automático
    print(contador)

# Si quiero imprimir el contador del cero al 10
contador = 0

print("Ciclo while 0-10")  # El contador se imprime cuando es 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
while contador <= 10:
    print(contador)
    contador += 1

contador = 0

print("Ciclo for 0-10")  # El contador se imprime cuando es 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
for contador in range(0, 11):
    print(contador)
