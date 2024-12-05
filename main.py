clienteList = []
funcionarioList = []
List = []
activeUsr = None
logged = False

############################
# CLASSES FUNCIONARIOS
############################
class Funcionario(): 
    def __init__(self, nome: str, cpf: str, bonus: float, username: str, senha: str, salario: float, atendimentos: int) -> None:
        self.nome = nome
        self.cpf = cpf
        self.bonus = bonus
        self.username = username
        self.senha = senha
        self.salario = salario
        self.atendimentos = atendimentos
        funcionarioList.append(self)

    def calcularSalario(self):
        pass # intencional, polimórfico nos filhos

    def novoCadastro(self):
        usrin = input("\n\tNOVO CADASTRO\n\t1)NOVO CLIENTE CONTA CORRENTE\n\t2)NOVO CLIENTE CONTA SALÁRIO\n\t3)NOVO GERENTE\n\t4)NOVO CONSULTOR\n\t(ESPAÇO PARA CANCELAR)\n>")

        if usrin == "":             
            input("\nPressione enter para continuar...")
            return

        nomein = input("\nInsira o nome do novo cliente: ")
        cpfin = input("\nInsira o cpf do novo cliente: ")
        usernamein = input("\nInsira o username do novo cliente (usado para acessar a conta): ")
        senhain = input("I\nnsira a senha do novo usuário: ")

        if usrin == "1": # CONTA CORRENTE
            newclient = Cli_CC(nome=nomein, cpf=cpfin, username=usernamein, senha=senhain, saldo=0, credMax=0)
            if nomein and cpfin and usernamein and senhain and newclient:
                print(f"Conta Corrente criada para {newclient.nome}, CPF - {newclient.cpf}")
                input("\n\tPressione enter para continuar... ")
                return
            else:
                print("proibido espaços em branco ")
    
        elif usrin == "2": # SALARIO
            newclient = Cli_CS(nome=nomein, cpf=cpfin, username=usernamein, senha=senhain, saldo=0)
            if nomein and cpfin and usernamein and senhain and newclient:
                print(f"Conta Salário criada para {newclient.nome}, CPF - {newclient.cpf}")
                input("\n\tPressione enter para continuar... ")
                return
            else:
                print("proibido espaços em branco ")
    
        elif usrin == "3": # GERENTE
            try:
                salarioin = float(input("Insira o salario do novo gerente: "))
                if nomein and cpfin and usernamein and senhain and salarioin:
                    newgerente = Gerente(nome=nomein, cpf=cpfin, bonus=0, username=usernamein, senha=senhain, salario=salarioin, atendimentos=0)
                    print(f"Conta de Gerente criada para {newgerente.nome}, CPF - {newgerente.cpf}")
                    input("\n\tPressione enter para continuar... ")
                else: 
                    print("proibido espaços em branco ")
            except ValueError:
                print("\nERRO: Insira apenas números para salário")
                input("\n\tPressione enter para continuar... ")
                return

        elif usrin == "4": # FUNCIONARIO

            try:
                salarioin = float(input("Insira o salario do novo consultor: "))
                if nomein and cpfin and usernamein and senhain and salarioin:    
                    newconsultor = Consultor(nome=nomein, cpf=cpfin, bonus=0, username=usernamein, senha=senhain, salario=salarioin, atendimentos=0)
                    print(f"Conta de Gerente criada para {newconsultor.nome}, CPF - {newconsultor.cpf}")
                    input("\n\tPressione enter para continuar... ")
                else: 
                    print("proibido espaços em branco ")                
            except ValueError:
                print("\nERRO: Insira apenas números para salário")
                input("\n\tPressione enter para continuar... ")
                return
        else:
            print(f"Opção '{usrin}' inválida")

    def modificarCliente(self):
        print("\n\t Lista de clientes ")
        for cliente in clienteList:
            print(f"\t{cliente.nome}")
                    
            search = input("\nDigite o nome do cliente desejado (ESPAÇO PARA CANCELAR): ")
            if search != "":
                for cliente in clienteList:
                    if search == cliente.nome:

                        nomein = input("Insira o nome do novo cliente (ESPAÇO PARA PULAR): ")
                        if nomein != "":
                            cliente.nome = nomein

                        cpfin = input("Insira o cpf do novo cliente (ESPAÇO PARA PULAR): ")
                        if cpfin != "":
                            cliente.cpf = cpfin

                        usernamein = input("Insira o username do novo cliente (ESPAÇO PARA PULAR): ")
                        if usernamein != "":
                            cliente.username = usernamein

                        senhain = input("Insira a senha do novo usuário (ESPAÇO PARA PULAR): ")
                        if senhain != "":
                            cliente.senha = senhain
                            
                        print("\nNOVOS DADOS:\n\t"
                        f"Nome: {cliente.nome}\n\t"
                        f"CPF: {cliente.cpf}\n\t"
                        f"Username: {cliente.username}\n\t"
                        f"Senha: {cliente.senha}\n\t")
                        input("\n\tPressione enter para continuar... ")
                        return
                    else: 
                        continue
            else: 
                print("\n\tERRO: Proibida entrada vazia. ")
                return
            print(f"\n\tERRO: Cliente '{search}' não encontrado, verifique a ortografia. ") 

    def modificarCadastroHandler(self, permissao):
        if permissao == "gerente":
            usrin = input("\n\t1) MODIFICAR CADASTRO DE CLIENTE\n\t2) MODIFICAR CADASTRO DE FUNCIONARIO\n\t(ESPAÇO PARA CANCELAR)\n>")
            if usrin == "1":
                self.modificarCliente()
                return

            elif usrin == "2":
                print("\n\t Lista de funcionarios ")
                for funcionario in funcionarioList:
                    print(f"\t{funcionario.nome}")
                
                search = input("\nDigite o nome do funcionario desejado: ")
                if search != "":
                    for funcionario in funcionarioList:
                        if search == funcionario.nome:
                            nomein = input("Insira novo nome do funcionario (ESPAÇO PARA PULAR): ")
                            if nomein != "":
                                funcionario.nome = nomein
                            cpfin = input("Insira novo cpf dofuncionario (ESPAÇO PARA PULAR): ")
                            if cpfin != "":
                                funcionario.cpf = cpfin
                            usernamein = input("Insira o novo username do funcionario (ESPAÇO PARA PULAR): ")
                            if usernamein != "":
                                funcionario.username = usernamein
                            senhain = input("Insira a nova senha do funcionario (ESPAÇO PARA PULAR): ")
                            if senhain != "":
                                funcionario.senha = senhain
                            print("\nNOVOS DADOS:\n\t"
                            f"Nome: {funcionario.nome}\n\t"
                            f"CPF: {funcionario.cpf}\n\t"
                            f"Username: {funcionario.username}\n\t"
                            f"Senha: {funcionario.senha}\n\t")
                            input("\n\tPressione enter para continuar... ")
                            return
                        else: 
                            continue
                else: 
                    print("\n\tERRO: Proibida entrada vazia. ")
                    return
                print(f"\n\tERRO: Funcionário '{search}' não encontrado, verifique a ortografia. ")     
            else: 
                print("\n\tOpção inválida")
                input("\n\tPressione enter para continuar... ")
                return

        elif permissao == "consultor":
            self.modificarCliente()

        input("\n\tPressione enter para continuar... ")

    def verDadosCliente(self):  
        print("\n\t Lista de clientes ")
        for cliente in clienteList:
            print(f"\t{cliente.nome}")

        search = input("\nDigite o nome do cliente desejado (ESPAÇO PARA CANCELAR): ")
        if search != "":
            for cliente in clienteList:
                if search == cliente.nome:
                    print(f"\n\tDados do cliente:"
                    f"\nNome: {cliente.nome}"
                    f"\nCPF: {cliente.cpf}"
                    f"\nUsername: {cliente.username}"
                    f"\nSenha: {cliente.senha}"
                    f"\nSaldo: {cliente.saldo}"
                    )
                    if isinstance(cliente, Cli_CC):
                        cliente.calcular_credMax()
                        print(f"Crédito Máximo:\t{cliente.credMax}")
                        input("\n\tPressione enter para continuar... ")
                        return
                    input("\n\tPressione enter para continuar... ")
                    return
                else: 
                    continue
        else: print("\n\tERRO: Proibida entrada vazia. ")
        print(f"\n\tERRO: Cliente '{search}' não encontrado, verifique a ortografia. ")
        input("\n\tPressione enter para continuar... ")

