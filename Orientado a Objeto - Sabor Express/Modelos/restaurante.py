class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self.categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do restaurante'.ljust(20)} | {'Categoria'.ljust(20)} | {'Status'.ljust(20)}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(20)} | {restaurante._categoria.ljust(20)} | {restaurante.ativo}')
            
    @property
    def ativo(self):
        return '☒' if self._ativo else '☐'
    
    def altenar_estado(self):
        self._ativo = not self._ativo

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_praca.altenar_estado()
restaurante_pizza = Restaurante('pizza Express', 'Italiana')

Restaurante.listar_restaurantes()