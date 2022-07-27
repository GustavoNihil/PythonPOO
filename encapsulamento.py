

class BaseDeDados:
    def __init__(self):
        self.__dados = {}

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})

    def lista_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)

    def apaga_cliente(self, id):
        del self.__dados['clientes'][id]

bd = BaseDeDados()
#print(bd.__dados)
bd.inserir_cliente(123, 'Gustavo')
#print(bd.__dados)
bd.inserir_cliente(597, 'Gabriel')
#print(bd.__dados) # com "__" no início do atributo ou método não é possível printá-la ou alterá-la
print(bd._BaseDeDados__dados) #somente assim é possível printá-la
bd.lista_clientes()
bd.apaga_cliente(597)
bd.lista_clientes()