class Gerente(Funcionario):
    def __init__(self, nome: str, cpf: str, bonus: float, username: str, senha: str, salario: float, atendimentos: int) -> None:
        super().__init__(nome, cpf, bonus, username, senha, salario, atendimentos)

    def calcularSalario(self):
        self.bonus = self.atendimentos * 100
        self.salario = self.salario + self.bonus
        return self.salario

    def excluirCadastro(self): # excluir tanto funcionario / cliente
        usrin = input(
            "\n\t1)EXCLUIR CADASTRO DE CLIENTE"
            "\n\t2)EXCLUIR CADASTRO DE FUNCIONÁRIO\n\t(ESPAÇO PARA CANCELAR)\n>"
            )

        if usrin == "1":
            print("\n\tLista de clientes ")
            for cliente in clienteList:
                print(f"\t{cliente.nome}")

            search = input("\nDigite o nome do cliente desejado: ")
            if search != "":
                for cliente in clienteList:
                    if search == cliente.nome:
                        confirmation = input(f"\n\tTEM CERTEZA DE QUE QUER EXCLUIR O CADASTRO DO CLIENTE '{cliente.nome}'?"
                        "\n\tATENÇÃO: ESSA AÇÃO NÃO É REVERSÍVEL!!!"
                        "\n\tDIGITE 'S' OU 'N'"
                        )
                        if confirmation.lower() == "s":
                            del clienteList[clienteList.index(cliente)]
                            print(f"Cliente '{search}' removido, pressione enter para continuar...")
                            input("")
                            return
                        elif confirmation.lower() == "n":
                            print("\n\n\texclusão cancelada, pressione enter para retornar...")
                            input("")
                            return
                        else:
                            print(f"\n\n\nOPÇÃO '{confirmation}' INVÁLIDA, PRESSIONE ENTER PARA CONTINUAR...")
                            input("")
                            return

                print(f"FUNCIONARIO '{search}' NÃO ENCONTRADO")
                
            
        elif usrin == "2":
            print("\n\tLista de funcionarios: ")
            for funcionario in funcionarioList:
                    print(f"\t{funcionario.nome}")

            search = input("\nDigite o nome do funcionario desejado: ")
            if search != "":
                for funcionario in funcionarioList:
                    if search == funcionario.nome and search != activeUsr.nome:
                        confirmation = input(f"\n\tTEM CERTEZA DE QUE QUER EXCLUIR O CADASTRO DO FUNCIONARIO: '{funcionario.nome}'?"
                        "\n\tATENÇÃO: ESSA AÇÃO NÃO É REVERSÍVEL!!!"
                        "\n\tDIGITE 'S' OU 'N'"
                        )
                        if confirmation.lower() == "s":
                            del funcionarioList[funcionarioList.index(funcionario)]
                            print(f"Funcionario '{search}' removido, pressione enter para continuar...")
                            input("")
                            return
                        elif confirmation.lower() == "n":
                            print("\n\n\texclusão cancelada, pressione enter para retornar...")
                            input("")
                            return
                        else:
                            print(f"\n\n\nOPÇÃO '{confirmation}' INVÁLIDA, PRESSIONE ENTER PARA CONTINUAR...")
                            input("")
                            return
                    else: 
                        continue
                print(f"\nFUNCIONARIO '{search}' NÃO ENCONTRADO"
                f"\nVERIFIQUE A ORTOGRAFIA; TAMBÉM NÃO É POSSÍVEL EXCLUIR O USUÁRIO ATUAL.")

        else: 
            print("opção inválida")
            input("\nPressione enter para continuar...")


    def verDadosConsultor(self):
        print("\n\t Lista de consultores: ")
        for consultor in funcionarioList:
            if isinstance(consultor, Consultor):    
                print(f"\t{consultor.nome}")
            else: 
                continue

        search = input("\nDigite o nome do consultor desejado: ")
        if search != "":
            for consultor in funcionarioList:
                if search == consultor.nome:
                    consultor.calcularSalario()
                    print(f"\n\tDados do cliente:"
                    f"\nNome: {consultor.nome}"
                    f"\nCPF: {consultor.cpf}"
                    f"\nUsername: {consultor.username}"
                    f"\nSenha: {consultor.senha}"
                    f"\nSalário: {consultor.salario}"
                    f"\nAtendimentos: {consultor.atendimentos}"
                    f"\nBonus atual: {consultor.bonus}")
                    input("\n\tPressione enter para continuar... ")
                    return
                else: 
                    continue
        else: 
            print("\n\tERRO: Proibida entrada vazia. ")
            input("\nPressione enter para continuar...")
            return
        print("\n\tERRO: Consultor não encontrado, verifique a ortografia. ")

