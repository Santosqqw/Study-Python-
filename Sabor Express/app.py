import os
restaurantes = ['Pizza', 'Sushi']

def exibir_nome_programa():
    print('Sabor Express\n')

def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)
    print()

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def finalizar_app():
   exibir_subtitulo('Finalizando app\n')

def opcao_invalida():
    print('Opção Inválida!!\n')
    menu_principal()

def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastros de novos restaurante')
    nome_do_restarante = input('Digite o nome do restaurante a ser cadastrado: ')
    restaurantes.append(nome_do_restarante)
    print(f'O restaurante {nome_do_restarante} foi cadastrado com sucesso!!')
    menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Lista de restaurantes cadastrados')
    quantidade_de_cadastros = len(restaurantes)
    print(f'Atualmente temos {quantidade_de_cadastros} cadastrados em nosso sistema\n')
    
    for restaurante in restaurantes:
        print(f'.{restaurante}')
    
    menu_principal()

def menu_principal():
    input('\nDigite alguma tecla para voltar ao menu principal ')
    main()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        
        match opcao_escolhida:
            case 1:
                cadastrar_novo_restaurante()
            case 2:
                listar_restaurantes()
            case 3:
                print('ativar_restaurante')
            case 4:
                finalizar_app()
            case _:
                opcao_invalida()
    except:
        opcao_invalida()            

def main():
    os.system('cls')
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
   main()