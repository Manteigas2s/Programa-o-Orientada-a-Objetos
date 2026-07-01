class AutenticacaoSenha:
    def autenticar(self, valor):
        if valor == "1234":
            print("Autenticado por senha.")
        else:
            print("Senha inválida.")


class AutenticacaoChave:
    def autenticar(self, valor):
        if valor == "CHAVE-ABC":
            print("Autenticado por chave de acesso.")
        else:
            print("Chave inválida.")


class AutenticacaoCodigo:
    def autenticar(self, valor):
        if valor == "7890":
            print("Autenticado por código temporário.")
        else:
            print("Código inválido.")


autenticadores = [
    AutenticacaoSenha(),
    AutenticacaoChave(),
    AutenticacaoCodigo()
]

for autenticador in autenticadores:
    dado = input("Digite senha, chave ou código: ")
    autenticador.autenticar(dado)
