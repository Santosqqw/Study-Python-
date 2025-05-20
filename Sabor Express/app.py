import os
restaurantes = [{'nome' : 'Praça', 'categoria' : 'Japonesa', 'ativo' : False},{'nome' : 'Pizza Suprema', 'categoria' : 'Pizza', 'ativo' : True}, {'nome' : 'Cantina', 'categoria' : 'Italiano', 'ativo' : False}]

def exibir_nome_programa():
    print('Sabor Express\n')

def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*' * (len(texto) + 1)
    print(linha)
    print(texto)
    print(linha)
    print()

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alternar estado restaurante')
    print('4. Sair\n')

def finalizar_app():
   exibir_subtitulo('Finalizando app')

def opcao_invalida():
    print('Opção Inválida!!\n')
    menu_principal()

def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastros de novos restaurante')
    nome_do_restarante = input('Digite o nome do restaurante a ser cadastrado: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restarante}: ')
    dados_do_restaurante = {'nome': nome_do_restarante, 'categoria': categoria, 'ativo': False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restarante} foi cadastrado com sucesso!!')
    menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Lista de restaurantes cadastrados')
    quantidade_de_cadastros = len(restaurantes)
    print(f'Atualmente temos {quantidade_de_cadastros} cadastrados em nosso sistema\n')

    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | {'Status'}')    
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        ativo_restaurante = 'Ativado' if  restaurante['ativo'] else 'Desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria_restaurante.ljust(20)} | {ativo_restaurante}')
    
    menu_principal()

def menu_principal():
    input('\nDigite alguma tecla para voltar ao menu principal ')
    main()

def alternar_estado_restaurante():
    exibir_subtitulo('Alternando estado restaurante')
    nome_restaurante = input('Digite o nome do resturante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativo com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')



    menu_principal()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        
        match opcao_escolhida:
            case 1:
                cadastrar_novo_restaurante()
            case 2:
                listar_restaurantes()
            case 3:
                alternar_estado_restaurante()
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