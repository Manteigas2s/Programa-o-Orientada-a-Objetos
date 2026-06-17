class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.__preco = preco

    @property
    def preco(self):
        return self.__preco
    
    @preco.setter
    def preco(self, novo_preco):
        if novo_preco > 0:
            self.__preco = novo_preco
            print("Preço alterado com sucesso!")
        else:
            print("Preço deve ser maior que zero.")

    def mostrar_produtos(self):
        print(f"Produto: {self.nome}")
        print(f"Preço: R$ {self.__preco:.2f}")

produto1 = Produto("Mémoria Ram", 500)

produto1.mostrar_produtos()

produto1.preco = 800
produto1.mostrar_produtos()

produto1.preco = -300
produto1.mostrar_produtos()