from acervo.biblioteca import Biblioteca
import os

def exibir_nome_do_programa():
    '''Exibe o nome do programa estilizado'''
    print(
        '''
██████╗░██╗██████╗░██╗░░░░░██╗░█████╗░████████╗███████╗░█████╗░░█████╗░
██╔══██╗██║██╔══██╗██║░░░░░██║██╔══██╗╚══██╔══╝██╔════╝██╔══██╗██╔══██╗
██████╦╝██║██████╦╝██║░░░░░██║██║░░██║░░░██║░░░█████╗░░██║░░╚═╝███████║
██╔══██╗██║██╔══██╗██║░░░░░██║██║░░██║░░░██║░░░██╔══╝░░██║░░██╗██╔══██║
██████╦╝██║██████╦╝███████╗██║╚█████╔╝░░░██║░░░███████╗╚█████╔╝██║░░██║
╚═════╝░╚═╝╚═════╝░╚══════╝╚═╝░╚════╝░░░░╚═╝░░░╚══════╝░╚════╝░╚═╝░░╚═╝'''
    )

def exibir_opcoes():
    '''Mostra as opções que o usuário devera escolher no menu principal'''
    print(
        '''
    1. Adicionar livro
    2. Adicionar usuário
    3. Emprestar livro
    4. Listar livros disponíveis
    5. Listar livros emprestados
    6. Listar usuários
    7. Sair
'''
    )

def voltar_ao_menu_principal():
    '''Pede ao usuário uma tecla para voltar ao menu principal'''
    input('\nDigite uma tecla para voltar ao menu principal: ')
    main()
  
def opcao_invalida():
    '''Exibe a mensagem inválida'''
    print('Opção inválida!\n')
    voltar_ao_menu_principal()

def escolher_opcao():
    '''Solicita ao usuário a escolha de uma das opções e executa suas respectivas funções'''
    try:
        
        biblioteca = Biblioteca()
        opcao_escolhida = input('Escolha uma opção: ')
        opcao_escolhida = int(opcao_escolhida)
     
        if opcao_escolhida == 1:
                biblioteca.adicionar_livros() #CONCLUÍDO
                voltar_ao_menu_principal()
        elif opcao_escolhida == 2:
                biblioteca.adicionar_usuario() #CONCLUIDO
                voltar_ao_menu_principal()          
        elif opcao_escolhida == 3:
                biblioteca.emprestar_livro() # CONCLUIDO
                voltar_ao_menu_principal()
        elif opcao_escolhida == 4:
                biblioteca.listar_livros_disponiveis() #EDITAR
                voltar_ao_menu_principal()
        elif opcao_escolhida == 5:
                biblioteca.listar_livros_emprestados() #FALTA FAZER
                voltar_ao_menu_principal()
        elif opcao_escolhida == 6:
                biblioteca.listar_usuarios() #CONCLUIDO
                voltar_ao_menu_principal()

        elif opcao_escolhida == 7:
                biblioteca.finalizar_app() #CONCLUIDO               
    except ValueError:
        opcao_invalida()
        
def main(): 
    '''Função principal que inicia o programa'''
    os.system('cls') #Limpa a tela
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__': 
    '''Se este arquivo for executado diretamente, a função main() será chamada.
    Isso permite que o programa seja executado como um script independente
    '''   
    main()