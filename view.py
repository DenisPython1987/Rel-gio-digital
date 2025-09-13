#Arquivo para o GUI

import tkinter as tk
from tkinter import ttk
from model import atualizar_relógio, mostrar_data

"""Aqui eu crio a janela principal, determino o tamanho, o título e proíbo o 
redimensionamento."""
root = tk.Tk()
root.geometry('500x500+300+300')
root.title('Mostrador de Data e Hora')
root.resizable(False, False)

#Aqui eu crio a variável para armazenar a informação da hora.
time_var = tk.StringVar()

#Aqui eu crio e fixo na janela o painel para mostrar a hora
painel = ttk.LabelFrame(root, text='Hora')
painel.grid(row=0, column=0, rowspan=1, columnspan=1, sticky=tk.E + tk.W,
            padx=30, pady=20)

#Aqui eu crio e fixo no painel o Label que mostra a hora
mostrador = tk.Label(painel, textvariable=time_var, font=('Arial', 48), fg='lime', 
                        bg='black')
mostrador.grid(row=0, column=0, sticky='nsew', padx=5, pady=5)

#Aqui eu crio a variável para os Radiobuttons dos formatos de hora
hora_var = tk.BooleanVar(value=True)

#Aqui eu crio e fixo no painel o Radiobutton do formato 24 horas
hora_24 = ttk.Radiobutton(painel, text='24 horas', variable=hora_var, value=True)
hora_24.grid(row=5, column=0, sticky=tk.E + tk.W, padx=5, pady=5)

#Aqui eu crio e fixo no painel o Radiobutton do formato 12 horas
hora_12 = ttk.Radiobutton(painel, text='12 horas', variable=hora_var, value=False)
hora_12.grid(row=5, column=1, sticky=tk.E + tk.W, padx=5, pady=5)

#Aqui eu crio e fixo na janela o painel para mostrar a data
painel_data = ttk.LabelFrame(root, text='Data')
painel_data.grid(row=1, column=0, rowspan=1, columnspan=1, sticky='nsew',
                 padx=20, pady=20)

#Aqui eu crio a variável para armazenar a informação da data
data_var = tk.StringVar()

#Aqui eu crio e fixo no painel_data o Label da data
mostrador_data = tk.Label(painel_data, textvariable=data_var, font=('Arial', 48), fg='lime',
                          bg='black')
mostrador_data.grid(row=0, column=0, sticky='nsew', padx=5, pady=5)

#Aqui eu chamo as duas funções para mostrar a data e a hora
atualizar_relógio(root, time_var, hora_var)
mostrar_data(data_var)

root.mainloop()


