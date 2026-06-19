class ClienteComum:
    def calcular_desconto(self, total):
        return total * 0.05


class ClienteVIP:
    def calcular_desconto(self, total):
        return total * 0.10


class ClienteAtacadista:
    def calcular_desconto(self, total):
        return total * 0.15


clientes = [
    ClienteComum(),
    ClienteVIP(),
    ClienteAtacadista()
]

total_compra = 1000

for cliente in clientes:
    desconto = cliente.calcular_desconto(total_compra)
    valor_final = total_compra - desconto

    print(f"Desconto: R$ {desconto:.2f}")
    print(f"Valor final: R$ {valor_final:.2f}")