class Consultor(Funcionario):
    def __init__(self, nome: str, cpf: str, bonus: float, username: str, senha: str, salario: float, atendimentos: int) -> None:
        super().__init__(nome, cpf, bonus, username, senha, salario, atendimentos)

    def calcularSalario(self):
        self.bonus = self.atendimentos * 25
        self.salario = self.salario + self.bonus
        return self.salario

############################
# CLASSES CLIENTES  
############################
class Cliente():
    def __init__(self, nome: str, cpf: str, username: str, senha: str, saldo: float) -> None:
        self.nome = nome
        self.cpf = cpf
        self.username = username
        self.senha = senha
        self.saldo = saldo
        clienteList.append(self)

    def saque(self):       
        try:
            usrin = float(input("\nInsira o valor a sacar: "))
            if usrin < self.saldo or usrin == self.saldo:    
                self.saldo = self.saldo - usrin
                print(f"'{usrin}' reais sacados com sucesso.")
                input("\nPressione enter para continuar...")
            else: print("\nERRO\n Valor insuficiente na conta.")
        except ValueError: 
            print("apenas numeros, para decimais use .\nEX: Um real e cinquenta centavos = 1.50")
            input("\nPressione enter para continuar...")

    def verExtrato(self):
        print(f"Total da conta: {self.saldo}")  
        input("\nPressione enter para continuar...")
        return

