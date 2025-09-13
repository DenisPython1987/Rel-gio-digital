#Arquivo para a lógica

from datetime import datetime

def atualizar_relógio(root, time_var):
    """Pequena função que pega a hora de datetime e atualiza a cada segundo."""
    agora = datetime.now().strftime('%H:%M:%S') #pega a hora atual
    time_var.set(agora)
    root.after(1000, atualizar_relógio, root, time_var)

