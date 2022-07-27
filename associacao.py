# ASSOCIAÇÃO

class Escritor:
    def __init__(self, nome):
        self.nome = nome
        self.ferramenta = None

class Caneta:
    def __init__(self, marca):
        self.marca = marca

    def escrever(self):
        print('Caneta está escrevendo...')

class MaquinaDeEscrever:
    def escrever(self):
        print('Máquina está escrevendo...')

# Execução das classes em 'associacao2'

#--------------------------------------------- AGREGAÇÃO

class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []

    def inserir_produto(self, produto):
        self.produtos.append(produto)

    def lista_produtos(self):
        for produto in self.produtos:
            print(produto.nome, produto.valor)

    def soma_total(self):
        total = 0
        for produto in self.produtos:
            total += produto.valor
        print(total)

class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

carrinho = CarrinhoDeCompras()
produto1 = Produto('Caneta', 2)
produto2 = Produto('Resistor', 0.25)
produto3 = Produto('SSD', 225)
carrinho.inserir_produto(produto1)
carrinho.inserir_produto(produto2)
carrinho.inserir_produto(produto3)
carrinho.inserir_produto(produto1)
carrinho.lista_produtos()
carrinho.soma_total()

#----------------------------------------- COMPOSIÇÃO - Ao apagar um objeto os outros abjetos atribuídos a ele tamvém são apagados

class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.enderecos = []

    def insere_endereco(self, cidade, estado):
        self.enderecos.append(Endereco(cidade, estado)) #uma função de uma classe que cria um objeto dentro de outro objeto

    def lista_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.cidade, endereco.estado)

    def __del__(self):
        print('{} FOI APAGADO'.format(self.nome))

class Endereco:
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado

    def __del__(self):
        print('{}/{} FORAM APAGADOS'.format(self.cidade, self.estado))

cliente1 = Cliente('Gustavinho', 19)
cliente1.insere_endereco('Belo Horizonte', 'MG')
cliente2 = Cliente('Maria', 31)
cliente2.insere_endereco('Salvador', 'BA')
cliente2.insere_endereco('Rio de Janeiro', 'RJ')
cliente3 = Cliente('Luix', 18)
cliente3.insere_endereco('São Paulo', 'SP')
print(cliente1.nome)
cliente1.lista_enderecos()
del cliente1 # ao apagar o objeto 'cliente1' o objeto da classe 'Endereco' também é apagado
print()
print(cliente2.nome)
cliente2.lista_enderecos()
print()
print(cliente3.nome)
cliente3.lista_enderecos()

print('############################################')

#------------------------------------------------ Revisão em HERANÇA

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.classe = self.__class__.__name__

    def falar(self):
        print('{} falando...'. format(self.classe))

class Aluno(Pessoa):
    def estudar(self):
        print(f'{self.classe} estudando...')

class Marinheiro(Pessoa):
    def navegar(self):
        print(f'{self.classe} navegando....')

aluno1 = Aluno('Genivaldo', 23)
marinheiro1 = Marinheiro('Luffy', 19)

print(aluno1.nome)
print(marinheiro1.nome)

aluno1.falar()
marinheiro1.falar()
aluno1.estudar()
marinheiro1.navegar()

