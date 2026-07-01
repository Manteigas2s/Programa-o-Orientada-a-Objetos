from abc import ABC, abstractmethod

class BancoAbstracao(ABC):
    @abstractmethod
    def login(self):
        pass

class Banco(BancoAbstracao):
    def __init__(self, cliente: str, saldo: float, senha: int):
        self.cliente = cliente
        self.saldo = saldo
        self.__senha = senha
        self.__status = False
    
    def mostrarMenu(self):
        print("\n--------- Sistema de Saldo Bancário ---------\n")

    def validarSenha(self, senha):
        if senha == "":
                print("Digite Algo!")
                return False

        elif not senha.isdigit():
                print("Erro! Digite apenas números.")
                return False
            
        elif len(senha) !=6:
                print("6 DÍGITOS OBRIGATÓRIOS!")
                return False
        return True

    def login(self) -> bool:
        tentativas = 3

        while tentativas > 0:
            senha = input("Digite sua senha (Somente números): ")

            if not self.validarSenha(senha):
                 continue
            
            if int(senha) == self.__senha:
                self.__status = True
                print("\nLogin realizado com sucesso.\n")
                return True
            
            tentativas -= 1     
            print(f"Senha incorreta! Tentativas restantes: {tentativas}")
        
        print("Conta Bloqueada.")
        return False
    
        
    def mostrarDadosConta(self):
        if self.__status:
            print("===== DADOS DA CONTA =====")
            print("Cliente:", self.cliente)
            print(f"Saldo: R$ {self.saldo:.2f}")
        else:
            print("Acesso Negado!")

conta = Banco("Pedro", 2000, 777777)

conta.mostrarMenu()

if conta.login():
    conta.mostrarDadosConta()