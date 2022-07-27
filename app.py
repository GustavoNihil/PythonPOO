# TERCEIRA PARTE - HERANÇA E SOBREPOSIÇÃO
# atravéz disso é possível colocar classes dentro de outra classe (ex: uma classe destinada à "Secretária" que está dentro de uma classe "Pessoa" que recebe atribuição de CPF)


class Pessoa:

    def __init__(self, nome, cpf, altura):
        self.cpf = cpf
        self.altura = altura
        self.nome = nome
        print('Nova pessoa cadastrada')

    def exibe_cpf(self):
        return "000674568878"


class Secretario(Pessoa): #entre parênteses coloca-se a classe herdada por ela

    def __init__(self, id_secretaria, nome, cpf, altura): #por padrão executará o "__init__" da classe filha, caso exista; caso não exista irá procurar na classe pai
        super().__init__(nome, cpf, altura) #com o "super()" é possível acessar os métodos da classe pai
        self.id_secretaria = id_secretaria

class Padeiro(Pessoa):
    pass

s1 = Secretario('2', 'Marcos', '45677', 178) # ao cadastrar um Secretário ou Padeiro, a def __init__ da classe Pessoa é executada
p1 = Padeiro('Antônio', '90893', 165)

print(s1.exibe_cpf()) # Secretário adiquire as atribuições de CPF de Pessoa


# PRIMEIRA PARTE - DIFERENÇA ENTRE ATRIBUTOS DE INSTÂNCIA "SELF" E DE CLASSE "CLS" / "@classmethod" e "@staticmethod"
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

    @classmethod #é possível acessar os atributos de classe, porém não de instância
    def cargo_usuario(cls):
        print(cls.cargo)

    @staticmethod #não acessa atributos de instância e nem de classe - "self" nem "cls"
    def e_adulto(idade):
        if idade >= 18:
            print(True)
        else:
            print(False)

Usuarioo.e_adulto(19)
Usuarioo.cargo_usuario() #Ao tentar executar dá erro. Porém ao usar o "@classmethod" passa a ser possível ter acésso à atributos de classe atravéz de métodos de classe
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



