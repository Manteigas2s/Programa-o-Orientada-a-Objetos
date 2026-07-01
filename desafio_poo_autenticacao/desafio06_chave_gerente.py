class Venda:
    def __init__(self, produto, valor, chave_gerente):
        self.produto = produto
        self.valor = valor
        self.__chave_gerente = chave_gerente

    def aplicar_desconto(self, percentual, chave_digitada):
        if chave_digitada == self.__chave_gerente:
            desconto = self.valor * percentual
            valor_final = self.valor - desconto
            print(f"Desconto autorizado.")
            print(f"Valor final: R$ {valor_final:.2f}")
        else:
            print("Chave de gerente inválida.")


venda1 = Venda("Notebook", 3000, "GER-2026")

chave = input("Digite a chave do gerente: ")

venda1.aplicar_desconto(0.10, chave)
