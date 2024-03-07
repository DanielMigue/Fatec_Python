class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular=titular
        self.saldo=saldo
    
    def depositar(self,valor):

        self.saldo += valor
    
    def sacar(self,valor_saque):

        valor_saque -= self.saldo if self.saldo > valor_saque else print('Saldo insuficiente')
        
    def obter_saldo(self):
        print(self.saldo)

class ContaCorrente(ContaBancaria):
    def __init__(self, titular, saldo,limite_cheque_especial):
        self.titular=titular
        self.saldo=saldo
        self.limite_cheque_especial=limite_cheque_especial
    
    def usar_cheque_especial(self, valor):
        if valor > self.saldo :
            valor-=self.limite_cheque_especial
        else:
            print('Seu saldo é positvo, não precisa de cheque especial')

        
        
            
        

    
        
    

        