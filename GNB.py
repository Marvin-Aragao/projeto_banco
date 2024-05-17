import os
from turtle import clear

def inicio():
    print()
    print("Bem vindo ao GNB!\n")
    print("Opções\n")
    print("1 - Criar Conta")
    print("2 - Cerificar Saldo")
    print("3 - Depositar Dinheiro")
    print("4 - Sacar Dinheiro")
    print("5 - Sair\n")

def voltar_inicio():
    voltar = int(input("Digite '1' para voltar ao menu ou '2' para encerrar o atendimento: "))
    if voltar == 1:
        main()
    elif voltar == 2:
        encerrar_atendimento()
    else:
        print("insira uma opção valida")
        voltar_inicio() 

#Ao depositar dinheiro, o programa deve atualizar o saldo da conta bancária adicionando o valor depositado ao saldo atual.
saldo = 0

def depositar_dinheiro():
    deposito = float(input("Digite a quantia que deseja depositar: "))
    saldo += deposito
    print(f"Deposito no valor de {deposito}\n")
    voltar_inicio()

"""Ao sacar dinheiro, o programa deve verificar se o valor a ser sacado é menor ou igual ao saldo atual da conta bancária e, em caso afirmativo, atualizar o saldo da conta bancária subtraindo o valor sacado do saldo atual.
Se o valor a ser sacado for maior que o saldo atual da conta bancária, o programa deve exibir uma mensagem informando que não há saldo suficiente na conta bancária para realizar a operação."""

def sacar_dinheiro():
    saque = float(input("Digite o valor que deseja sacar: "))
    if saldo >= saque:
        saldo -= saque
        print(f"O saque no valor de {saque} foi realizado com sucesso.")
    else:
        print("Saldo insuficiemte para este saque")
    voltar_inicio()

#O programa deve armazenar as informações da conta bancária do usuário em um dicionário.
#Criar conta 
usuarios = []

def criar_conta():
    nome = input("Digite seu nome: ")
    senha = input("Crie uma senha: ")
    numero_conta = int(input("Digite o numero da sua conta: "))
    dinheiro = 0
    dados_conta = {"usuario": nome, "senha": senha, "numero da conta": numero_conta, "saldo": dinheiro}
    usuarios.append(dados_conta)
    voltar_inicio()

# def add_usuario():
#     usuarios.append()

def verificar_saldo():
    print(f"{saldo}\n")
    voltar_inicio()

def encerrar_atendimento():
    os.system('cls')
    print("Volte sempre")

def opcao_escolhida():
    opcao = int(input("Escolha uma opçao: "))
    if opcao == 1:
        criar_conta()
    elif opcao == 2:
        verificar_saldo()
    elif opcao == 3:
        depositar_dinheiro()
    elif opcao == 4:
        sacar_dinheiro()
    elif opcao == 5:
        encerrar_atendimento()
    else:
        encerrar_atendimento()

def main():
    inicio()
    opcao_escolhida()

main()