# NO ELIMINAR LAS SIGUIENTES IMPORTACIONES, sirven para probar tu código en consola, y el funcionamiento del módulo csv respectivamente
#from pruebas import pruebas_codigo_estudiante
import csv

"""NOTAS: 
    -PARA ESTE RETO PUEDES PROBAR TU PROGRAMA, DANDO CLICK EN LA NAVE ESPACIAL
    -LA CONSOLA TE DARÁ INSTRUCCIONES SI PUEDES EVALUAR O NO TU CÓDIGO
"""

"""Inicio espacio para programar funciones propias"""


def obtener_concepto(promedio):
    if promedio < 200:
        return "MUY BAJO"
    elif 200 <= promedio < 300:
        return "BAJO"
    elif 300 <= promedio < 500:
        return "MEDIO"
    elif 500 <= promedio < 600:
        return "ALTO"
    elif promedio >= 600:
        return "MUY ALTO"


"""Fin espacio para programar funciones propias"""


def solucion():
    rows = []
    low = ["", 10000000]
    high = ["", -10000000]
    with open("./TSLA.csv") as file:
        old_file = csv.reader(file)
        for row in old_file:
            rows.append(row)
    with open("analisis_archivo.csv", "w") as file:
        new_file = csv.writer(file, delimiter="\t")
        new_file.writerow(["Fecha", "Concepto"])
        for row in rows[1:]:
            fecha = row[0]
            promedio = (float(row[4]))
            concepto = obtener_concepto(promedio)
            if promedio < low[1]:
                low[0] = fecha
                low[1] = promedio
            if promedio > high[1]:
                high[0] = fecha
                high[1] = promedio

            new_file.writerow([fecha, concepto])

    date_lowest, lowest_value, date_highest, highest_value = low[0], low[1], high[0], high[1]

    return date_lowest, lowest_value, date_highest, highest_value


"""
NO COLOCAR CÓDIGO FUERA DE LAS FUNCIONES QUE USTED CREE
Esta línea de código que sigue permite saber si su solución al ejercicio es correcto
Por favor NO ELIMINARLA, NO MODIFICARLA
"""
#pruebas_codigo_estudiante(solucion)
