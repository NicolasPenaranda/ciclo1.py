
import turtle
lampara = turtle.Turtle()

inputFigura = input("que figura vas a usar? (triangulo, cuadrado): ")
inputColor = input("que color vas a usar? (digita el nombre de un color en inglés):")

# triangulo
if inputFigura == "triangulo":
    lampara.color(inputColor)               # establece el color de la figura
    lampara.begin_fill()                    # inicia el relleno de la figura
    i = 0                                   # i -> Es lo mismo que contador, lo puedo declarar en el mismo if
    while i < 2:                            # mientras i sea menor a 2:
        lampara.forward(-100)               # se mueve forward -100 para que la punta del triangulo mire hacia arriba
        lampara.right(120)                  # se mueve right 120 para formar el triángulo
        i += 1                              # suma 1 a i para que el ciclo no sea infinito, y termine a las 2 iteraciones
    lampara.end_fill()                      # termina de rellenar el triángulo
    turtle.done()

# cuadrado
elif inputFigura == "cuadrado":             # lo mismo que el triángulo
    lampara.color(inputColor)               # establece su color
    lampara.begin_fill()                    # relleno
    i = 0                                   # declaramos el contador i
    while i < 4:                            # mientras i sea menor a 4:
        lampara.forward(90)                 # se mueve 90 forward
        lampara.right(90)                   # se mueve 90 right, para hacer el cuadrado
        i += 1                              # importante adicionar 1 al contador, para que el ciclo no sea infinito
    lampara.end_fill()
    turtle.done()
