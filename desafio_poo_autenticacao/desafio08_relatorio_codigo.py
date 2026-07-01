class RelatorioFinanceiro:
    def __init__(self, titulo, total_vendas, codigo_acesso):
        self.titulo = titulo
        self.total_vendas = total_vendas
        self.__codigo_acesso = codigo_acesso

    def gerar_relatorio(self, codigo_digitado):
        if codigo_digitado == self.__codigo_acesso:
            print("Relatório autorizado.")
            print(f"Título: {self.titulo}")
            print(f"Total de vendas: R$ {self.total_vendas:.2f}")
        else:
            print("Código de acesso inválido.")


relatorio = RelatorioFinanceiro("Relatório Mensal", 45000, "FIN-123")

codigo = input("Digite o código financeiro: ")

relatorio.gerar_relatorio(codigo)
