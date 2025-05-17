# 1 - Crie uma lista para cada informação a seguir:

# Lista de números de 1 a 10;
# Lista com quatro nomes;
# Lista com o ano que você nasceu e o ano atual.

lista_de_numeros = [1,2,3,4,5,6,7,8,9,10]
lista_de_nomes = ['Anderson','Lucineide', 'Adailton', 'Liz Anielly', 'Alisson']
lista_de_anos = [2000,2025]


# 2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.

for listar_numeros in lista_de_numeros:
    print(listar_numeros)


# 3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.

calcular_impares = 0
for i in range(1,11,2):
    calcular_impares += i
print(calcular_impares)


# 4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.

for ordem_decresente in range(10,0,-1):
    print(ordem_decresente)


# 5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.

numero_tabuada = int(input('Digite um numero para gerar uma tabuada: '))
for i in range(1,11):
    resultado_tabuada = numero_tabuada * i
    print(f'{numero_tabuada} x {i} = {resultado_tabuada}')


6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.

lista_de_numeros = [1,2,3,4,5,6,7,8,9,10]
calcular_numeros = 0
try:
    for i in lista_de_numeros:
        calcular_numeros += i
    print(f'O resultado do calculo dos numeros: {lista_de_numeros} é = {calcular_numeros}')
except Exception as e:
    print(f'Ocorreu um erro {e}')

7 - Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.

lista_de_numeros = ['a']
soma_valores = 0

try:
    for valor in lista_de_numeros:
        soma_valores += valor 
    media = soma_valores / len(lista_de_numeros)
    print(media)

except ZeroDivisionError:
    print("A lista está vazia, não é possível calcular a média.")

except Exception as e:
    print(f"Ocorreu um erro: {e}")