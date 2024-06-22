# Display Menu
menu = """\n
========== Escolha a opção Desejada !! ==========
           
           [1] Depositar
           [2] Sacar
           [3] Extrato

           [0] Sair

=================================================

"""

# Banco de Dados dos valores

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

#código da parte lógica do projeto
while True:
    opcao = input(menu)

# Bloco de código Depósito
    if opcao == "1":
        valor = float(input(" Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("\nOperação falhou! O valor informado é inválido")
# Bloco de código Saque    
    elif opcao == "2":
        valor = float(input("Informe o valor do Saque: "))

        exedeu_saldo = valor > saldo
        
        exedeu_limite = valor > limite

        exedeu_saque = numero_saques >= LIMITE_SAQUES

        if exedeu_saldo:
             print("\nOperação Falhou!! Você não tem saldo suficiente")

        elif exedeu_limite:
             print("\nOperação Falhou!! O valor de saque excede o limite")

        elif exedeu_saque:
             print("\nOperação Falhou!!, Você atingiu o limite de saques diários")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
# caso o usuario tente informar um valor negativo.
        else:
            print("""
========== Operação Falhou ==========
        
        O valor Informado 
            é Invalido

=======================================
""")

# Bloco de código do Extrato        
    elif opcao == "3":
         print("\n ========= Extrato ========")
         print(" Não foi realizada \n nenhuma movimentação." if not extrato else extrato)
         print(f"\nSaldo: R$ {saldo:.2f}")
         print("=============================")
    
# Exit, Finaliza o loop while
    elif opcao == "0":
        break

# Caso o valor informado não esteja de acordo com o formato.

    else:
        print("""
========== Operação inválida ==========
        
        Por favor, Selecionar novamente
           a operação desajda.

=======================================
""")