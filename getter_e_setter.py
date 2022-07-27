
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * percentual / 100)

    # Getter - Obtem
    @property
    def preco(self): # sempre que o "preco" é chamado, o getter entra em ação
        return self._preco # o valor da variável possuí um "_" na frente para evitar looping

    # Setter - Configura
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str): #se for uma string
            valor = float(valor.replace('R$', ''))

        self._preco = valor

    #outro exemplo
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor_nome):
        self._nome = valor_nome.title()  # "title()" transforma a primeira letra em maiuscula e o restante em minuscula


p1 = Produto('camisa', 50)
p1.desconto(10)
print(p1.nome, p1.preco)

p2 = Produto('caneca', 'R$15') # usando getter e setter para filtrar o valor atribuído, para que seja um número e não uma string
p2.desconto(10)
print(p2.nome, p2.preco)




