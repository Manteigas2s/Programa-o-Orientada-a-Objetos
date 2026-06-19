class VendedorInterno:
    def calcular_comissao(self, valor_venda):
        return valor_venda * 0.03


class VendedorExterno:
    def calcular_comissao(self, valor_venda):
        # Comissão de 5%
        return valor_venda * 0.05


class VendedorMarketplace:
    def calcular_comissao(self, valor_venda):
        # Comissão de 8%
        return valor_venda * 0.08


vendedores = [
    VendedorInterno(),
    VendedorExterno(),
    VendedorMarketplace()
]

valor_venda = 2000

for vendedor in vendedores:
    comissao = vendedor.calcular_comissao(valor_venda)
    print(f"Comissão calculada: R$ {comissao:.2f}")
