from abc import ABC, abstractmethod


class Autenticador(ABC):
    @abstractmethod
    def autenticar(self, valor):
        pass


class LoginSenha(Autenticador):
    def autenticar(self, valor):
        if valor == "1234":
            print("Login autorizado.")
        else:
            print("Login negado.")


class LoginCodigo(Autenticador):
    def autenticar(self, valor):
        # Complete a verificação do código 5555
        if valor == "________":
            print("Código autorizado.")
        else:
            print("Código inválido.")


login1 = LoginSenha()
login2 = LoginCodigo()

login1.autenticar("1234")
login2.autenticar("5555")
