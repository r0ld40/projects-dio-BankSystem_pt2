LIMITE_SAQUES = 3
LIMITE = 500
CONTAS_E_USUARIOS = {}
user = ''
senha = ''
cpf = ''

def listaUsers():
    for keys, values in CONTAS_E_USUARIOS.items():
        print(keys,values)

def criarConta():

    print("\n######## CRIAR CONTA ########\n")

    userN = input('Digite seu nome: ')
    cpfN = int(input('Digite seu CPF: '))
    senhaN = int(input('Crie sua senha: '))

    print('Digite abaixo seu endereco completo:\n')

    cidade = input('>>> Cidade: ')
    bairro = input('>>> Bairro: ')
    rua = input('>>> Rua: ')
    numero = int(input('>>> Numero: '))
    cep = int(input('>>> CEP: '))

    if cpfN in (conta['CPF'] for conta in CONTAS_E_USUARIOS.values()) or senhaN in (conta['senha'] for conta in CONTAS_E_USUARIOS.values()):
        print('\n[ERRO] Usuário ou dados já cadastrados.')  
    else:
        CONTAS_E_USUARIOS[userN] = {'CPF': cpfN, 'senha': senhaN, 'dados': {'saldo': 0, 'extrato': [], 'num_saques': 0}, 'endereco': {'cidade': cidade, 'bairro': bairro, 'numero': numero, 'rua': rua, 'CEP': cep}}

    print("\n######## VOLTANDO AO INÍCIO ########\n")

def deposito():

    x = float(input("Digite um valor para deposito: R$ "))

    CONTAS_E_USUARIOS[user]['dados']['saldo'] += x
    CONTAS_E_USUARIOS[user]['dados']['extrato'].append(x)

    print("\n######## VOLTANDO AO INICIO ########\n")

def saque():

    x = float(input("Digite um valor para saque: R$ "))

    if x > CONTAS_E_USUARIOS[user]['dados']['saldo'] or CONTAS_E_USUARIOS[user]['dados']['num_saques'] >= LIMITE_SAQUES or x >= LIMITE:
        print("[ERRO] LIMITE DE SAQUES EXCEDIDO OU VALOR MAIOR QUE O ESPERADO.")
    else:
        CONTAS_E_USUARIOS[user]['dados']['saldo'] -= x
        CONTAS_E_USUARIOS[user]['dados']['num_saques'] += 1
        CONTAS_E_USUARIOS[user]['dados']['extrato'].append(-x)

    print("\n######## VOLTANDO AO INICIO ########\n")

def mostraExtrato():

    print(f"""\n######## SUA CONTA ########\n
SALDO: {CONTAS_E_USUARIOS[user]['dados']['saldo']}
EXTRATO: {CONTAS_E_USUARIOS[user]['dados']['extrato']}
SAQUES: {CONTAS_E_USUARIOS[user]['dados']['num_saques']}
LIMITE DE SAQUES: {LIMITE_SAQUES}""")
    print("\n######## VOLTANDO AO INICIO ########\n")

def perguntaMenu():

    menu = input("""
######## MENU ########
    
[A] DEPOSITO
[B] SAQUE
[C] EXTRATO
[D] CRIAR NOVA CONTA
[E] LISTAR CONTAS
[F] SAIR
                 
>>> """)
    
    if menu == "a" or menu == "A":
        deposito()
    elif menu == "b" or menu == "B":
        saque()
    elif menu == "c" or menu == "C":
        mostraExtrato()
    elif menu == "d" or menu == "D":
        criarConta()
    elif menu == "e" or menu == "E":
        listaUsers()
    elif menu == "f" or menu == "F":
        sair()
    else:
        print("##### [ERRO] OPERACAO INVALIDA #####")

def perguntaUsuario():
    
    global user, senha, cpf

    x = str(input('\nJa tem conta? [S/N] --> '))

    if x == 'S' or x == 's': 

        print("\n######## INICIO ########\n")

        user = str(input('Digite seu nome: '))
        cpf = int(input('Digite seu CPF: '))
        senha = int(input('Digite sua senha: '))

        if user in CONTAS_E_USUARIOS and CONTAS_E_USUARIOS[user]['CPF'] == cpf and CONTAS_E_USUARIOS[user]['senha'] == senha:
            perguntaMenu()
        else:
            print('\n[ERRO] Dados nao encontrados.\n')
    else:
        criarConta()

def sair():
    global repete
    repete = False
    print("\n######## FINALIZANDO O PROGRAMA ########")


repete = True
while repete == True:
    user = ''
    senha = ''
    cpf = ''
    
    perguntaUsuario()