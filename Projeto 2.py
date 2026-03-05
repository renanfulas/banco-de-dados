# Classe exemplo, não utilizada
class Projeto2:
    pass

print('Testando o projeto para começarmos no GitHub')

from Clientes import Clientes
from Conta import Conta
from datetime import datetime
import re

# Função para buscar o último saldo salvo
def buscar_ultimo_saldo(arquivo_path):
    try:
        with open(arquivo_path, "r", encoding="utf-8") as f:
            conteudo = f.read()
            saldos = re.findall(r"Saldo do cliente: R\$(\d+\.?\d*)", conteudo)
            if saldos:
                return float(saldos[-1])
    except FileNotFoundError:
        pass
    return 1000.0  # valor padrão inicial

# Criação do cliente
cliente1 = Clientes("Renan", "renanjr@outlook.com", "111")

# Busca saldo mais recente
saldo_inicial = buscar_ultimo_saldo("saldo_cliente.txt")

# Criação da conta associada ao cliente com saldo atualizado
conta1 = Conta(12345, saldo_inicial)

# Exibindo informações do cliente
print("Informações do cliente:")
cliente1.exibir_informacoes()

# Exibindo informações da conta
print("\nInformações da conta:")
print(f"Número da conta: {conta1.numero_conta}")
print(f"Saldo: R${conta1.saldo}")

# Função do menu
def menu():
    print("\n--- Menu Bancário ---")
    print("1 - Consultar saldo")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Ver histórico")
    print("5 - Sair")
    return input("Escolha uma opção: ").strip()

# Loop principal
while True:
    opcao = menu()
    if opcao == "1":
        print(f"\nSaldo atual: R${conta1.saldo}")
    elif opcao == "2":
        while True:
            valor = input("Quanto gostaria de depositar? (apenas números): ")
            if valor.isdigit():
                valor = float(valor)
                break
            else:
                print("Por favor, digite apenas números.")
        conta1.depositar(valor)
        cliente1.atualizar_saldo(conta1.saldo)
        print(f"\nSaldo atualizado: R${conta1.saldo}")
        # Salva histórico
        ultima_atualizacao = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        with open("saldo_cliente.txt", "a", encoding="utf-8") as arquivo:
            arquivo.write(f"Nome do cliente: {cliente1.nome}\n")
            arquivo.write(f"Saldo do cliente: R${cliente1.saldo}\n")
            arquivo.write(f"Última atualização: {ultima_atualizacao}\n")
            arquivo.write("-"*30 + "\n")
    elif opcao == "3":
        while True:
            valor = input("Quanto gostaria de sacar? (apenas números): ")
            if valor.isdigit():
                valor = float(valor)
                break
            else:
                print("Por favor, digite apenas números.")
        conta1.sacar(valor)
        cliente1.atualizar_saldo(conta1.saldo)
        print(f"\nSaldo atualizado: R${conta1.saldo}")
        # Salva histórico
        ultima_atualizacao = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        with open("saldo_cliente.txt", "a", encoding="utf-8") as arquivo:
            arquivo.write(f"Nome do cliente: {cliente1.nome}\n")
            arquivo.write(f"Saldo do cliente: R${cliente1.saldo}\n")
            arquivo.write(f"Última atualização: {ultima_atualizacao}\n")
            arquivo.write("-"*30 + "\n")
    elif opcao == "4":
        try:
            with open("saldo_cliente.txt", "r", encoding="utf-8") as arquivo:
                linhas = arquivo.readlines()
                registros = [linhas[i:i+4] for i in range(0, len(linhas), 4)]
                ultimos = registros[-3:] if len(registros) >= 3 else registros
                print("\n--- Últimos registros ---")
                for reg in ultimos:
                    print("".join(reg))
        except FileNotFoundError:
            print("Nenhum histórico encontrado.")
    elif opcao == "5":
        print("Obrigado! Encerrando o programa.")
        break
    else:
        print("Opção inválida. Tente novamente.")

# Salva saldo do cliente em tempo real (histórico)
ultima_atualizacao = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
with open("saldo_cliente.txt", "a", encoding="utf-8") as arquivo:
    arquivo.write(f"Nome do cliente: {cliente1.nome}\n")
    arquivo.write(f"Saldo do cliente: R${cliente1.saldo}\n")
    arquivo.write(f"Última atualização: {ultima_atualizacao}\n")
    arquivo.write("-"*30 + "\n")