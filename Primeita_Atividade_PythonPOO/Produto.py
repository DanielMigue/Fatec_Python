
class Produto:
    def __init__(self,nome,preco,estoque):
        self.nome=nome
        self.preco=preco
        self.estoque=estoque

    def informacoes(self):
        print(f'''

█ █▄░█ █▀▀ █▀█ █▀█ █▀▄▀█ ▄▀█ █▀▀ █▀█ █▀▀ █▀   █▀▄ █▀█   █▀█ █▀█ █▀█ █▀▄ █░█ ▀█▀ █▀█
█ █░▀█ █▀░ █▄█ █▀▄ █░▀░█ █▀█ █▄▄ █▄█ ██▄ ▄█   █▄▀ █▄█   █▀▀ █▀▄ █▄█ █▄▀ █▄█ ░█░ █▄█
              
        Nome :{self.nome}
        Preço:{self.preco}
        Estoque:{self.estoque}           

''')    
    
    def vender(self,venda):
        
        self.estoque -= venda
        print(f'Foi vendido {venda} produos, restando {self.estoque} disponíveis no estoque')

class ProdutoImportado(Produto):
    def __init__(self,nome,preco,estoque,pais):
        self.nome=nome
        self.preco=preco
        self.estoque=estoque
        self.pais=pais
    
    def informacoes(self):
        print(f'''

█ █▄░█ █▀▀ █▀█ █▀█ █▀▄▀█ ▄▀█ █▀▀ █▀█ █▀▀ █▀   █▀▄ █▀█   █▀█ █▀█ █▀█ █▀▄ █░█ ▀█▀ █▀█
█ █░▀█ █▀░ █▄█ █▀▄ █░▀░█ █▀█ █▄▄ █▄█ ██▄ ▄█   █▄▀ █▄█   █▀▀ █▀▄ █▄█ █▄▀ █▄█ ░█░ █▄█
              
        Nome :{self.nome}
        Preço:{self.preco}
        Estoque:{self.estoque}  
        País de origem:{self.pais}         

''')  




    