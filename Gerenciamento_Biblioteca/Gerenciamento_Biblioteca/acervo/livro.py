class Livro:
    def __init__(self,titulo,autor,ano_de_publicacao,genero,disponivel=True):
        self._titulo=titulo
        self._autor=autor
        self._ano_de_publicacao=ano_de_publicacao
        self._genero=genero
        self._disponivel= disponivel

    def estado_disponibilidade(self):    
        return '✅' if self._disponivel else '❌'
    
    
   


   
 


   