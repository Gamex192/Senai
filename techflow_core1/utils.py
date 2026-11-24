import os

# função que limpa a tela do terminal
def limpar_tela():
    """Pausa a execução aguardando o usuário e limpa o terminal."""
    sla = input("Pressione Enter para continuar...")
    os.system('cls' if os.name == 'nt' else 'clear')

def verifica_int(id_chamado):
    try:
        id_chamado = int(id_chamado)
        return id_chamado
    except ValueError:
        print("ID inválido. Por favor, digite apenas números.")
        return