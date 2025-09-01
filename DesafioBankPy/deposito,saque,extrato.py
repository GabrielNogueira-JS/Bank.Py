import gender_guesser.detector as gender

d = gender.Detector()

nome = input("Qual é o seu nome?: ").strip()
genero = d.get_gender(nome.split()[0]) 

if genero in ['male', 'mostly_male']:
    artigo = 'o'
elif genero in ['female', 'mostly_female']:
    artigo = 'a'
else:
    artigo = 'x'

# Escolha do tipo de conta
tipo_conta = input("Conta gold? (s/n): ").strip().lower()
if tipo_conta == "s":
    conta_gold = True
    LIMITE_SAQUES = 10
    limite = 1000
else:
    conta_gold = False
    LIMITE_SAQUES = 10
    limite = 500

menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 5000.00
extrato = ""
numero_saques = 0

print(f"Olá, {nome}! Sua conta {'gold' if conta_gold else 'normal'} está pronta para uso.")

while True:
    opcao = input(menu).lower()

    if opcao == "d":
        valor = float(input("Informe o valor a ser depositado: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Depósito realizado com sucesso!")
        else:
            print("Valor inválido para depósito.")

    elif opcao == "s":
        valor = float(input("Informe o valor de saque: "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Você não possui saldo suficiente.")
        elif excedeu_limite:
            print("Erro! O valor do saque é maior que o limite.")
        elif excedeu_saques:
            print("Quantidade de saques diários atingida!")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("Saque realizado com sucesso!")
        else:
            print("Valor inválido para saque.")

    elif opcao == "e":
        print("\n========== EXTRATO ==========")
        print(extrato if extrato else "Não foram realizadas movimentações.")
        print(f"Saldo Atual: R$ {saldo:.2f}")
        print(f"Obrigad{artigo} por usar o py.bank, volte sempre!")
        print("=============================\n")

    elif opcao == "q":
        print("Sistema encerrado. Até logo!")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
