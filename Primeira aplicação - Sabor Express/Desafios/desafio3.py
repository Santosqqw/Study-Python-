# # 1 - Crie uma lista para cada informação a seguir:
# # Lista de números de 1 a 10;
# # Lista com quatro nomes;
# # Lista com o ano que você nasceu e o ano atual.

# lista_numero = [1,2,3,4,5,6,7,8,9,10]
# lista_nomes = ['Lucas', 'Anderson', 'Lucineide', 'Alisson']
# lista_ano = [2000, 2025]


# # 2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.

# for i in lista_nomes:
#     print(i)


# # 3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.
# soma = 0
# for i in range(1,11,2):
#     soma += i
#     print(i)
# print(soma)

# # 4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.

# for i in range(10,0,-1):
#     print(i)


# # 5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.
# numero = int(input('Digite um valor: '))
# for i in range(1,11):
#     resultado = numero * i
#     print(f'{numero} X {i} = {resultado}')


# # 6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.

# lista_numeros = [1,2,3,4,5,6,7,8,9,10,'a']
# try:
#     for i in lista_numeros:
#         soma_lista = sum(lista_numeros)
#     print(soma_lista)
# except Exception as e:
#         print(f'Valor inserido inválido.{e}')

# 7 - Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.

lista_numeros = []
soma = 0
try:
    for i in lista_numeros:
        soma = sum(lista_numeros)
    media = soma/len(lista_numeros)
    print(media)
except ZeroDivisionError as e:
    print(f'A lista está vazia, não é possível calcular a média.')
except Exception as e:
    print(f'Ocorreu um erro: {e}')