class Cli_CC(Cliente): # conta corrente
    def __init__(self, nome: str, cpf: str, username: str, senha: str, saldo: float, credMax: float)-> None:
        super().__init__(nome, cpf, username, senha, saldo)
        self.credMax = saldo + (saldo * 0.5)

    def calcular_credMax(self):
        # função arbirtária para cálculo, apenas exemplo
        credMax = 0
        if self.saldo > 0:
            credMax = self.saldo + (self.saldo * 0.5)
            self.credMax = credMax
            return credMax
        else: 
            self.credMax == 0
            return credMax

    def depositar(self):
        try:
            usrin = float(input("\nInsira o valor a depositar: "))
            self.saldo = self.saldo + usrin
            self.calcular_credMax() # precisa chamar com o self sempre que referencia funcao dentro da classe
            print(f"\nNovo saldo: {self.saldo}")
            print(f"Novo crédito máximo: {self.credMax}")

        except ValueError: 
            print("\nERRO: Apenas numeros, para decimais use '.'\nEX: Mil reais e cinquenta centavos = 1.50")
            input("\nPressione enter para continuar...")

class Cli_CS(Cliente): # conta salário
    def __init__(self, nome: str, cpf: str, saldo: float, username: str, senha: str) -> None:
        super().__init__(nome, cpf, username, senha, saldo)

