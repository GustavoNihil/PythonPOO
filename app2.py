#classe é o agrupamento por similaridade (de características e funções), já o objeto é a instância que recebe os atributos da classe - havendo, portanto distinção entre objetos de uma mesma classe
# variáveis privadas são definidas com "__" no inicio (ex: "__preço_fabricacao")

class Computador:
    def __init__(self, marca, memoria_ram, placa_de_video):
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.placa_de_video = placa_de_video

    def ligar(self):
        print('ligando')

    def desligar(self):
        print('desligando')

    def informacoes(self):
        print(self.marca, self.memoria_ram, self.placa_de_video)

computador1 = Computador('VrummVruuumVeloz', '8gb', 'GTX87634k')
computador1.ligar()
computador1.desligar()
computador1.informacoes()


class ControleRemoto:
    def passar_canal(self, botao):
        if botao == '+':
            print('Valor selecionado: "{}".Aumentando o canal'.format(botao))
        elif botao == '-':
            print('Valor selecionado: "{}".Diminuindo canal'.format(botao))
        else:
            print('Botão inválido: "{}". Tente novamente inserindo outro valor'.format(botao))

controle_remoto1 = ControleRemoto()
# atributos não possuem "()" no final, já métodos e atribuição de classe sim

controle_remoto1.passar_canal('+')
controle_remoto1.passar_canal('-')
controle_remoto1.passar_canal('88')

# se eu defino uma variável em um "def" sem o uso do "self" ela é aceita somente dentro daquela "def". Porém, ao definir uma
#variável usando "self" (ex: "self.lista_planos = ["basic", "premium"]") a atribuição é feita ao objeto, portanto é possível acessar uma variável definida em uma "def" em outra "def"

class Cliente:
    def __init__(self, nome, email, plano):
        self.nome = nome
        self.email = email
        self.lista_planos = ['basic', 'premium']
        if plano in self.lista_planos:
            self.plano = plano
        else:
            raise Exception('Plano inválido') #tratamento de erros

    def mudar_plano(self, novo_plano):
        if novo_plano in self.lista_planos:
            self.plano = novo_plano
            print('Novo plano "{}" cadastrado com sucesso'.format(self.plano))
        else:
            print('Plano inválido')

cliente69 = Cliente('Jorge', 'jorge@gmail.com', 'basic')

print(cliente69.plano)
cliente69.mudar_plano('premium')
print(cliente69.plano)

cliente69.mudar_plano('padeiro')
print(cliente69.plano)
