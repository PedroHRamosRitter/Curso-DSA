from dsaoperacoes.banco import Banco
from dsautilitarios.exceptions import SaldoInsuficiente, ContaInexistenteError
def menu_principal():
    print("""
    \n--- Mini-Projeto 2 - Sistema Bancário Digital ---
    1. Adicionar Cliente
    2. Criar Conta
    3. Acessar Conta
    4. Sair\n
    """)

    return input("Escolha uma opção: ")

def menu_conta(banco):
    try:
        num_conta = int(input(f"Digite o número da conta: "))

        conta = banco.buscar_conta(num_conta)

        while True:
            print(f"""
                \n--- Operações para Conta Nº {conta._numero} ---
                Cliente: {conta._cliente.nome} | Saldo R${conta.saldo:.2f}
                1. Depositar
                2. Sacar
                3. Ver Extrato
                4. Voltar ao Menu Principal
            """)

            opcao = input(f"Escolha uma opção")

            if opcao == '1':
                valor = float(input(f"Digite o valor para o depósito: "))
                conta.depositar(valor)

            elif opcao == '2':
                try:
                    valor = float(input(f"Digite o valor para o saque: "))
                    conta.sacar(valor)
                except SaldoInsuficiente as e:
                    print(f"Erro na operação {e}")

            elif opcao == '3':
                conta.extrato()

            elif opcao == '4':
                break
            else:
                print(f"Opção inválida. Tente novamento.")

    except ContaInexistenteError as e:
        print(f"Erro: {e}")

    except ValueError:
        print(f"Erro: Entrada inválida. Por favor, digite um número.")

def main():
    banco = Banco("Banco Digital Grêmio")

    while True:
        opcao = menu_principal()

        if opcao == '1':
            banco.adicionar_conta(str(input(f"Nome: ")), str(input(f"CPF: ")))

        elif opcao == '2':
            cpf = input("Digite o CPF do cliente para vincular a conta.")
            cliente = banco._clientes.get(cpf)

            if cliente:
                tipo = input("Digite o tipo da conta (corrente / poupanca): ")
                banco.criar_conta(cliente, tipo)
            else:
                print(f"Cliente não encontrado. Cadastre o cliente primeiro.")

        elif opcao == '3':
            menu_conta(banco)

        elif opcao == '4':
            print(f"\nObrigado por usar o nosso sitema. Até logo!\n")
            break
        else:
            print(f"\nOpção inválida. Por favor, tente novamente.")

if __name__ == '__main__':
    main()