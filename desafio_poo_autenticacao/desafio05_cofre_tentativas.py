class CofreDigital:
    def __init__(self, senha):
        self.__senha = senha
        self.__tentativas = 0
        self.__bloqueado = False

    def abrir(self, senha_digitada):
        if self.__bloqueado:
            print("Cofre bloqueado.")
            return

        if senha_digitada == self.__senha:
            print("Cofre aberto.")
        else:
            self.__tentativas += 1
            print("Senha incorreta.")

            if self.__tentativas >= 3:
                self.__bloqueado = True
                print("Cofre bloqueado por excesso de tentativas.")


cofre = CofreDigital("9999")

for i in range(3):
    senha = input("Digite a senha do cofre: ")
    cofre.abrir(senha)
