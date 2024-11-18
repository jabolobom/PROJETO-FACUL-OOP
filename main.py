clienteList = []
funcionarioList = []
activeUsr = None
logged = False

class Banco():
    def __init__(self, id_banco: str) -> None:
        self.id_banco = id_banco

    def getStats(self): ######### WIP
        usrin = input("1) Estatísticas de funcionário\n\t2)Estatísticas de clientes\n\t 3)Folha salarial")
        if usrin == "1":    
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
        elif usrin == "2":
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
        elif usrin == "3":
            print("\nFOLHA SALARIAL")
            total = 0
            for funcionario in funcionarioList:

                salarioTemp = funcionario.calcularSalario()
                total += salarioTemp

                print(f"\nNome: {funcionario.nome} Salário: {salarioTemp}")
            print(f"\nGasto total com salarios: {total}")
        else:
            print("Opção inválida.")

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

    def novoCadastro(self):
        usrin = input("\n\tNOVO CADASTRO\n\t1)NOVO CLIENTE CONTA CORRENTE\n\t2)NOVO CLIENTE CONTA SALÁRIO")

        if usrin == "1":
            nomein = input("Insira o nome do novo cliente: ")
            cpfin = input("Insira o cpf do novo cliente: ")
            usernamein = input("Insira o username do novo cliente (usado para acessar a conta): ")
            senhain = input("Insira a senha do novo usuário: ")
            newclient = Cli_CC(nome=nomein, cpf=cpfin, username=usernamein, senha=senhain, dinheiro=0, credMax=0, id_banco=activeUsr.id_banco)
            if nomein and cpfin and usernamein and senhain and newclient:
                print(f"Conta Corrente criada para {newclient.nome}, CPF - {newclient.cpf}")
            else:
                print("proibido espaços em branco ")
        elif usrin == "2":
            nomein = input("Insira o nome do novo cliente: ")
            cpfin = input("Insira o cpf do novo cliente: ")
            usernamein = input("Insira o username do novo cliente (usado para acessar a conta): ")
            senhain = input("Insira a senha do novo usuário: ")
            newclient = Cli_CS(nome=nomein, cpf=cpfin, username=usernamein, senha=senhain, dinheiro=0, id_banco=activeUsr.id_banco)
            if nomein and cpfin and usernamein and senhain and newclient:
                print(f"Conta Salário criada para {newclient.nome}, CPF - {newclient.cpf}")
            else:
                print("proibido espaços em branco ")
        else:
            print("Opção inválida")

    def modificarCadastro(self):
        print("debug")

    def verDadosCliente(self):  
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

    def excluirCadastro(self):
        pass # excluir tanto funcionario / cliente
        usrin = input("temp")
        if usrin == "1":
            pass
        if usrin == "2":
            pass
        else: print("opção inválida")

    def verDadosConsultor(self):
        pass 

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
    def __init__(self, nome: str, cpf: str, username: str, senha: str, id_banco: str) -> None:
        super().__init__(id_banco)
        self.nome = nome
        self.cpf = cpf
        self.username = username
        self.senha = senha
        clienteList.append(self)

    def saque(self):       
        try:
            usrin = float(int("\nInsira o valor a sacar: "))
            if usrin < self.dinheiro or usrin == self.dinheiro:    
                self.dinheiro = self.dinheiro - usrin
            else: print("\nERRO\n Valor insuficiente na conta.")
        except TypeError: 
            print("apenas numeros, para decimais use .\nEX: Um real e cinquenta centavos = 1.50")

    def verExtrato(self):
        print(f"Total da conta: {self.dinheiro}")     
        return

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
 
class Cli_CS(Cliente): # conta salário
    def __init__(self, nome: str, cpf: str, dinheiro: float, username: str, senha: str, id_banco: str) -> None:
        super().__init__(nome, cpf, username, senha, id_banco)
        self.dinheiro = dinheiro

    
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
                print("\n\tERRO: Funcionário não encontrado")
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
                    return
            else: 
                continue
    else: print("\tERRO: não existem clientes cadastrados")         

def funcionarioMenu():
    global logged
    global activeUsr

    while logged:
        if isinstance(activeUsr, Gerente):
            usrin = input(
                "Escolha uma opção do menu.\n\t"
                "1) Novo Cliente\n\t"
                "2) Modificar/Remover cliente\n\t"
                "3) Excluir cadastro (cliente/consultor)\n\t"
                "4) Ver dados de cliente\n\t"
                "5) Ver dados de consultor\n\t"
                "6) Estatísticas do banco\n\t"
                "0) Sair "
            )

            match usrin:
                case "1": # add cliente
                    activeUsr.novoCadastro()
                case "2": # edit acc details
                    activeUsr.modificarCadastro()
                case "3": # remove acc
                    activeUsr.excluirCadastro()
                case "4": # ver dados cliente específico
                    activeUsr.verDadosCliente()
                case "5": # ver dados de consultor específico
                    activeUsr.verDadosConsultor()
                case "6": # estatísticas do banco (clientes/funcionarios)
                    activeUsr.getStats()
                case "0": # exit
                    activeUsr = None
                    logged = False
                case _:
                    print("opção inválida")

        elif isinstance(activeUsr, Consultor): # NÃO PODE REMOVER CADASTROS, MAS PODE EDITAR
            usrin = input("Escolha uma opção do menu.\n\t1)Novo Cliente\n\t2)Modificar cliente\n\t3)ph\n\t4)ph\n\t5)Sair ")

            match usrin:
                case "1": # add client
                    activeUsr.novoCadastro()
                case "2": # edit acc details
                    activeUsr.modificarCadastro()
                case "3": # calcular salario
                    activeUsr.calcularSalario()
                case "4": # ver dados do cliente
                    activeUsr.verDadosCliente() 
                case _:
                    print("Opção inválida")
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
        case "2": # SAIR
            usrin = 0
            break
        case _: # op invalida
            print("\nOpção inválida. ")