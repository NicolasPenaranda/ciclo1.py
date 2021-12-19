#Paso 1. Instalación de la librería

#Paso 2. Importar librería y crear una ventana principal y mainloop()
from tkinter import *

main_window = Tk()
main_window.title("Probando Interfaces de usuario")
#main_window.mainloop()

#Paso 3. Frames / Marco
main_frame = Frame(main_window,         #Ventana que va a contener el frame
                   bg="#FFFFFF",        #background color código html - > RGB Red Green Blue
                   height = 500,        #tamaño de alto
                   width = 500,         #ancho
                   padx = 50,           #margen en el eje x
                   pady = 50,           #margen en el eje y
                   cursor = 'arrow')      #especifica el cursor que le quiero poner al mouse -> dot, arrow

main_frame.pack()                       #se instancia en la interfaz
#main_window.mainloop()

#Paso 4. Labels -> Se utiliza para escribir textos, titulos, etiquetas, etc

title_label = Label(main_frame,            #Frame que contendrá el label
                    text = "Hola Interfaces de Usuario",    #Text que se va a visualizar
                    font = ('Arial',15),    #tipo de ltra y tamaño
                    fg = '#000000',         #color de la letra
                    justify = CENTER,
                    bg = '#FFFFFF')       #Alineación LEFT, RIGHT, CENTER
title_label.pack()
#main_window.mainloop()

#Paso 5. PhotoImage -> Insertar imagenes en el frame que se esta trabajando
"""imagen = PhotoImage(file = 'python_img.png')
img_label = Label(main_frame,
                  image = imagen,
                  bg = '#FFFFFF')       #se pone una imagen a visualizar
img_label.pack()"""
#main_window.mainloop()

#paso 6. Button

def accion_button():
    global boton_text
    if boton_text == "Hola":
        boton_text = "Click"
    else:
        boton_text = "Hola"
    boton.config(text = boton_text)

boton_text = "Hola"
boton = Button(main_frame,
               text = boton_text,   #text coloca el texto al boton
               bg = "#00FFFF",  #color de fondo
               fg = "#FF0000",  #color de la letra
               command = accion_button)     #funcion que se ejecuta al dar click al botón
boton.pack()
#main_window.mainloop()

#Paso 7 -> Posicionamiento se utiliza .place(x = posx, y= posy)

ventana = Tk()
ventana.title("Posicionamiento")
ventana.geometry("400x200")
boton = Button(ventana, text="Primer Widget").place(x=10, y=10)
etiqueta = Label(ventana, text= "Segundo Widget").place(x=200, y=10)
etiqueta2 = Label(ventana, text= "tercer Widget").place(x=10, y = 60)
etiqueta3 = Label(ventana, text= "cuarto Widget").place(x=200, y = 60 )
#ventana.mainloop()

#ejercicio1 Ubicar un Label "Dame click para saludar" y un boton al dar click saluda en consola
#"un label "Desde aqui minimizamos" y al dar click en el botón se minimiza la ventana

def saludo():
    print("Hola a todos")

def minimizar():
    ventana.iconify()

ventana = Tk()
ventana.title("Ejercicio Número 1")
ventana.geometry("400x200")
saludarLabel = Label(ventana, text="Desde aquí saludamos").place(x=30, y=50)
minimizarLabel = Label(ventana, text="Desde aquí minimizamos").place(x=30, y=100)
saludarButton = Button(ventana, text="Dame click para saludar", command=saludo).place(x=200, y=50)
minimizarButton = Button(ventana, text= "Dame click para minimizar", command=minimizar).place(x=200, y=100)

#ventana.mainloop()

#Paso 8- Entradas de textos

ventana = Tk()
ventana.geometry("200x100")
ventana.title("Entrada de texto")
textbox = Entry(ventana).place(x=10, y=10)
#ventana.mainloop()

#Variables de control: Son objetos especiales que se asocian a los widgets para almacenar valores y
#facilitar su disponibilidad para otras partes del programa
#entero = IntVar()
#cadena = StringVar()
#boolean = BooleanVar()
#flotante = FloatVar()
#Ej dato = IntVar(value = 4)
#Método set para asignar un valor Ej dato.set(43)
#Método get para obtener el valor Ej dato.get()

#Ejercicio Formulario que reciba nombres, primer apellido y segundo apellido
def saludar():
    print(f'Hola: {nombre.get()} {primerApellido.get()} {segundoApellido.get()}')

ventana = Tk()
ventana.title("Entrada de datos")
ventana.geometry("400x400")

nombre = StringVar()
primerApellido = StringVar()
segundoApellido = StringVar()

nombreLabel = Label(ventana, text="Escriba su nombre: ").place(x=10, y=10)
nombreEntry = Entry(ventana, textvariable=nombre).place(x=200, y=10)

primerApellidoLabel = Label(ventana, text="Escriba su primer apellido: ").place(x=10, y=120)
primerApellidoEntry = Entry(ventana, textvariable=primerApellido).place(x=200, y=120)

segundoApellidoLabel = Label(ventana, text="Escriba su segundo apellido: ").place(x=10, y=230)
segundoApellidoEntry = Entry(ventana, textvariable=segundoApellido).place(x=200, y=230)

saludarButton = Button(ventana, text="Saludar", command=saludar).place(relx=0.5, y=340, anchor= CENTER)

ventana.mainloop()









