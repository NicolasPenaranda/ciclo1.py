from tkinter import *
import random
from tkinter import messagebox

raiz = Tk()
raiz.title("Ahorcado")
raiz.config(bg="#1B181C")
raiz.resizable(False, False)
listLetras = StringVar()
listLetrasUsadas = StringVar()
raiz.iconbitmap("game_icon.ico")
listLetters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
listLettersUsed = []
palabra_adiv = StringVar()
palabra_adiv2 = StringVar()
palabras = 'valor aprenderpython comida jugar python web programacion videojuegos computador perros mascota pies ' \
           'arbol libros dinero lapiz telefono amor discos software libre propio cancion collar sol luna juguete ' \
           'españa escuela universidad'.split()
palabraCorrecta = ""
palabraCifrada = []
mistakes = 0


def buscarPalabraAleat(listaPalabras):
    # Esta funcion nos devolvera una palabra elegida aleatoriamente.
    palabraAleatoria = random.randint(0, len(listaPalabras) - 1)
    return listaPalabras[palabraAleatoria]


def check():
    if palabra_adiv2.get().lower() == palabraCorrecta:
        palabra_adiv.set(palabraCorrecta)
        messagebox.showinfo("Winner", "Has ganado!")
    elif ''.join(palabraCifrada) == palabraCorrecta:
        messagebox.showinfo("Winner", "Has ganado!")
    elif len(palabra_adiv2.get()) == 1:
        comparar()


def imagenes():
    if mistakes == 1:
        imageLabel1 = Label(miFrame,
                            image=miImagen1, borderwidth=0, highlightthickness=0
                            ).grid(row=2, column=2, padx=10, columnspan=5, rowspan=5)
    elif mistakes == 2:
        imageLabel2 = Label(miFrame,
                            image=miImagen2, borderwidth=0, highlightthickness=0
                            ).grid(row=2, column=2, padx=10, columnspan=5, rowspan=5)
    elif mistakes == 3:
        imageLabel3 = Label(miFrame,
                            image=miImagen3, borderwidth=0, highlightthickness=0
                            ).grid(row=2, column=2, padx=10, columnspan=5, rowspan=5)
    elif mistakes == 4:
        imageLabel4 = Label(miFrame,
                            image=miImagen4, borderwidth=0, highlightthickness=0
                            ).grid(row=2, column=2, padx=10, columnspan=5, rowspan=5)
    elif mistakes == 5:
        imageLabel5 = Label(miFrame,
                            image=miImagen5, borderwidth=0, highlightthickness=0
                            ).grid(row=2, column=2, padx=10, columnspan=5, rowspan=5)
    elif mistakes == 6:
        imageLabel6 = Label(miFrame,
                            image=miImagen6, borderwidth=0, highlightthickness=0
                            ).grid(row=2, column=2, padx=10, columnspan=5, rowspan=5)
    elif mistakes == 7:
        imageLabel7 = Label(miFrame,
                            image=miImagen7, borderwidth=0, highlightthickness=0
                            ).grid(row=2, column=2, padx=10, columnspan=5, rowspan=5)


def imprimir():
    palabra = ""
    for i in palabraCifrada:
        palabra += i + " "
    palabra_adiv.set(palabra)


def empezar():
    global palabraCorrecta
    global palabraCifrada
    palabraCorrecta = buscarPalabraAleat(palabras)
    for i in palabraCorrecta:
        palabraCifrada.append("_")
    listLetras.set(listLetters)
    imprimir()
    switchButtonState()
    print(palabraCorrecta)


def comparar():
    global palabraCifrada
    global mistakes
    global listLetrasUsadas
    if palabra_adiv2.get() in palabraCorrecta:
        cont = 0
        for i in palabraCorrecta:
            if palabra_adiv2.get() == i:
                palabraCifrada[cont] = palabra_adiv2.get()
            cont += 1
        if palabra_adiv2.get() in listLettersUsed:
            messagebox.showinfo("Advertencia", f"La letra {palabra_adiv2.get()} ya se uso, intenta con otra")
        else:
            listLettersUsed.append(palabra_adiv2.get())
            listLetrasUsadas.set(listLettersUsed)
            listLetters.remove(palabra_adiv2.get())
            listLetras.set(listLetters)
        imprimir()
        palabra_adiv2.set("")
    else:
        if palabra_adiv2.get() in listLettersUsed:
            messagebox.showinfo("Advertencia", f"La letra {palabra_adiv2.get()} ya se uso, intenta con otra")
        else:
            listLettersUsed.append(palabra_adiv2.get())
            listLetrasUsadas.set(listLettersUsed)
            listLetters.remove(palabra_adiv2.get())
            listLetras.set(listLetters)
            mistakes += 1
            messagebox.showinfo("Fallaste", f"La letra no se encuentra en la palabra. llevas {mistakes} intentos")
        palabra_adiv2.set("")
    imagenes()
    if mistakes > 6:
        finishgame()


