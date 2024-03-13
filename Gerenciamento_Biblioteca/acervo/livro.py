class Livro:
    def __init__(self,titulo,autor,ano_de_publicacao,genero,disponivel=True):
        self._titulo=titulo.title()
        self._autor=autor.title()
        self._ano_de_publicacao=ano_de_publicacao
        self._genero=genero.title()
        self._disponivel= disponivel

    def estado_disponibilidade(self):    
        return '✅' if self._disponivel else '❌'
    
    
   


   
 


   