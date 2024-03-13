from acervo.livro import Livro
from acervo.usuario import Usuario
import os

class Biblioteca:
    #ARRAYS: ARRUMAR
    livros = [] 
    usuarios = []
    emprestados = []
    def __init__(self): 
         pass

    def exibir_subtitulo(self, texto):

        '''Estiliza e exibe o subtítulo na tela
        Inputs:
        -texto: str - O texto do subtítulo
        '''

        os.system('cls')#limpa o programa
        linha = '*' * len(texto)#len = tamanho
        print(linha)
        print(texto)
        print(linha)
        print()

    def finalizar_app(self):
        '''Encerra o gerenciamento da Biblioteca com uma mensagem de finalização'''

        self.exibir_subtitulo('Você saiu do gerenciamento da Biblioteca!')
    
    def adicionar_usuario(self):

        '''Adiciona o Usuario no Array "Usuarios".'''

        os.system('cls')        
        self.exibir_subtitulo('Adicionar Usuário')

        nome_usuario = input('Digite o nome do usuário: ')
        
        id_usuario = input('Digite o id do usuário: ')

        dados_usuario = Usuario(id_usuario, nome_usuario)

        self.usuarios.append(dados_usuario)

        print(f'O usuário "{nome_usuario}" foi adicionado ao sistema biblioteca')
   
    def adicionar_livros(self):
        '''Adiciona o livro no Array "livros". '''
        os.system('cls')   

        self.exibir_subtitulo('Adicionar livros Disponiveis')
                    
        titulo_livro = input('Digite o título do livro que deseja adicionar: ')
        autor_livro = input('Digite o autor do livro: ')
        ano_publicacao = input('Digite o ano de publicação: ')
        genero = input('Digite o gênero do livro: ')
        
        novo_livro = Livro(titulo_livro,autor_livro,ano_publicacao,genero)

        self.livros.append(novo_livro)
        
        print(f'\nO livro "{titulo_livro}" foi adicionado ao acervo com sucesso!')
    
    def listar_usuarios(self):
        '''Exibe a lista de usuários estilizada'''
        os.system('cls')

        self.exibir_subtitulo('Lista de Usuários')

        print(f'{"ID:".ljust(5)} | {"Nome:"}') 

        for usuario in self.usuarios:
            print(f'{usuario._id.ljust(5)} | {usuario._nome}')
    
    def listar_livros_disponiveis(self):
        '''Exibe uma lista estilizada dos livros disponiveis na biblioteca'''        
        os.system('cls')

        self.exibir_subtitulo('Lista de Livros disponíveis')
        
        print(f'{"Título:".ljust(30)} | {"Autor:".ljust(20)} | {"Ano:".ljust(10)} | {"Genero:".ljust(10)} | {"Disponivel:"}')
        for livro in self.livros:
            
            disponivel = livro.estado_disponibilidade()
            if disponivel:         
                print(f'{livro._titulo.ljust(30)} | {livro._autor.ljust(20)} | {livro._ano_de_publicacao.ljust(10)} | {livro._genero.ljust(10)} | {disponivel}')

    def emprestar_livro(self):
        '''Empresta um livro a um usuário. Antes de emprestar,verifica se o 
        livro está disponível e se o usuário está cadastrado na biblioteca.
        Atualiza a disponibilidade do livro após emprestá-lo.

        Inputs:
        -livro_emprestado
        -nome_usuario
        '''

        os.system('cls')
        self.exibir_subtitulo('Empréstimo de Livros')

        #lista de livros
        print(f'{"Título:".ljust(30)} | {"Disponivel:"}')
        for livro in self.livros:
            disponivel = livro.estado_disponibilidade()
            
            print(f'{livro._titulo.ljust(30)} | {disponivel}')
            

        livro_emprestado = input('\nDigite o nome do livro que será emprestado: ')

        os.system('cls')
        #lista de usuários
        print('Lista de Usuários')

        print(f'{"ID:".ljust(25)} | {"Nome:"}') 
        for usuario in self.usuarios:
            print(f'{usuario._id.ljust(25)} | {usuario._nome}')
            
        nome_usuario = input('\nDigite o nome do usuário que irá receber o livro: ')

        os.system('cls')

        livro_encontrado=None
        usuario_encontrado=None

        #BUSCA DE LIVROS E USUÁRIOS:
        for livro in self.livros:#encontra o nome do livro que bata com o input pedido
            if livro._titulo == livro_emprestado:          
             livro_encontrado=livro  
             break

        for usuario in self.usuarios:#encontra o nome do usuario que bata com o input pedido
            if usuario._nome.lower() == nome_usuario.lower(): 
                usuario_encontrado=usuario           
                break 
               
        if usuario_encontrado and livro_encontrado: #verifique o encontro do livro e usuario
                        
            dados_emprestimo = (nome_usuario.title(), livro_emprestado.title()) # armazena os dados que entrarão na lista
            livro_encontrado._disponivel=False
            self.emprestados.append(dados_emprestimo) #adiciona os dados para lista emprestados

            self.exibir_subtitulo('Disponibilidade dos livros')

            print(f'O livro {livro_emprestado.title()} foi emprestado para {nome_usuario.title()} com sucesso!\n')

            print(f'{"Título:".ljust(30)} | {"Autor:".ljust(20)} | {"Ano:".ljust(10)} | {"Genero:".ljust(10)} | {"Disponivel:"}')
            for livro in self.livros: #mostra a lista de disponibilidade
                disponivel = livro.estado_disponibilidade()

                
                print(f'{livro._titulo.ljust(30)} | {livro._autor.ljust(20)} | {livro._ano_de_publicacao.ljust(10)} | {livro._genero.ljust(10)} | {disponivel}')

            self.livros.remove(livro_encontrado) #remove o livro que o usuário escolheu

        else:
         print('Usuário ou livro não cadastrados!')
            
    def listar_livros_emprestados(self):

        ''' Lista todos os livros atualmente emprestados.'''

        os.system('cls')
        
        self.exibir_subtitulo('Lista de Livros Emprestados')
        print(f'{"Título:".ljust(25)} | {"Usuário:"}')    
        for emprestimo in self.emprestados:
            (nome_usuario, livro_emprestado) = emprestimo #unpacking, desestruturação de tuplas, ela pertimite o acesso dos valores
            print(f'{livro_emprestado.ljust(25)} | {nome_usuario} ')

        

        


        


            








