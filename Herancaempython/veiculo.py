class Veiculo:
    def __init__(self,modelo,marca,ano):
        self.modelo = modelo
        self.marca = marca
        self.ano = ano
    
    def apresentar(self):
        print("===== DADOS DO VEÍCULO =====")
        print(f"Modelo: {self.modelo}")
        print(f"Marca: {self.marca}")
        print(f"Ano: {self.ano}")
