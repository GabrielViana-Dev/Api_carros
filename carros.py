class Carros():

    id = 1

    def __init__(self,marca,ano,status='DISPONIVEL'):
        self.id = Carros.id
        self.marca = marca
        self.ano = ano
        self.status = status
        Carros.id +=1

    def carro_vendido(self):
        self.status = 'VENDIDO'

    def carro_negociando(self):
        self.status = 'NEGOCIANDO'