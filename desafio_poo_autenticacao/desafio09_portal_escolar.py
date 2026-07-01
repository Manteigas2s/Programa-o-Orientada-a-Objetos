class UsuarioPortal:
    def __init__(self, nome, codigo):
        self.nome = nome
        self.__codigo = codigo

    def verificar_codigo(self, codigo_digitado):
        return codigo_digitado == self.__codigo


class Aluno(UsuarioPortal):
    def acessar(self):
        print(f"{self.nome} acessou a área do aluno.")


class Professor(UsuarioPortal):
    def acessar(self):
        print(f"{self.nome} acessou a área do professor.")


class Coordenador(UsuarioPortal):
    def acessar(self):
        print(f"{self.nome} acessou a área da coordenação.")


usuarios = [
    Aluno("Carlos", "ALU-1"),
    Professor("Mariana", "PROF-2"),
    Coordenador("Ana", "COORD-3")
]

for usuario in usuarios:
    codigo = input(f"Digite o código de {usuario.nome}: ")

    if usuario.verificar_codigo(codigo):
        usuario.acessar()
    else:
        print("Código inválido.")
