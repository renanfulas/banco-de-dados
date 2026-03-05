class Clientes:
    def __init__(self, nome, email, telefone, saldo=0):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.saldo = saldo

    def exibir_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Email: {self.email}")
        print(f"Telefone: {self.telefone}")
        print(f"Saldo: R${self.saldo}")

    def atualizar_saldo(self, novo_saldo):
        self.saldo = novo_saldo