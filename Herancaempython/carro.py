from veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, modelo, marca, ano, quantidade_portas):
        super().__init__(modelo, marca, ano, quantidade_portas)
        self.quantidade_portas = quantidade_portas
    
    def mostrar_portas(self):
        print("===== QUANTIDADADE DE PORTAS =====")
        print(f"{self.quantidade_portas}")