#Arquivo para o GUI

import tkinter as tk
from tkinter import ttk
from model import atualizar_relógio

root = tk.Tk()
root.geometry('500x500+300+300')
root.resizable(False, False)

time_var = tk.StringVar()
painel = ttk.LabelFrame(root, text='Data e hora')
painel.grid(row=0, column=0, rowspan=1, columnspan=1, sticky=tk.E + tk.W,
            padx=5, pady=5)

mostrador = tk.Label(painel, textvariable=time_var, font=('Arial', 48), fg='lime', 
                        bg='black')
mostrador.grid(row=0, column=0, sticky=tk.E + tk.W, padx=5, pady=5)

atualizar_relógio(root, time_var)

root.mainloop()


