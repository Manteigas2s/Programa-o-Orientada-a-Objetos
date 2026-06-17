class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.__idade = idade
    @property 
    def idade(self):
        return self.__idade 
    
    @idade.setter
    def idade(self, nova_idade):
        if nova_idade >= 0:
            self.__idade = nova_idade   
        else:
            print("A idade não pode ser negativa.")
    
    def apresentar(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.__idade}")
    
pessoa1 = Pessoa("Pedro", 20)
pessoa1.apresentar()

pessoa1.idade = 21
pessoa1.apresentar()

pessoa1.idade = -5
pessoa1.apresentar()