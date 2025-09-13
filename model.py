#Arquivo para a lógica

from datetime import datetime, date

def atualizar_relógio(root, time_var, hora_var):
    """Pequena função que pega a hora de datetime e atualiza a cada segundo."""
    if hora_var.get():
        agora = datetime.now().strftime('%H:%M:%S') #pega a hora atual
        time_var.set(agora)
    else:
        agora = datetime.now().strftime('%I:%M:%S %p') 
        time_var.set(agora)
    root.after(1000, atualizar_relógio, root, time_var, hora_var)

def mostrar_data(data_var):
    """Função para mostrar data"""
    hoje = date.today()
    data_var.set(hoje.strftime('%d/%m/%Y'))
