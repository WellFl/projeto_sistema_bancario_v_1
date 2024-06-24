def menu_transacoes():
    menu = """\n
========== Escolha a opção Desejada !! ==========
           
           [1] Depositar
           [2] Sacar
           [3] Extrato

           [0] Sair

=================================================

"""
    return input(menu)

def menu_login():
    menu = """\n
========== Escolha a opção Desejada !! ==========
           
           [1] Novo usuário
           [2] Nova Conta
           [3] logar

           [0] Sair

=================================================

"""
    return input(menu)

def depositar(saldo, valor, extrato,/):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("\n ----- Depósito Realizado com Sucesso!! -----")
    else:
        print("""
========== Operação Falhou ==========
        
        O valor Informado 
            é Invalido

=======================================
""")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
         print("\n ---- Operação Falhou!! Você não tem saldo suficiente -----")

    elif excedeu_limite:
         print("\n ----- Operação Falhou!! O valor de saque excede o limite ------")

    elif excedeu_saques:
         print("\n----- Operação Falhou!!, Você atingiu o limite de saques diários ------")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("\n ----- Saque Realizado Com Sucesso!! -----")
# caso o usuario tente informar um valor negativo.
    else:
        print("""
========== Operação Falhou ==========
        
        O valor Informado 
            é Invalido

=======================================
""")
    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    print("\n ========= Extrato ========")
    print(" Não foi realizada \n nenhuma movimentação." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("=============================")

def criar_usuario(usuarios):

    cpf = input("Qual o seu CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n ---- Já existe um usúario com esse CPF! ----")
        return
    
    nome = input("Informe seu Nome Completo: ")
    data_de_nascimento = input("Data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe seu Endereço (longradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_de_nascimento": data_de_nascimento, "cpf": cpf, "endereço": endereco})

    print("---- Usúario Criado com Sucesso!! ----")

def filtrar_usuario(cpf, usuarios):

    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None
            
def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n --- Conta Criada com Sucesso! ---")
        print(f"\n Sua conta é : {agencia, numero_conta}")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print ("\n ----- Usuário Não encontrado, Fluxo de Criação de conta encerrado!! -----")

def origem():
    
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        
        menu_1 = menu_login()
        

        if menu_1 == "1":
            criar_usuario(usuarios)
        
        elif menu_1 == "2":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif menu_1 == "3":
                print(" ---- Seja Bem Vindo ----")

                while True:
                    menu_2 = menu_transacoes()
# Bloco de código Depósito
                    if menu_2 == "1" :
                        valor = float(input(" Informe o valor do depósito: "))
            
                        saldo, extrato = depositar(saldo, valor, extrato)
# Bloco de código Saque    
                    elif menu_2 == "2":
                        valor = float(input("Informe o valor do Saque: "))

                        saldo, extrato = sacar(
                            saldo=saldo,
                            valor=valor,
                            extrato=extrato,
                            limite=limite,
                            numero_saques=numero_saques,
                            limite_saques=LIMITE_SAQUES
                            )


# Bloco de código do Extrato        
                    elif menu_2 == "3":
                        exibir_extrato(saldo, extrato=extrato)
    
# Exit, Finaliza o loop while
                    elif menu_2 == "0":
                        break

# Caso o valor informado não esteja de acordo com o formato.

                    else:
                         print("""
                         ========== Operação inválida ==========
        
                             Por favor, Selecionar novamente
                                 a operação desajda.

                         =======================================
                        """)
                        

        elif menu_1 == "0":
            break

        else:
            print("""
========== Operação inválida ==========
        
        Por favor, Selecionar novamente
           a operação desajda.

=======================================
""")
    
            
origem()
