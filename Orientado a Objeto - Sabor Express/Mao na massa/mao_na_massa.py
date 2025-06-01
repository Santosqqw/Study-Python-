# class Musica:
#     nome = ''
#     artista = ''
#     duracao = int

# musica1 = Musica()
# musica1.nome = 'Amiga da minha mulher'
# musica1.artista = 'Seu Jorge'
# musica1.duracao = 255

# print(f'Música: {musica1.nome} - banda: {musica1.artista} - Duração: {musica1.duracao} segundos')

# 
print(70*'-')
# 

class Musica:
    def __init__(self, nome, artista, duracao ):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao

    def __str__(self):
        return f'{self.nome} | {self.artista} | {self.duracao}'

musica1 = Musica('Amiga da minha mulher', 'Seu Jorge', 255)
musica2 = Musica('A flor e o beija-flor', 'Herique e Juliano & Marilia Mendonça', 255 )

print(musica1)
print(musica2)
