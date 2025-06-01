class ContaBancaria:
    def __init__(self, titular = '', saldo = 0):
        self.titular = titular
        self.saldo = saldo
        self._ativo = False
    
    def __str__(self):
        return f'Titular: {self.titular.ljust(15)} | Saldo: R${self.saldo}'
    
    def ativar_conta(cls, conta):
        conta._ativo = True

    
conta1 = ContaBancaria('Anderson', 1000)
conta2 = ContaBancaria('Alisson', 5000)
print(conta1)
print(conta2)