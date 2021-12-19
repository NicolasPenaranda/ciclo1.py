from tkinter import *
from tkinter import messagebox


# Functions
def emptyLists():
    if not rowA:
        return False
    elif not rowB:
        return False
    elif not rowC:
        return False
    elif not rowD:
        return False
    elif not column1:
        return False
    elif not column2:
        return False
    elif not column3:
        return False
    elif not column4:
        return False
    elif not block1:
        return False
    elif not block2:
        return False
    elif not block3:
        return False
    elif not block4:
        return False
    else:
        return True


def commandReset():
    # Clear A 1-4
    A1.set(0)
    A2.set(0)
    A3.set(0)
    A4.set(0)

    # Clear B 1-4
    B1.set(0)
    B2.set(0)
    B3.set(0)
    B4.set(0)

    # Clear C 1-4
    C1.set(0)
    C2.set(0)
    C3.set(0)
    C4.set(0)

    # Clear D 1-4
    D1.set(0)
    D2.set(0)
    D3.set(0)
    D4.set(0)


def commandSet():
    # Clear all the arrays
    rowA.clear()
    rowB.clear()
    rowC.clear()
    rowD.clear()
    column1.clear()
    column2.clear()
    column3.clear()
    column4.clear()
    block1.clear()
    block2.clear()
    block3.clear()
    block4.clear()
    allNumbers.clear()

    # Set Rows
    rowA.append(A1.get())
    rowA.append(A2.get())
    rowA.append(A3.get())
    rowA.append(A4.get())

    rowB.append(B1.get())
    rowB.append(B2.get())
    rowB.append(B3.get())
    rowB.append(B4.get())

    rowC.append(C1.get())
    rowC.append(C2.get())
    rowC.append(C3.get())
    rowC.append(C4.get())

    rowD.append(D1.get())
    rowD.append(D2.get())
    rowD.append(D3.get())
    rowD.append(D4.get())

    # Set Columns
    column1.append(A1.get())
    column1.append(B1.get())
    column1.append(C1.get())
    column1.append(D1.get())

    column2.append(A2.get())
    column2.append(B2.get())
    column2.append(C2.get())
    column2.append(D2.get())

    column3.append(A3.get())
    column3.append(B3.get())
    column3.append(C3.get())
    column3.append(D3.get())

    column4.append(A4.get())
    column4.append(B4.get())
    column4.append(C4.get())
    column4.append(D4.get())

    # Set Blocks
    block1.append(A1.get())
    block1.append(A2.get())
    block1.append(B1.get())
    block1.append(B2.get())

    block2.append(A3.get())
    block2.append(A4.get())
    block2.append(B3.get())
    block2.append(B4.get())

    block3.append(C1.get())
    block3.append(C2.get())
    block3.append(D1.get())
    block3.append(D2.get())

    block4.append(C3.get())
    block4.append(C4.get())
    block4.append(D3.get())
    block4.append(D4.get())

    allNumbers.append(rowA)
    allNumbers.append(rowB)
    allNumbers.append(rowC)
    allNumbers.append(rowD)


def commandCheck():
    if emptyLists():
        errors = 0
        errorCounter.set(0)

        # Check zeros in all the entries
        for row in allNumbers:
            for i in range(4):
                if row[i] == 0:
                    errors += 1

        errorCounter.set(errors)
        if errorCounter.get() == 0:
            messagebox.showinfo('Won', 'Congratulations!, you have won the game!')
            commandReset()
            commandSet()
        else:
            messagebox.showerror('Error', f'Your answer has {errorCounter.get()} errors')
    else:
        messagebox.showwarning('Error', 'You must pin up your answer before check it (with \'Set\' button)')


def buttonChange(num):
    if num.get() == 0:
        num.set(1)
    elif num.get() == 1:
        num.set(2)
    elif num.get() == 2:
        num.set(3)
    elif num.get() == 3:
        num.set(4)
    elif num.get() == 4:
        num.set(0)


# User interface
window = Tk()

# 16 Variables for the entries
A1 = IntVar()
A2 = IntVar()
A3 = IntVar()
A4 = IntVar()
B1 = IntVar()
B2 = IntVar()
B3 = IntVar()
B4 = IntVar()
C1 = IntVar()
C2 = IntVar()
C3 = IntVar()
C4 = IntVar()
D1 = IntVar()
D2 = IntVar()
D3 = IntVar()
D4 = IntVar()

