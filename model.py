#Arquivo para a lógica

from datetime import datetime, date

def atualizar_relógio(root, time_var, hora_var):
    """Pequena função que pega a hora de datetime e atualiza a cada segundo."""

    #Aqui eu crio um if statement para os formatos 12 e 24 horas
    #Eu pego a hora da variavel de controlo com o get()
    if hora_var.get():

        #Aqui eu pego a hora e formato em 24 horas  
        agora = datetime.now().strftime('%H:%M:%S')

        #Aqui e atribuo a hora de "agora" à variável "time_var"
        time_var.set(agora)
    else:

        #Aqui eu pego a hora e formato em 12 horas com AM e PM
        agora = datetime.now().strftime('%I:%M:%S %p') 

        #Aqui eu atribuo a hora de "agora" à variável "time_var"
        time_var.set(agora)
    
    #Aqui eu uso a função "after" para atualizar o relógio na janela
    root.after(1000, atualizar_relógio, root, time_var, hora_var)

def mostrar_data(data_var):
    """Função para mostrar data"""

    #Aqui eu pego a data de hoje
    hoje = date.today()

    #Aqui eu atribuo a data de hoje, formatada para o Brasil, à variável "data_var"
    data_var.set(hoje.strftime('%d/%m/%Y'))
