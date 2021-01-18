import tkinter
from tkinter import messagebox


def calcular():
    n1 = txtnumero1.get()

    if (len(n1) == 0):
        messagebox.showinfo(message="Ingrese el primero Numero !!", title="Mensaje")
        txtnumero1.focus()

    else:
        n1 = int(n1)
        for i in range(1, 16):
            #print(f'{i} x {n1} = {i * n1}')
            area.insert(1.0, "\nEl producto : {}".format(f'{i} x {n1} = {i * n1}'))







ventana = tkinter.Tk()  # instancia del formulario
ventana.title("Ventana Principal")
ventana.geometry("600x500")
# ventana.configure(background='green')
lblnumero1 = tkinter.Label(ventana, text='tabla de multiplicar del numero:')
lblnumero1.place(x=100, y=50)
txtnumero1 = tkinter.Entry(ventana, width=20)
txtnumero1.place(x=310, y=50)

boton = tkinter.Button(ventana, text="Generar tabla", command=calcular)
boton.place(x=250, y=100)
area = tkinter.Text(ventana)
area.config(width=42, height=13)
area.place(x=100, y=150)
# paises=tkinter.StringVar(ventana)
# paises.set("--------------")
# combo=tkinter.OptionMenu(ventana,paises,"--------------","Peru","Chile","Mexico")
# combo.place(x=100,y=400)
ventana.mainloop()  # ejec