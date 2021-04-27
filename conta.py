class Conta:
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
        if (valor <= (self.__saldo + self.__limite)):
            self.saldo -= valor
        else:
            print("O valor {} passou o limite".format(valor))

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)
    
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