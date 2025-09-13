#Arquivo para o GUI

import tkinter as tk
from tkinter import ttk
from model import atualizar_relógio, mostrar_data

root = tk.Tk()
root.geometry('500x500+300+300')
root.title('Mostrador de Data e Hora')
root.resizable(False, False)

time_var = tk.StringVar()
painel = ttk.LabelFrame(root, text='Hora')
painel.grid(row=0, column=0, rowspan=1, columnspan=1, sticky=tk.E + tk.W,
            padx=30, pady=20)

mostrador = tk.Label(painel, textvariable=time_var, font=('Arial', 48), fg='lime', 
                        bg='black')
mostrador.grid(row=0, column=0, sticky='nsew', padx=5, pady=5)

hora_var = tk.BooleanVar(value=True)
hora_24 = ttk.Radiobutton(painel, text='24 horas', variable=hora_var, value=True)
hora_24.grid(row=5, column=0, sticky=tk.E + tk.W, padx=5, pady=5)

hora_12 = ttk.Radiobutton(painel, text='12 horas', variable=hora_var, value=False)
hora_12.grid(row=5, column=1, sticky=tk.E + tk.W, padx=5, pady=5)


painel_data = ttk.LabelFrame(root, text='Data')
painel_data.grid(row=1, column=0, rowspan=1, columnspan=1, sticky='nsew',
                 padx=20, pady=20)

data_var = tk.StringVar()
mostrador_data = tk.Label(painel_data, textvariable=data_var, font=('Arial', 48), fg='lime',
                          bg='black')
mostrador_data.grid(row=0, column=0, sticky='nsew', padx=5, pady=5)

atualizar_relógio(root, time_var, hora_var)
mostrar_data(data_var)

root.mainloop()


