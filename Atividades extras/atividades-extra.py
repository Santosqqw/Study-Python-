# Calculadora de Soma Simples
# Descrição: Escreva um programa que peça dois números ao usuário e imprima a soma deles.
try:
    n1 = float(input('Digite o primeiro valor: '))
    n2 = float(input('Digite o primeiro valor: '))

except ValueError:
    print('Por favor, digite apenas numeros validos')


# Verificador de Par ou Ímpar
# Descrição: Peça um número ao usuário e informe se ele é par ou ímpar.

numero = int(input('Digite um valor: '))
resto = numero % 2
match resto:
    case 0:
        print(f'O valor {numero} é par')
    case 1:
        print(f'O valor {numero} é impar')


# Contador de 1 a 10
# Descrição: Use um loop for para imprimir todos os números de 1 a 10.

for i in range(1,11):
    print(i)


# Soma de Números em um Intervalo
# Descrição: Similar ao seu código, escreva um programa que some todos os números ímpares de 1 a 20.
soma_impares = 0
valor_maximo = int(input('Digite o valor maximo a ser comparado: '))
for i in range(1,valor_maximo + 1,2):
    soma_impares += i
print(f'A soma dos ímpares de 1 a {valor_maximo} é: {soma_impares}')


# Tabuada de um Número
# Descrição: Peça um número ao usuário e imprima a tabuada desse número (de 1 a 10).

numero = int(input('Digite um valor: '))
for i in range(1,11):
    resultado_multiplicacao = numero * i
    print(f'{numero} x {i} = {resultado_multiplicacao}')
