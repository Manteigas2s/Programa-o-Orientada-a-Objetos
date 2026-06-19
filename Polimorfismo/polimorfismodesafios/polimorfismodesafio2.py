class FreteTerrestre:
    def calcular_frete(self, peso, distancia):
        valor = peso * distancia * 0.05
        return valor


class FreteAereo:
    def calcular_frete(self, peso, distancia):
        
        valor = peso * distancia * 0.12
        return valor


class RetiradaLoja:
    def calcular_frete(self, peso, distancia):
        
        valor = peso * distancia
        return valor


fretes = [
    FreteTerrestre(),
    FreteAereo(),
    RetiradaLoja()
]

for frete in fretes:
    valor_frete = frete.calcular_frete(10, 100)
    print(f"Valor do frete: R$ {valor_frete:.2f}")