############################

def login_system(tipo: str):
    usrname = input("Usuario> ")
    global logged # checa se está logado
    global activeUsr # pointer para a instancia do usuário ativo 

    if tipo == "funcionario":
        if funcionarioList and not logged:
            for funcionario in funcionarioList:
                if usrname == funcionario.username:
                    passw = input(f"Senha> ")
                    if passw == funcionario.senha:
                        logged = True
                        activeUsr = funcionario
                        return funcionarioMenu()
                    else: 
                        print("senha errada...")

            print("\n\tERRO: Funcionário não encontrado")
        else: print("\n\tERRO: não existem funcionários cadastrados")

    elif tipo == "cliente":
        if clienteList and not logged:
            for cliente in clienteList:
                if usrname == cliente.username:
                    passw = input(f"Senha> ")
                    if passw == cliente.senha:
                        logged = True
                        activeUsr = cliente
                        return clienteMenu()
                    else: 
                        print("senha errada...")
                        return
                else: 
                    continue

            print("\n\tERRO: Cliente não encontrado")           
        else: print("\tERRO: não existem clientes cadastrados")         

def funcionarioMenu():
    global logged
    global activeUsr

    while logged:
        if isinstance(activeUsr, Gerente):
            usrin = input(
                "\nEscolha uma opção do menu. (ESPAÇO CANCELA QUALQUER OPÇÃO (ENVIAR ESPAÇOS VAZIOS))\n\t"
                "1) Novo Cliente ou Funcionário\n\t"
                "2) Modificar cliente ou funcionário\n\t"
                "3) Excluir cadastro (cliente/consultor)\n\t"
                "4) Ver dados de cliente\n\t"
                "5) Ver dados de consultor\n\t"
                "6) Estatísticas\n\t"
                "0) Sair \n>"
            )

            match usrin:
                case "1": # add cliente
                    activeUsr.novoCadastro()
                case "2": # edit acc details
                    activeUsr.modificarCadastroHandler("gerente")
                case "3": # remove acc
                    activeUsr.excluirCadastro()
                case "4": # ver dados cliente específico
                    activeUsr.verDadosCliente()
                case "5": # ver dados de consultor específico
                    activeUsr.verDadosConsultor()
                case "6": # estatísticas do  (clientes/funcionarios)
                    getStats()
                case "0": # exit
                    activeUsr = None
                    logged = False
                case _:
                    print("Opção inválida")

        elif isinstance(activeUsr, Consultor): # NÃO PODE REMOVER CADASTROS, MAS PODE EDITAR
            usrin = input("\nEscolha uma opção do menu. (ESPAÇO CANCELA QUALQUER OPÇÃO (ENVIAR ESPAÇOS VAZIOS))\n\t"
            "1)Novo Cliente\n\t"
            "2)Modificar cadastro de Cliente\n\t"
            "3)Ver dados de cliente\n\t"
            "4)Calcular meu salário\n\t"
            "0)Sair\n>")

            match usrin:
                case "1": # add client
                    activeUsr.novoCadastro()
                case "2": # edit acc details
                    activeUsr.modificarCadastroHandler("consultor")
                case "3": # ver dados do cliente
                    activeUsr.verDadosCliente() 
                case "4": # calcular salario de si mesmo
                    print(f"\n\tSeu salário é: '{activeUsr.calcularSalario()}' reais")
                case "0": # sair
                    activeUsr = None
                    logged = False
                case _:
                    print("Opção inválida")
