import sys
import os
import json
import utils
import integracoes_api

STATUS = "Aberto"

#função que cadastra chamados
def cadastra_chamado(lista):

    titulo = input("Digite o Titulo: ")
    solicitante = input("Nome do solicitante: ")
    prioridade = input("Prioridade (Alta/Media/Baixa): ")
    valor_estimado_brl = input("Valor estimado em reais: ")
    cep = input("CEP: ")

    # chama a função cotacao para pegar o valor do dolar do dia
    valor_dolar = integracoes_api.cotacao()
    
    valor_estimado_brl = valor_estimado_brl.replace(",", ".")
    valor_estimado_brl = float(valor_estimado_brl)
    valor_estimado_dolar = valor_estimado_brl / valor_dolar

    # verififca se o cep é um número, caso não seja, retorna uma mensagem de erro
    try:
        int(cep)
    except ValueError:
        print("CEP inválido. Por favor, digite apenas números.")
        return
    endereco = integracoes_api.cep(cep)
    
    # dicionario sem padronizacao
    item = {
        "id": len(lista) + 1,
        "titulo": titulo,
        "solicitante": solicitante,
        "prioridade": prioridade,
        "cep": cep,
        "endereco": endereco,
        "valor_estimado_brl": valor_estimado_brl,
        "valor_estimado_dolar": valor_estimado_dolar,
        "status": STATUS
    }
    lista.append(item)
    print("Cadastrado com sucesso!")

#função para listar todos os chamados cadastrados
def lista_todos(lista):
  if len(lista) == 0:
      print("Não há chamados cadastrados")
  for i in lista:
      print("ID:", i["id"], "| Título:", i["titulo"], "| Status:", i["status"], "| Valor: $", i["valor_estimado_dolar"])

lista_global_chamados = []

# função que busca os chamados cadastrados pelo ID, caso não encontre, retorna uma mensagem de erro
def buscar_chamado(lista):
    chamado_encontrado = False
    id_chamado = input("Digite o ID do chamado: ")
    id_chamado = utils.verifica_int(id_chamado)

    for chamado in lista:
        if chamado["id"] == id_chamado:
            print("ID:", chamado["id"], "| Título:", chamado["titulo"], "| Status:", chamado["status"])
            chamado_encontrado = True
            return
    if not chamado_encontrado:
        print("Chamado não encontrado.")

#função altera os dados do chamado, caso não encontre, retorna uma mensagem de erro
def alterar_chamado(lista):
    id_chamado = input("Digite o ID do chamado que deseja alterar: ")
    id_chamado = utils.verifica_int(id_chamado)
    for chamado in lista:
        if chamado["id"] == id_chamado:
            print("Chamado encontrado. Informe os novos dados:")
            chamado["titulo"] = input("Novo título: ")
            chamado["solicitante"] = input("Novo solicitante: ")
            chamado["prioridade"] = input("Nova prioridade (Alta/Media/Baixa): ")
            chamado["cep"] = input("Novo CEP: ")
            print("Chamado alterado com sucesso!")
            return
    print("Chamado não encontrado.")

#função que exclui chamados
def excluir_chamado(lista):
    id_chamado = input("Digite o ID do chamado que deseja excluir: ")
    id_chamado = utils.verifica_int(id_chamado)
    for chamado in lista:
        if chamado["id"] == id_chamado:
            lista.remove(chamado)
            print("Chamado excluído com sucesso!")
            return
    print("Chamado não encontrado.")

# filtra os chamados por prioridade, caso não encontre, retorna uma mensagem de erro
def filtra_prioridade(lista):
    prioridade = input("Digite a prioridade que deseja filtrar (Alta/Media/Baixa): ")
    chamados_filtrados = [chamado for chamado in lista if chamado["prioridade"].lower() == prioridade.lower()]
    if len(chamados_filtrados) == 0:
        print("Nenhum chamado encontrado com essa prioridade.")
    else:
        for chamado in chamados_filtrados:
            print("ID:", chamado["id"], "| Título:", chamado["titulo"], "| Status:", chamado["status"])

# função principal, mostra o menu e chama as funções de acordo com a escolha do usuário
def menu():
    while True:
        print("\n--- MENU TECHFLOW ---")
        print("1. Cadastrar")
        print("2. Listar")
        print("3. Buscar")
        print("4. Alterar")
        print("5. Excluir")
        print("6. Filtrar por prioridade")
        print("7. Sair")
        opcao = input("Escolha: ")
        match opcao:
            case "1":
                utils.limpar_tela()
                cadastra_chamado(lista_global_chamados)
                utils.limpar_tela()
            case "2":
                utils.limpar_tela()
                lista_todos(lista_global_chamados)
                utils.limpar_tela()
            case "3":
                utils.limpar_tela()
                buscar_chamado(lista_global_chamados)
                utils.limpar_tela()
            case "4":
                utils.limpar_tela()
                alterar_chamado(lista_global_chamados)
                utils.limpar_tela()
            case "5":
                utils.limpar_tela()
                excluir_chamado(lista_global_chamados)
                utils.limpar_tela()
            case "6":
                utils.limpar_tela()
                filtra_prioridade(lista_global_chamados)
                utils.limpar_tela()
            case "7":
                utils.limpar_tela()
                sys.exit()
            case _:
                utils.limpar_tela()
                print("Opção inválida. Tente novamente.")
                utils.limpar_tela()

if __name__ == "__main__":
    menu()