# Other Variables
errorCounter = IntVar()

# Arrays for the variables
rowA = []
rowB = []
rowC = []
rowD = []

column1 = []
column2 = []
column3 = []
column4 = []

block1 = []
block2 = []
block3 = []
block4 = []
# Array with all the variables
allNumbers = []
# Array for the errors
errorList = []

# Images
sudokuIcon = PhotoImage(file='sudoku icon.png')

# Fonts
titleFont = ('Franchise', 44, 'bold')
numbersFont = ('VCR OSD Mono', 20)
letterFont = ('VCR OSD Mono', 20, 'bold')

# Background and Foreground
mainbg = '#B48A58'
mainfg = '#480403'

# Size and Coordinates
numberswidth = 75
numbersheight = 75
# X
coordinates1 = 200
coordinates2 = 275
coordinates3 = 350
coordinates4 = 425
# Y
coordinatesA = 325
coordinatesB = 250
coordinatesC = 175
coordinatesD = 100

# Coordinates for the coordinates Labels
coordinatesABCD = coordinates1 - 25
coordinates1234 = coordinatesA + 75

# Main window
window.geometry('700x550')
window.title('Sudoku')
window.iconphoto(False, sudokuIcon)
window.config(bg=mainbg)

# Labels
titleLabel = Label(window,
                   text='Sudoku',
                   bg=mainbg,
                   fg=mainfg,
                   font=titleFont).place(relx=0.5, y=40, anchor=CENTER)

# A 1-4
A1button = Button(window,
                  textvariable=A1,
                  font=numbersFont,
                  bg=mainbg,
                  fg=mainfg,
                  command=lambda: buttonChange(A1)).place(x=coordinates1, y=coordinatesA,
                                                          height=numbersheight, width=numberswidth)
A2button = Button(window,
                  textvariable=A2,
                  font=numbersFont,
                  bg=mainbg,
                  fg=mainfg,
                  command=lambda: buttonChange(A2)).place(x=coordinates2, y=coordinatesA,
                                                          height=numbersheight, width=numberswidth)
A3button = Button(window,
                  textvariable=A3,
                  font=numbersFont,
                  bg=mainbg,
                  fg=mainfg,
                  command=lambda: buttonChange(A3)).place(x=coordinates3, y=coordinatesA,
                                                          height=numbersheight, width=numberswidth)
A4button = Button(window,
                  textvariable=A4,
                  font=numbersFont,
                  bg=mainbg,
                  fg=mainfg,
                  command=lambda: buttonChange(A4)).place(x=coordinates4, y=coordinatesA,
                                                          height=numbersheight, width=numberswidth)

# B 1-4
B1button = Button(window,
                  textvariable=B1,
                  font=numbersFont,
                  bg=mainbg,
                  fg=mainfg,
                  command=lambda: buttonChange(B1)).place(x=coordinates1, y=coordinatesB,
                                                          height=numbersheight, width=numberswidth)
B2button = Button(window,
                  textvariable=B2,
                  font=numbersFont,
                  bg=mainbg,
                  fg=mainfg,
                  command=lambda: buttonChange(B2)).place(x=coordinates2, y=coordinatesB,
                                                          height=numbersheight, width=numberswidth)
B3button = Button(window,
                  textvariable=B3,
                  font=numbersFont,
                  bg=mainbg,
                  fg=mainfg,
                  command=lambda: buttonChange(B3)).place(x=coordinates3, y=coordinatesB,
                                                          height=numbersheight, width=numberswidth)
B4button = Button(window,
                  textvariable=B4,
                  font=numbersFont,
                  bg=mainbg,
                  fg=mainfg,
                  command=lambda: buttonChange(B4)).place(x=coordinates4, y=coordinatesB,
                                                          height=numbersheight, width=numberswidth)

# C 1-4
C1button = Button(window,
                  textvariable=C1,
                  font=numbersFont,
                  bg=mainbg,
                  fg=mainfg,
                  command=lambda: buttonChange(C1)).place(x=coordinates1, y=coordinatesC,
                                                          height=numbersheight, width=numberswidth)
