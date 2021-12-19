from tkinter import *

# Functions


def add():
    print()


# UI (User interface)
window = Tk()
nombrePeluche = StringVar()
cantidadPeluche = IntVar()
precioPeluche = DoubleVar()

# Images
teemoIcon = PhotoImage(file='Teemo icon.png')

# Fonts
titleFont = ('Relate', 30)
widgetsFont = ('Dealerplate California', 20)
buttonsFont = ('Dealerplate California', 18)
buttonsHeight = 1
buttonsWidth = 10

# Main window
window.geometry("800x700")
window.title("Peluchitos.com")
window.iconphoto(False, teemoIcon)

# Labels
titleLabel = Label(window,
                   text="Peluchitos.com",
                   font=titleFont,
                   relief='groove').place(relx=0.5, y=50, anchor=CENTER)

nombreLabel = Label(window, text="Nombre del Peluche: ", font=widgetsFont).place(x=15, y=120)
nombreEntry = Entry(window, textvariable=nombrePeluche, font=widgetsFont).place(x=280, y=120)

cantidadLabel = Label(window, text="Cantidad del Peluche: ", font=widgetsFont).place(x=15, y=180)
cantidadEntry = Entry(window, textvariable=cantidadPeluche, font=widgetsFont).place(x=280, y=180)

precioLabel = Label(window, text="Precio del Peluche: ", font=widgetsFont).place(x=15, y=240)
precioEntry = Entry(window, textvariable=precioPeluche, font=widgetsFont).place(x=280, y=240)

AddButton = Button(window,
                   text="Agregar",
                   font=buttonsFont,
                   height=buttonsHeight,
                   width=buttonsWidth,
                   command=add,).place(relx=0.5, y=330, anchor=CENTER)

# Mainloop
window.mainloop()
