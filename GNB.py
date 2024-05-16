"""Crie um programa que permita ao usuário realizar as seguintes operações bancárias:


"""

#O programa deve exibir um menu para o usuário escolher a operação que deseja realizar e, em seguida, executar a operação escolhida.
opcao = int(input("Escolha uma opçao"))
if opcao == 1:
    def criar_conta()
elif opcao == 2:
    def verificar_saldo()
elif opcao == 3:
    def depositar_dinheiro()
elif opcao == 4:
    def sacar_dinheiro()
elif opcao == 5:
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

