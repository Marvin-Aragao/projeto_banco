import os

def inicio():
    os.system("cls")
    print()
    print("Bem vindo ao GNB!\n")
    print("Opções\n")
    print("1 - Criar Conta")
    print("2 - Login")
    print("3 - Verificar Saldo")
    print("4 - Depositar Dinheiro")
    print("5 - Sacar Dinheiro")
    print("6 - Sair\n")

def voltar_inicio():
    print()
    voltar = int(input("Digite '1' para voltar ao menu ou '2' para encerrar o atendimento: "))
    if voltar == 1:
        main()
    elif voltar == 2:
        encerrar_atendimento()
    else:
        print("insira uma opção valida\n")
        voltar_inicio() 

usuarios = []

def criar_conta():
    os.system("cls")
    print("     Criação de Conta\n\n")
    nome = input("Digite seu nome: ")
    senha = int(input("Crie uma senha: "))
    numero_conta = int(input("Digite o numero da sua conta: "))
    dinheiro = 0
    dados_conta = {"usuario": nome, "senha": senha, "numero da conta": numero_conta, "saldo": dinheiro}
    usuarios.append(dados_conta)
    print()
    print("Sua conta foi Criada com sucesso!\n\nVolte para o menu para realizar outras ações")
    voltar_inicio()

def verifica_usuario():
    login = input("Digite seu Usuario: ")
    for usuario in usuarios:
        if usuario["usuario"] == login:
            return True
        else:
            return False

def verifica_senha():
    senha = int(input("Digite sua senha: "))
    for usuario in usuarios:
        if usuario["senha"] == senha:
         return True
        else:
            return False

def tente_novamente():
    print()
    tentativa = int(input("Usuario ou senha invalido.\n Digite 1 para tentar novamente ou 2 para voltar ao menu principal: "))
    if tentativa == 1:
        print()
        acessar_conta()
    elif tentativa == 2:
        main()
    else:
        print("Digite uma opção valida\n")
        tente_novamente()

def acessar_conta():
    if verifica_usuario() == True and verifica_senha() == True:
        print("Bem vindo(a)", )
        return True
    else:
        tente_novamente()
def verificar_saldo():
    os.system("cls")
    print("     Saldo\n")
    print("Seu saldo é de R$", usuarios[0]["saldo"],",00")
    voltar_inicio()

def depositar_dinheiro():
    os.system("cls")
    print("     Area de Deposito\n\n")
    deposito = int(input("Digite a quantia que deseja depositar: "))#com o float, o valor fica com um ponto e zero(.0) indesejavel
    for usuario in usuarios:
        if acessar_conta() == True:#and usuario["conta"] == numero_conta:
            usuarios[0]["saldo"] += deposito#if ["senha"] in usuarios:def \\ otimizar  a utilizaçao do indice
    print()
    print("Deposito no valor de", deposito,",00")
    voltar_inicio()

def sacar_dinheiro():
    os.system("cls")
    print("     Area de Saque\n\n")
    saque = int(input("Digite o valor que deseja sacar: "))
    if usuarios[0]["saldo"] >= saque:
        usuarios[0]["saldo"] -= saque
        print(f"O saque no valor de {saque},00 foi realizado com sucesso.")
    else:
        print("Saldo insuficiemte para este saque")
    voltar_inicio()

def encerrar_atendimento():
    os.system("cls")
    print("Volte sempre")

def opcao_escolhida():
    opcao = int(input("Escolha uma opçao: "))
    if opcao == 1:
        criar_conta()
    elif opcao == 2:
        acessar_conta()
    elif opcao == 3:
        verificar_saldo()
    elif opcao == 4:
        depositar_dinheiro()
    elif opcao == 5:
        sacar_dinheiro()
    elif opcao == 6:
        encerrar_atendimento()
    else:
        encerrar_atendimento()

def main():
    inicio()
    opcao_escolhida()

main()