class Usuario:
    def __init__(self, nome, senha):
        self.nome = nome
        self.__senha = senha

    def verificar_senha(self, senha_digitada):
        return senha_digitada == self.__senha


class Administrador(Usuario):
    def __init__(self, nome, senha, chave_acesso):
        super().__init__(nome, senha)
        self.__chave_acesso = chave_acesso

    def verificar_chave(self, chave_digitada):
        return chave_digitada == self.__chave_acesso


admin = Administrador("Mariana", "1234", "ADM-2026")

senha = input("Senha: ")
chave = input("Chave de acesso: ")

if admin.verificar_senha(senha) and admin.verificar_chave(chave):
    print("Acesso administrativo liberado.")
else:
    print("Acesso negado.")
