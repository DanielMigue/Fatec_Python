import os
#CLASSE
os.system('cls')
 
#MÉTODO CONSTRUTOR
class Carro:
    def __init__(self, marca, modelo, ano, quilometragem):
#1º ATRIBUTOS
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.quilometragem = quilometragem

#2º MÉTODOS:        
    def informacoes(self):
        print(f'''
       
        O carro possui a marca: {self.marca}
        O modelo: {self.modelo}
        Ano:{self.ano}
        Quilometragem:{self.quilometragem}
 
''')       
    def andar(self, distancia):      
        distancia += self.quilometragem
        print(f'O carro andou de {distancia} km, sua nova quilometragem é de {self.quilometragem} km')

#3º Classe nova, com atributos
class CarroEletrico(Carro):
    def __init__(self, marca, modelo, ano, quilometragem,autonomia):
        self.marca=marca
        self.modelo=modelo
        self.ano=ano
        self.quilometragem-quilometragem
        self.autonomia=autonomia

#4º Poliformismo
    def informacoes(self):
         print(f'''       
               
        O carro possui a marca: {self.marca}
        O modelo: {self.modelo}
        Ano:{self.ano}
        Quilometragem:{self.quilometragem} 
        Autonomia:{self.autonomia}
''')       
    

            
 
#DEFININDO UMA NOVA CLASSE
    