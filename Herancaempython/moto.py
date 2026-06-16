from veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, modelo, marca, ano, cilindradas):
        super().__init__(modelo, marca, ano, cilindradas)
    
    def mostrar_cilindradas(self):
        print("===== CILINDRADAS DA MOTO =====")
        print(f"{self.mostrar_cilindradas}")