def finishgame():
    global palabraCorrecta
    global palabraCifrada
    global listLetters
    global listLettersUsed
    global mistakes
    messagebox.showinfo("Finalizado", f"La palabra era {palabraCorrecta}. ")
    mistakes = 0
    palabraCorrecta = ""
    palabraCifrada = []
    palabra_adiv.set("")
    palabra_adiv2.set("")
    listLetters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u', 'v', 'w', 'x', 'y', 'z']
    listLettersUsed = []
    listLetrasUsadas.set(listLettersUsed)
    listLetras.set(listLetters)
    imageLabel = Label(miFrame,
                       image=miImagen, borderwidth=0, highlightthickness=0
                       ).grid(row=2, column=2, padx=10, columnspan=5, rowspan=5)
    switchButtonState()


def switchButtonState():
    if startButton["state"] == "normal":
        startButton.config(state=DISABLED)
        checkButton.config(state=ACTIVE)
        finishButton.config(state=ACTIVE)
    elif finishButton["state"] == "normal":
        startButton.config(state=ACTIVE)
        checkButton.config(state=DISABLED)
        finishButton.config(state=DISABLED)


miFrame = Frame(raiz,  # Ventana que va a contener el frame
                bg="#FFFFFF",  # Background color codigo html --> RGB
                height=600,  # tamaño alto
                width=600,  # tamaño ancho
                padx=10,  # margen eje x
                pady=10,  # margen eje x
                cursor='arrow')  # especifica el cursor del mouse.
miFrame.pack()

miImagen = PhotoImage(file="ahorcado1.png")
imageLabel = Label(miFrame,
                   image=miImagen, borderwidth=0, highlightthickness=0
                   ).grid(row=2, column=2, padx=10, columnspan=5, rowspan=5)
miImagen1 = PhotoImage(file="ahorcado2.png")
miImagen2 = PhotoImage(file="ahorcado3.png")
miImagen3 = PhotoImage(file="ahorcado4.png")
miImagen4 = PhotoImage(file="ahorcado5.png")
miImagen5 = PhotoImage(file="ahorcado6.png")
miImagen6 = PhotoImage(file="ahorcado8.png")
miImagen7 = PhotoImage(file="ahorcado9.png")

miLabel = Label(miFrame,
                text="Juego del ahorcado", bg="#FFFFFF",
                fg="black",
                font=("Comic sans MS", 20, "bold")).grid(row=0, column=0, pady=20, columnspan=4, sticky="e")
miLabel2 = Label(miFrame,
                 text="Escriba la palabra completa o una letra: ", bg="#FFFFFF",
                 fg="black",
                 font=("Comic sans MS", 10, "bold")).grid(row=1, column=0, sticky="w", pady=5)
miLabel3 = Label(miFrame,
                 text="Letras disponibles", bg="#FFFFFF",
                 fg="black",
                 font=("Comic sans MS", 10, "bold")).grid(row=3, column=0, sticky="w", pady=5)
miLabel4 = Label(miFrame,
                 text="Letras Usadas",
                 fg="black", bg="#FFFFFF",
                 font=("Comic sans MS", 10, "bold")).grid(row=5, column=0, sticky="w", pady=5)

palabraAdivinada = Entry(miFrame,
                         width=35, textvariable=palabra_adiv, borderwidth=1, highlightthickness=1, state='disabled',
                         font=("Comic sans MS", 10, "bold")).grid(row=2, column=0, pady=10, sticky="nw")

palabraAdiWrite = Entry(miFrame,
                        width=35, textvariable=palabra_adiv2, borderwidth=1, highlightthickness=1,
                        font=("Comic sans MS", 10, "bold")).grid(row=2, column=0, pady=5, sticky="sw")

pantalla_letras = Entry(miFrame,
                        justify="left", bg="#FFFFFF", state='disabled', width=40,
                        textvariable=listLetras,
                        font=("Helvetica", 10), borderwidth=1, highlightthickness=1
                        ).grid(row=4, column=0)

pantalla_letras_usadas = Entry(miFrame,
                               justify="right", bg="#FFFFFF", state='disabled', width=40,
                               textvariable=listLetrasUsadas,
                               font=("Helvetica", 10), borderwidth=1, highlightthickness=1
                               ).grid(row=6, column=0)

startButton = Button(miFrame,
                     text="Start", state=ACTIVE,
                     command=lambda: empezar(),
                     bg="#020002", fg="#E3E0E3", activeforeground="#E3E0E3", activebackground="#020002",
                     font=("Helvetica", 10, "bold"), borderwidth=0)
startButton.grid(row=7, column=0, sticky="w")

checkButton = Button(miFrame,
                     text="Check", state=DISABLED,
                     command=lambda: check(),
                     bg="#020002", fg="#E3E0E3", activeforeground="#E3E0E3", activebackground="#020002",
                     font=("Helvetica", 10, "bold"), borderwidth=0)
checkButton.grid(row=7, column=0)
finishButton = Button(miFrame,
                      text="Finish", state=DISABLED,
                      command=lambda: finishgame(),
                      bg="#020002", fg="#E3E0E3", activeforeground="#E3E0E3", activebackground="#020002",
                      font=("Helvetica", 10, "bold"), borderwidth=0)
finishButton.grid(row=7, column=0, sticky="e")
raiz.mainloop()
