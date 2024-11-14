clienteList = []
funcionarioList = []
activeUsr = None
logged = False

class Banco():
    def __init__(self, id_banco) -> None:
        self.id_banco = id_banco

    def retornaFolhaSalarial():
        print("\nFOLHA SALARIAL")
        total = 0
        for funcionario in funcionarioList:

            salarioTemp = funcionario.calcularSalario()
            total += salarioTemp

            print(f"\nNome: {funcionario.nome} Salário: {salarioTemp}")
        print(f"Gasto total com salarios: {total}")

    def getAllFuncionario_Stats(): ######### WIP
        maiorSalario = funcionarioList[0] 
        menorSalario = funcionarioList[0]
        quantidadeTotal = 0

        for funcionario in funcionarioList:
            if funcionario.salario > maiorSalario.salario:
                maiorSalario = funcionario
            
            if funcionario.salario < menorSalario.salario:
                menorSalario = funcionario

            quantidadeTotal += 1 

        print(f"\nO maior salario é do funcionario {maiorSalario.nome}, salario: {maiorSalario.salario}")
        print(f"\nO menor salario é do funcionario {menorSalario.nome}, salario: {menorSalario.salario}")

    def getAllCliente_Stats():
        qntdCC = 0
        qntdCS = 0
        qntdTotal = 0

        for cliente in clienteList:
            if isinstance(cliente, Cli_CC):
                qntdCC += 1
            elif isinstance(cliente, Cli_CS):
                qntdCS += 1
            
            qntdTotal += 1

        print(f"\nExistem {qntdTotal} clientes/contas do bnk.\n{qntdCC} são contas correntes e {qntdCS} são contas salário")


############################
# CLASSES FUNCIONARIOS
############################
class Funcionario(Banco): 
    def __init__(self, nome: str, cpf: str, bonus: float, id_banco) -> None:
        super().__init__(id_banco)
        self.nome = nome
        self.cpf = cpf
        self.bonus = bonus
        funcionarioList.append(self)

    def calcularSalario(self):
        pass

class Gerente(Funcionario):
    def __init__(self, nome: str, cpf: str, bonus: float, username: str, senha: str, salario: float, atendimentos: int, id_banco: str) -> None:
        super().__init__(nome, cpf, bonus, id_banco)
        self.username = username
        self.senha = senha
        self.salario = salario
        self.atendimentos = atendimentos

    def calcularSalario(self):
        self.salario = self.salario + (self.atendimentos * 100)
        if self.bonus != 0:
            self.salario += self.bonus

class Consultor(Funcionario):
    def __init__(self, nome: str, cpf: str, bonus: float, username: str, senha: str, salario: float, atendimentos: int, id_banco: str) -> None:
        super().__init__(nome, cpf, bonus, id_banco) 
        self.salario = salario
        self.username = username
        self.senha = senha
        self.atendimentos = atendimentos

    def calcularSalario(self):
        self.salario = self.salario + (self.atendimentos * 25)

############################
# CLASSES CLIENTES  
############################
class Cliente(Banco):
    def __init__(self, nome, cpf, username, senha, id_banco) -> None:
        super().__init__(id_banco)
        self.nome = nome
        self.cpf = cpf
        self.username = username
        self.senha = senha
        clienteList.append(self)


class Cli_CC(Cliente): # conta corrente
    def __init__(self, nome: str, cpf: str, username: str, senha: str, dinheiro: float, credMax: float, id_banco: str) -> None:
        super().__init__(nome, cpf, username, senha, id_banco)
        self.dinheiro = dinheiro
        self.credMax = dinheiro + (dinheiro * 0.5)

    def calcular_credMax(self, dinheiroAtual):
        # função arbirtária para cálculo, apenas exemplo
        credMax = 0

        if dinheiroAtual:
            credMax = dinheiroAtual + (dinheiroAtual * 0.5)
            self.credMax = credMax
            return credMax
        else: 
            return credMax

    def depositar(self):
        try:
            
            usrin = float(int("\nInsira o valor a depositar: "))
            self.dinheiro = self.dinheiro + usrin
            self.calcular_credMax(dinheiroAtual = self.dinheiro) # precisa chamar com o self sempre que referencia funcao dentro da classe
            print(f"\nNovo balanço: {self.dinheiro}")
            print(f"Novo Crédito: {self.credMax}")

        except TypeError: 
            print("apenas numeros, para decimais use .\nEX: Mil reais e cinquenta centavos = 1.50")

    def saque(self):       
        try:
            usrin = float(int("\nInsira o valor a sacar: "))
            if usrin < self.dinheiro or usrin == self.dinheiro:    
                self.dinheiro = self.dinheiro - usrin
                self.calcular_credMax(dinheiroAtual = self.dinheiro) # precisa chamar com o self sempre que referencia funcao dentro da classe
                print(f"\nNovo balanço: {self.dinheiro}")
                print(f"Novo Crédito: {self.credMax}")

            else: print("\nERRO\n Valor insuficiente na conta.")
        except TypeError: 
            print("apenas numeros, para decimais use .\nEX: Um real e cinquenta centavos = 1.50")
        