def clienteMenu():
    global logged
    global activeUsr

    while logged:
        if isinstance(activeUsr, Cli_CC):
            usrin = input("\nEscolha uma opção do menu. (ESPAÇO CANCELA QUALQUER OPÇÃO (ENVIAR ESPAÇOS VAZIOS))\n\t"
                        "1)Depositar\n\t"
                        "2)Sacar\n\t"
                        "3)Calcular Crédito\n\t"
                        "4)Ver extrato\n\t"
                        "0)Sair\n\t>")

            match usrin:
                case "1":
                    activeUsr.depositar()
                case "2":
                    activeUsr.saque()
                case "3":
                    print(f"\nCrédito máximo atual: {activeUsr.calcular_credMax()}")
                    input("\nPressione enter para continuar...")
                case "4":
                    activeUsr.verExtrato()
                case "0":
                    activeUsr = None
                    logged = False
                case _:
                    print("Opção inválida")

        elif isinstance(activeUsr, Cli_CS):
            usrin = input("\nEscolha uma opção do menu. (ESPAÇO CANCELA QUALQUER OPÇÃO (ENVIAR ESPAÇOS VAZIOS))\n\t"
                        "1)Sacar\n\t"
                        "2)Ver extrato\n\t"
                        "0)Sair\n\t>")
            
            match usrin:
                case "1":
                    activeUsr.saque()
                case "2":
                    activeUsr.verExtrato()
                case "0":
                    activeUsr = None
                    logged = False
                case _:
                    print("Opção inválida")

def getStats(): 
    usrin = input("\n\t1)Estatísticas de funcionário\n\t2)Estatísticas de clientes\n\t3)Folha salarial\n>")
    if usrin == "1":    
        maiorSalario = funcionarioList[0] 
        menorSalario = funcionarioList[0]
        quantidadeTotal = 0
        totalfunc = 0
        qntdGR = 0
        qntdCSTR = 0

        for funcionario in funcionarioList:
            
            totalfunc += 1
            if isinstance(funcionario, Gerente):
                qntdGR += 1
            elif isinstance(funcionario, Consultor):
                qntdCSTR += 1

            if funcionario.salario > maiorSalario.salario:
                maiorSalario = funcionario
                
            if funcionario.salario < menorSalario.salario:
                menorSalario = funcionario

            quantidadeTotal += 1 

        print(f"\nExistem {totalfunc} funcionários trabalhando no banco. {qntdGR} são gerentes e {qntdCSTR} são consultores"
            f"\nO maior salario é do funcionario {maiorSalario.nome}, salario: {maiorSalario.salario}"
            f"\nO menor salario é do funcionario {menorSalario.nome}, salario: {menorSalario.salario}"
            )
        input("\n\tPressione enter para continuar... ")
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

        print(f"\nExistem {qntdTotal} clientes/contas no banco.\n{qntdCC} são contas correntes e {qntdCS} são contas salário")
        input("\n\tPressione enter para continuar... ")
    elif usrin == "3":
        print("\nFOLHA SALARIAL")
        total = 0
        for funcionario in funcionarioList:

            salarioTemp = funcionario.calcularSalario()
            total += salarioTemp
            print(f"\nNome: {funcionario.nome} || Salário: {salarioTemp}")
        
        print(f"\nGasto total com salarios: {total}")
        input("\n\tPressione enter para continuar... ")
    else:
        print(f"Opção '{usrin}' inválida.")
        input("\nPressione enter para continuar...")
        return


### DEBUG
# DEFAULT USUARIOS
admin = Gerente(nome="Gerente", cpf="12345678900", bonus=0, username="admin", senha="123", salario=13000, atendimentos=5)
consultorTeste = Consultor(nome="Consultor", cpf="12345678900", bonus=0, username="consultor", senha="123", salario=3000, atendimentos=15)
ClienteCCteste = Cli_CC(nome="Fulano", cpf="123123123", username="fulano", senha="123", saldo=1000, credMax=0)

while True:
    usrin = input("\n\t1)Login funcionario\n\t2)Login cliente\n\t0)Sair:\n>")
    # always define usrin 0 BEFORE calling any functions
    match usrin:
        case "1": # LOGIN
            usrin = 0
            login_system("funcionario")
        case "2":
            usrin = 0
            login_system("cliente")
        case "0": # SAIR
            usrin = 0
            break
        case _: # op invalida
            print("\nOpção inválida. ")