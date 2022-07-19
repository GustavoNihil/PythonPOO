





# PRIMEIRA PARTE - DIFERENÇA ENTRE ATRIBUTOS DE INSTÂNCIA "SELF" E DE CLASSE "CLS"
class Usuarioo:
    cargo = 'usuário'

    def __init__(self, nome, idade, altura): #"__init__" é executado assim que uma variável recebe a "class"
        print(nome)
        self.x = 1 #self referencia a si mesmo
        self.altura = altura

    def retorna_altura(self):
        print(self.altura) #atravéz do "self" consigo acessar uma variável definida em outro método

    def exibe_cargo(cls):
        print(cls.cargo)


usuarioo1 = Usuarioo('Caio', 21, 176)
usuarioo2 = Usuarioo('Marcos', 31, 180)
print(usuarioo1.x)
usuarioo1.x = 10 #modifica o atributo (de instância) apenas daquele usuário, não interferindo nos outros
#o atributo de classe - diferentemente do de instância, com "self" - é igual para todos os objetos
print('-----')
print(usuarioo1.x)
print(usuarioo2.x)

usuarioo1.retorna_altura()

usuarioo1.exibe_cargo()
Usuarioo.cargo = 'Gerente' #com "cls" (atribuição de classe) a modificação é feita para todos os objetos
usuarioo1.exibe_cargo()
usuarioo2.exibe_cargo()

print('PRIMEIRA PARTE:') # PRIMEIRA PARTE - ATRIBUTOS E MÉTODOS
class Usuario: #uma classe possuí atributos e métodos. Atributos são valores atribuídos ao objeto, já o método é oque o objeto modelado faz.
    #um método é uma função dentro de uma classe. Ex:

    def logar(self):
        print('fui chamado')

    #atributos (características comuns entre os objetos):
    cargo = 'usuário'
    

usuario1 = Usuario() #o usuario1 adquire as propriedades do objeto Usuario

print(usuario1) #cada instância da classe ganha uma atribuição de endereço de memória

usuario1.logar() #consigo executar um método do objeto

print(usuario1.cargo) #informa o valor atribuído ao usuario1



