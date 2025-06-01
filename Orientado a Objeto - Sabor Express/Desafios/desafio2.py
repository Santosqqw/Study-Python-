class Carro:
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
    def __str__(self):
        return f'{self.modelo} | {self.cor} | {self.ano}'
    
carro = Carro('Corolla', 'Preto', 2007)
print(carro)

print(70*f'*')

class Restaurante:
    def __init__(self, nome, categoria, classe):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        self.entrega = True
        self.classe = classe

    def __str__(self):
        return f'{self.nome} | {self.categoria} | {self.ativo} | {self.entrega} | {self.classe}'
     
restaurante = Restaurante('Seu Miguel', 'Marmitex', 'Media')
print(restaurante)
