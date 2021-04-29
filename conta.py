class Conta:

    CODIGO_BANCO = "001"
    CODIGOS_BANCOS = {'BB': '001', 'Caixa': '104', 'Bradesco':'237'}

    def __init__(self, numero, titular, saldo, limite = 1000.0):
        print("Construindo objeto...")
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
    
    def extrato(self):
        print("Saldo {} do titular {}".format(self.saldo, self.titular))
    
    def deposita(self, valor):
        self.saldo += valor
    
    def saca(self, valor):
        if (self.pode_sacar(valor)):
            self.saldo -= valor
        else:
            print("O valor {} passou o limite".format(valor))

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)
    
    def __pode_sacar(self, valor):
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor <= valor_disponivel_a_sacar

    @property
    def saldo(self):    
        return self.__saldo
    
    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite
    
    @limite.setter
    def limite(self, limite):
        self.__limite = limite