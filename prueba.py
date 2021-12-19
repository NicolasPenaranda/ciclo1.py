import turtle

moffy = turtle.Turtle()
resp = input("qué figura deseas hacer: ")
color_p = input("qué color deseas usar: ")

if resp == "cuadrado":
    moffy.color(color_p)
    i = 0
    while i < 4:
        moffy.forward(100)
        moffy.right(90)
        i += 1
    turtle.done()
elif resp == "triangulo":
    moffy.color(color_p)
    i = 0
    while i < 3:
        moffy.forward(-100)
        moffy.right(120)
        i += 1
    turtle.done()
