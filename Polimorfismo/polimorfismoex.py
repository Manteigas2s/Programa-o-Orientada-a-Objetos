animais = []

class Animais:
    def __init__(self):
        print(f"\nSONS DOS ANIMAIS\n")
        

class Cachorro():
    def som(self):
        print(f"O Cachorro faz auau!")

class Gato():
    def som(self):
        print(f"O Gato faz miau!")

class Vaca():
    def som(self):
        print(f"A Vaca faz muu!")

Animais()
animais = [Cachorro(), Gato(), Vaca()]

for animal in animais:
    animal.som()