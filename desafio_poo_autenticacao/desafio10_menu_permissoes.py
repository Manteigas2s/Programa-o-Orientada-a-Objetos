class Perfil:
    def __init__(self, nome, senha):
        self.nome = nome
        self.__senha = senha

    def autenticar(self, senha_digitada):
        return senha_digitada == self.__senha

    def menu(self):
        pass


class Operador(Perfil):
    def menu(self):
        print("Menu Operador: consultar dados.")


class Supervisor(Perfil):
    def menu(self):
        print("Menu Supervisor: consultar e aprovar solicitações.")


class Administrador(Perfil):
    def menu(self):
        print("Menu Administrador: acesso completo ao sistema.")


perfis = [
    Operador("João", "1111"),
    Supervisor("Carla", "2222"),
    Administrador("Marcos", "3333")
]

for perfil in perfis:
    senha = input(f"Digite a senha de {perfil.nome}: ")

    if perfil.autenticar(senha):
        perfil.menu()
    else:
        print("Senha inválida.")