class Cli_CS(Cliente): # conta salário
    def __init__(self, nome: str, cpf: str, dinheiro: float, username: str, senha: str) -> None:
        super().__init__(nome, cpf, username, senha, )
        self.dinheiro = dinheiro

    def saque(self):       
        try:
            usrin = float(int("\nInsira o valor a sacar: "))
            if usrin < self.dinheiro or usrin == self.dinheiro:    
                self.dinheiro = self.dinheiro - usrin
            else: print("\nERRO\n Valor insuficiente na conta.")
        except TypeError: 
            print("apenas numeros, para decimais use .\nEX: Um real e cinquenta centavos = 1.50")

############################

def login_system():
    usrname = input("usuario> ")
    global logged
    global activeUsr

    if funcionarioList and not logged:
        for funcionario in funcionarioList:
            print(f"{funcionario.nome}")
            if usrname == funcionario.username:
                passw = input(f"\n\tUsuario: {funcionario.username}\n\tSenha: ")
                if passw == funcionario.senha:
                    logged = True
                    activeUsr = funcionario
                    return funcionarioMenu()
                else: 
                    print("senha errada...")
            else: 
                continue
    else: print("\n\tERRO: não existem funcionários cadastrados")

    if clienteList and not logged:
        for cliente in clienteList:
            if usrname == cliente.username:
                passw = input(f"\n\tUsuario: {cliente.username}\n\tSenha: ")
                if passw == cliente.senha:
                    logged = True
                    activeUsr = cliente
                    return clienteMenu()
                else: 
                    print("senha errada...")
            else: 
                continue
    else: print("\tERRO: não existem clientes cadastrados")         

    print("\n\tUsuário não encontrado")

def funcionarioMenu():
    global logged
    global activeUsr

    while logged:
        if isinstance(activeUsr, Gerente):
            usrin = input("Escolha uma opção do menu.\n\t1)Novo Cliente/Remover Cliente\n\t2)ph\n\t3)ph\n\t4)ph\n\t5)Sair ")

            match usrin:
                case "1": # add/remove client
                    usrin = input("\n\t1)NOVO CLIENTE CONTA CORRENTE\n\t2)NOVO CLIENTE CONTA SALARIO ")
                    match usrin:
                        case "1":
                            nomein = input("Insira o nome do novo cliente: ")
                            cpfin = input("Insira o cpf do novo cliente: ")
                            usernamein = input("Insira o username do novo cliente (usado para acessar a conta): ")
                            senhain = input("Insira a senha do novo usuário: ")
                            newclient = Cli_CC(nome=nomein, cpf=cpfin, username=usernamein, senha=senhain, dinheiro=0, credMax=0, id_banco=activeUsr.id_banco)
                            if nomein and cpfin and usernamein and senhain and newclient:
                                print(f"Conta Corrente criada para {newclient.nome}, CPF - {newclient.cpf}")
                            else: print("proibido espaços em branco ")

                        case "2":
                            nomein = input("Insira o nome do novo cliente: ")
                            cpfin = input("Insira o cpf do novo cliente: ")
                            usernamein = input("Insira o username do novo cliente (usado para acessar a conta): ")
                            senhain = input("Insira a senha do novo usuário: ")
                            newclient = Cli_CS(nome=nomein, cpf=cpfin, username=usernamein, senha=senhain, dinheiro=0, id_banco=activeUsr.id_banco)
                            if nomein and cpfin and usernamein and senhain and newclient:
                                print(f"Conta Salário criada para {newclient.nome}, CPF - {newclient.cpf}")
                            else: print("proibido espaços em branco ")

                        case _:
                            pass
                case "2": # edit acc details
                    pass
                case "3": # see bank statistics (funcionarios/contas)
                    pass
                case "4": # 
                    pass
                case "5": # exit
                    activeUsr = None
                    logged = False
                case _:
                    print("opção inválida")

        elif isinstance(activeUsr, Consultor):
            pass

def clienteMenu():
    if isinstance(activeUsr, Cli_CC):
        pass
    elif isinstance(activeUsr, Cli_CS):
        pass

### DEBUG
# DEFAULT USUARIOS
admin = Gerente(nome="Administrador", cpf="12345678900", bonus=0, username="admin", senha="123", salario=13000, atendimentos=5, id_banco=1)
consultorTeste = Consultor(nome="consultor1", cpf="12345678900", bonus=0, username="consultor", senha="123", salario=3000, atendimentos=15, id_banco=1)

while True:
    usrin = input("\n\t1) Login \n\t2) Sair: ")
    # always define usrin 0 BEFORE calling any functions
    match usrin:
        case "1": # LOGIN
            usrin = 0
            login_system()
        case _: # SAIR
            usrin = 0
            break