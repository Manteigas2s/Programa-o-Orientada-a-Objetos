class PagamentoPix:
    def pagar(self, valor):
        print(f"Pagamento via Pix realizado no valor de R$ {valor:.2f}.")

class PagamentoCartao:
    def pagar(self, valor):
        print(f"Pagamento via Pix realizado no valor de R$ {valor:.2f}.")

class PagamentoBoleto:
    def pagar(self, valor):
        print(f"Boleto gerado no valor de R$ {valor:.2f}. Aguardando pagamento.")

pagamentos = [
    PagamentoPix(),
    PagamentoCartao(),
    PagamentoBoleto()
]

for pagamento in pagamentos:
    pagamento.pagar(150)