C2button = Button(window,
                  textvariable=C2,
                  font=numbersFont,
                  bg=mainbg,
                  fg=mainfg,
                  command=lambda: buttonChange(C2)).place(x=coordinates2, y=coordinatesC,
                                                          height=numbersheight, width=numberswidth)
C3button = Button(window,
                  textvariable=C3,
                  font=numbersFont,
                  bg=mainbg,
                  fg=mainfg,
                  command=lambda: buttonChange(C3)).place(x=coordinates3, y=coordinatesC,
                                                          height=numbersheight, width=numberswidth)
C4button = Button(window,
                  textvariable=C4,
                  font=numbersFont,
                  bg=mainbg,
                  fg=mainfg,
                  command=lambda: buttonChange(C4)).place(x=coordinates4, y=coordinatesC,
                                                          height=numbersheight, width=numberswidth)

# D 1-4
D1button = Button(window,
                  textvariable=D1,
                  font=numbersFont,
                  bg=mainbg,
                  fg=mainfg,
                  command=lambda: buttonChange(D1)).place(x=coordinates1, y=coordinatesD,
                                                          height=numbersheight, width=numberswidth)
D2button = Button(window,
                  textvariable=D2,
                  font=numbersFont,
                  bg=mainbg,
                  fg=mainfg,
                  command=lambda: buttonChange(D2)).place(x=coordinates2, y=coordinatesD,
                                                          height=numbersheight, width=numberswidth)
D3button = Button(window,
                  textvariable=D3,
                  font=numbersFont,
                  bg=mainbg,
                  fg=mainfg,
                  command=lambda: buttonChange(D3)).place(x=coordinates3, y=coordinatesD,
                                                          height=numbersheight, width=numberswidth)
D4button = Button(window,
                  textvariable=D4,
                  font=numbersFont,
                  bg=mainbg,
                  fg=mainfg,
                  command=lambda: buttonChange(D4)).place(x=coordinates4, y=coordinatesD,
                                                          height=numbersheight, width=numberswidth)

# Option Buttons
resetButton = Button(window,
                     text='Reset',
                     font=letterFont,
                     bg=mainbg,
                     fg=mainfg,
                     command=commandReset).place(x=150, y=450,
                                                 height=50, width=100)

setButton = Button(window,
                   text='Set',
                   font=letterFont,
                   bg=mainbg,
                   fg=mainfg,
                   command=commandSet).place(x=300, y=450,
                                             height=50, width=100)

checkButton = Button(window,
                     text='Check',
                     font=letterFont,
                     bg=mainbg,
                     fg=mainfg,
                     command=commandCheck).place(x=450, y=450,
                                                 height=50, width=100)

# Labels for coordinates
# A-B-C-D (Vertical coordinates)
labelA = Label(window,
               text='A',
               font=letterFont,
               bg=mainbg,
               fg=mainfg).place(x=coordinatesABCD, y=coordinatesA+20)

labelB = Label(window,
               text='B',
               font=letterFont,
               bg=mainbg,
               fg=mainfg).place(x=coordinatesABCD, y=coordinatesB+20)

labelC = Label(window,
               text='C',
               font=letterFont,
               bg=mainbg,
               fg=mainfg).place(x=coordinatesABCD, y=coordinatesC+20)

labelD = Label(window,
               text='D',
               font=letterFont,
               bg=mainbg,
               fg=mainfg).place(x=coordinatesABCD, y=coordinatesD+20)

# 1-2-3-4 (Horizontal coordinates)
label1 = Label(window,
               text='1',
               font=letterFont,
               bg=mainbg,
               fg=mainfg).place(x=coordinates1+20, y=coordinates1234)

label2 = Label(window,
               text='2',
               font=letterFont,
               bg=mainbg,
               fg=mainfg).place(x=coordinates2+20, y=coordinates1234)

label3 = Label(window,
               text='3',
               font=letterFont,
               bg=mainbg,
               fg=mainfg).place(x=coordinates3+20, y=coordinates1234)

label4 = Label(window,
               text='4',
               font=letterFont,
               bg=mainbg,
               fg=mainfg).place(x=coordinates4+20, y=coordinates1234)
# Mainloop
window.mainloop()
