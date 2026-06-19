class Animal:
    def som(self):
        print("O animal emite um som")

class Cachorro(Animal):
    def som(self):
        print("Cachorro: Au Au!")

class Gato(Animal):
    def som(self):
        print("Gato: Miau")

class Vaca(Animal):
    def som(self):
        print("Vaca: Muuu")

animais = [
    Cachorro(),
    Gato(),
    Vaca()
]

for animal in animais:
    animal.som()