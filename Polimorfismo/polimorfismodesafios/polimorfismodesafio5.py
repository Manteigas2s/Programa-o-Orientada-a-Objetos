class MultaFixa:
    def calcular_multa(self, valor, dias):
        return 10 


class MultaPorDia:
    def calcular_multa(self, valor, dias):
        return dias * 2


class MultaPercentual:
    def calcular_multa(self, valor, dias):
        return valor * 0.02


multas = [
    MultaFixa(),
    MultaPorDia(),
    MultaPercentual()
]

valor_boleto = 500
dias_atraso = 5

for multa in multas:
    valor_multa = multa.calcular_multa(valor_boleto, dias_atraso)
    total = valor_boleto + valor_multa

    print(f"Multa: R$ {valor_multa:.2f}")
    print(f"Total a pagar: R$ {total:.2f}")
