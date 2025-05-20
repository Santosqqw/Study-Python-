pessoa = [{'nome': 'Anderson', 'idade': 24, 'genero': 'Masculino'}]
contador = [2]

for i in contador:
    pessoa_nome = input('Digite seu nome: ')
    pessoa_idade = input('Digite sua idade: ')
    pessoa_genero = input('Digite seu genero: ')
    pessoa_dados = [{'nome': pessoa_nome, 'idade': pessoa_idade, 'genero': pessoa_genero}]
    pessoa.append(pessoa_dados)
print(f'Nome: {pessoa_nome} | Idade: {pessoa_idade} | Gênero: {pessoa_genero}')

