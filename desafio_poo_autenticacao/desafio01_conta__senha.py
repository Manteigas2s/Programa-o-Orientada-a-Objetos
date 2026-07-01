class ContaBancaria:
    def __init__(self, titular, saldo, senha):
        self.titular = titular
        self.__saldo = saldo
        self.__senha = senha
        self.autenticado = False

    def autenticar(self, senha_digitada):
        if senha_digitada == self.__senha:
            self.autenticado = True
            print("Acesso liberado.")
        else:
            print("Senha incorreta.")

    def mostrar_saldo(self):
        if self.autenticado:
            print(f"Titular: {self.titular}")
            print(f"Saldo: R$ {self.__saldo:.2f}")
        else:
            print("Acesso negado. Autentique-se primeiro.")


conta1 = ContaBancaria("Ana", 1500, "1234")

senha = input("Digite a senha: ")

conta1.autenticar(senha)
conta1.mostrar_saldo()
