#1 - Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o número é par ou ímpar.
numero = int(input('Escolha um número: '))
resto = numero % 2

# if resto == 0:
#     print('O valor digitado é par')
# else:
#     print('O valor digitado é impar')

match resto:
    case 0:
        print('O valor digitado é par \n')
    case 1:
        print('O valor digitado é impar \n')

# 2 - Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar a idade em categorias de acordo com as seguintes condições:
# Criança: 0 a 12 anos;
# Adolescente: 13 a 18 anos;
# Adulto: acima de 18 anos.

idade = int(input('Digite sua idade: '))
if idade <= 12:
    print('Criança: 0 a 12 anos\n')
elif idade >= 13 or idade <= 18:
    print('Adolecente: 13 a 18 anos\n')
else:
    print('Adulto: acima de 18 anos\n')

# 3 - Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você.

usuario_padrao = 'Anderson'
senha_padrao = 1234

usuario = input('Digite seu usuario: ')
senha = int(input('Digite sua senha: '))

if usuario != usuario_padrao and senha != senha_padrao:
    print('Usuario ou senha invalido')
elif usuario == usuario_padrao and senha != senha_padrao:
    print('Senha invalida')
elif usuario != usuario_padrao and senha == senha_padrao:
    print('Usuario invalido')
else:
    print('Usuario e senha corretas')

# 4 - Solicite ao usuário as coordenadas (x, y) de um ponto qualquer e utilize uma estrutura if elif else para determinar em qual quadrante do plano cartesiano o ponto se encontra de acordo com as seguintes condições:

x = float(input('Digite o valor da coordenada X: '))
y = float(input('Digite o valor da coordenada Y: '))

if x > 0 and y > 0:
    print('Os valores digitados sao referente ao Primeiro Quadrante')
elif x < 0 and y > 0:
    print('Os valores digitados sao referente ao Segundo Quadrante')
elif x < 0 and y < 0:
    print('Os valores digitados sao referente ao Terceiro Quadrante')
else:
    print('Os valores digitados sao referente ao Quarto Quadrante')

