from abc import ABC, abstractmethod
class BancoAbstracao(ABC):
    pass

@abstractmethod
def login(self):
    pass

@abstractmethod
def exibirConta(self):
    pass

class Banco:
    def __init__(self, cliente, saldo, senha):
        self.cliente = cliente
        self.saldo = saldo
        self.senha = senha
        self.status = False
    
    def entrada(self):
        print("\n--------- Sistema de Saldo Bancário ---------\n")

    def login(self):
        tentativas = 3

        while tentativas > 0:
            senha_digitada = input("Digite sua senha (Somente números): ")

            if senha_digitada == "":
                print("Digite Algo!")
                continue

            elif senha_digitada.isdigit() == False:
                print("Erro! Digite apenas números.")
                continue
            
            elif (len(senha_digitada)!=6):
                print("6 DÍGITOS OBRIGATÓRIOS!")
                continue

            elif int(senha_digitada) == self.senha:
                self.status = True
                print("\nLogin realizado com sucesso.\n")
                break
            
            else:
                tentativas -= 1
                print(f"Senha incorreta! Tentativas restantes: {tentativas}")
        
    
        
    def exibirConta(self):
        if self.status:
            print("===== DADOS DA CONTA =====")
            print("Cliente:", self.cliente)
            print(f"Saldo: R$ {self.saldo:.2f}")
        else:
            print("Acesso Negado!")

conta = Banco("Pedro", 2000, 777777)
conta.entrada()
conta.login()
conta.exibirConta()