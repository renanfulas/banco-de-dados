class Conta:
    def __init__(self, numero_conta, saldo):
        self.numero_conta = numero_conta
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor} realizado. Novo saldo: R${self.saldo}")

    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente para saque.")
        else:
            self.saldo -= valor
            print(f"Saque de R${valor} realizado. Novo saldo: R${self.saldo}")