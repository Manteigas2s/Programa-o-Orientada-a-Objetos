class Entrega:
    def __init__(self, codigo_pedido, destino):
        self.codigo_pedido = codigo_pedido
        self.destino = destino

    def mostrar_entrega(self):
        print(f"Pedido: {self.codigo_pedido}")
        print(f"Destino: {self.destino}")


class EntregaEspecial(Entrega):
    def __init__(self, codigo_pedido, destino, chave_liberacao):
        super().__init__(codigo_pedido, destino)
        self.__chave_liberacao = chave_liberacao

    def liberar_entrega(self, chave_digitada):
        if chave_digitada == self.__chave_liberacao:
            print("Entrega especial liberada.")
            self.mostrar_entrega()
        else:
            print("Chave de liberação inválida.")


entrega = EntregaEspecial("PED-1001", "Fortaleza", "LOG-555")

chave = input("Digite a chave logística: ")

entrega.mostrar_entrega(chave)
