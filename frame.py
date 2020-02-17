# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk
from tkinter.ttk import *
from tkinter import scrolledtext

# Funcion de boton de almacenar
def modificar():

    raiz = Tk()
    raiz.geometry('500x500')
    raiz.configure(bg = 'white')
    raiz.title('Modificar datos')
    ttk.Button(raiz, text='Salir', command=quit).pack(side=BOTTOM)
    raiz.mainloop()
    print('current value is %s' % cara.get())
    final = ttk.Label(window, textvariable=cara,
    foreground="yellow", background="black",
    borderwidth=5, anchor="e")
    final.pack(side=TOP, fill=BOTH, expand=True,
    padx=20, pady=5)
    

def alm():
    messagebox.showinfo('Almacenamiento', 'Informacion almacenada correctamente.')
def bus():
    file = filedialog.askopenfilename(filetypes = (("Images","*.png"),("images","*.jpg")))

 
window = Tk()

# Titutlo de la ventana

window.title("Captura de alternativas.")

cara = StringVar()
carb = StringVar()
plataf = StringVar()

#Cuadros de texto dentro de las ventana

lbla = ttk.Label(window, text="Caracteristica A")
ca = ttk.Entry(window, textvariable=cara,
width=10)

lblb = ttk.Label(window, text="Caracteristica B")
cb = ttk.Entry(window, textvariable=carb,
width=10)

cons = ttk.Label(window, text="Fabricado por: ")
combo = Combobox(window)
combo['values']= ("DJI", "Parrot", "Xiaomi", "Hover", "AeroVironment", "3D Robotics", "INSITU", "Yunec", "Ehang", "Syma Toys")
combo.current(1)

plata = ttk.Label(window, text="Plataforma: ")
plata1 = ttk.Radiobutton(window, text='Android', variable=plataf, value='a')
plata2 = ttk.Radiobutton(window, text='IOS', variable=plataf, value='i')
plata3 = ttk.Radiobutton(window, text='Otro', variable=plataf, value='o')
desc = ttk.Label(window, text="Descripción técnica: ")
desctxt = scrolledtext.ScrolledText(window, width=40, height=10)
desctxt.insert(INSERT,'Ingresa la descripción...')
btn1 = ttk.Button(window, text="Almacenar",
                         command= alm)
btn2 = ttk.Button(window, text="Salir",
                         command=quit)
btn3 = ttk.Button(window, text="Modificar datos",
command= modificar)
                        
img = ttk.Label(window, text= "Cargar imagen... ")
btnimg = ttk.Button(window, text="Buscar",
command=bus)

# Atributos de los dialogos

lbla.pack(side=TOP, fill=BOTH, expand=False,
padx=10, pady=5)
ca.pack(side=TOP, fill=X, expand=False,
padx=20, pady=5)
lblb.pack(side=TOP, fill=BOTH, expand=False,
padx=10, pady=5)
cb.pack(side=TOP, fill=X, expand=False,
padx=20, pady=5)
cons.pack(side=TOP, fill=X, expand=False,
padx=10, pady=5)
combo.pack(side=TOP, fill=X, expand=False,
padx=20, pady=5)
plata.pack(side=TOP, fill=BOTH, expand=False,
padx=10, pady=5)
plata1.pack(side=TOP, fill=BOTH, expand=False,
padx=20, pady=5)
plata2.pack(side=TOP, fill=BOTH, expand=False,
padx=20, pady=5)
plata3.pack(side=TOP, fill=BOTH, expand=False,
padx=20, pady=5)
desc.pack(side=TOP, fill=BOTH, expand=False,
padx=10, pady=5)
desctxt.pack(side=TOP, fill=BOTH, expand=False,
padx=20, pady=5)
btn1.pack(side=LEFT, fill=BOTH, expand=False,
padx=10, pady=10)
btn2.pack(side=RIGHT, fill=BOTH, expand=False,
padx=10, pady=10)
img.pack(side=TOP, fill=BOTH, expand=False,
padx=10, pady=5)
btnimg.pack(side=BOTTOM, fill=BOTH, expand=True,
padx=10, pady=10)
btn3.pack(side=RIGHT, fill=BOTH, expand=True,
padx=10, pady=10)


window.mainloop()
