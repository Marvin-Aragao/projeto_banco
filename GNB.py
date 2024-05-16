"""Crie um programa que permita ao usuário realizar as seguintes operações bancárias:


"""

#O programa deve exibir um menu para o usuário escolher a operação que deseja realizar e, em seguida, executar a operação escolhida.
def inicio():
    print("Bem vindo ao GNB!/n")
    print("")
    print("Escolha uma opção abaixo:/n")
    print("1 - Criar Conta")
    print("2 - Cerificar Saldo")
    print("3 - Depositar Dinheiro")
    print("4 - Sacar Dinheiro")
    print("5 - Sair")
    OPCAO = int(input("Escolha uma opçao: "))

#opcao = int(input("Escolha uma opçao: "))
def opcao_escolhida(OPCAO):
    if OPCAO == 1:
        def criar_conta()
    elif OPCAO == 2:
        def verificar_saldo()
    elif OPCAO == 3:
        def depositar_dinheiro()
    elif OPCAO == 4:
        def sacar_dinheiro()
    elif OPCAO == 5:
        def encerrrar_atendimento()
    else:
        def encerrar_atendimento()
        

#Ao depositar dinheiro, o programa deve atualizar o saldo da conta bancária adicionando o valor depositado ao saldo atual.
saldo = 0

def depositar_dinheiro():
    deposito = float(input("Digite a quantia que deseja depositar: "))
    saldo += deposito
    print(f"Deposito no valor de {deposito}")

"""Ao sacar dinheiro, o programa deve verificar se o valor a ser sacado é menor ou igual ao saldo atual da conta bancária e, em caso afirmativo, atualizar o saldo da conta bancária subtraindo o valor sacado do saldo atual.
Se o valor a ser sacado for maior que o saldo atual da conta bancária, o programa deve exibir uma mensagem informando que não há saldo suficiente na conta bancária para realizar a operação."""

def sacar_dinheiro():
    saque = float(input("Digite o valor que deseja sacar: "))
    if saldo >= saque:
        saldo -= saque
        print(f"O saque no valor de {saque} foi realizado com sucesso.")
    else:
        print("Saldo insuficiemte para este saque")

#O programa deve armazenar as informações da conta bancária do usuário em um dicionário.
#Criar conta 
usuarios = []
def add_usuario():
    usuarios.append()

