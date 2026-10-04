from abc import ABC, abstractmethod
from datetime import datetime
from dsautilitarios.exceptions import SaldoInsuficiente

class Conta(ABC):

    """
    Classe base abstrata para contas bancárias.
    Demonstra Herança e Encapsulamentos
    """

    _total_contas = 0

    def __init__(self, numero : int, cliente):
        self._numero = numero
        self._saldo = 0
        self._cliente = cliente
        self._historico = []

    @property
    def saldo(self):
        return self._saldo

    @classmethod
    def get_total_contas(cls):
        """
        Metódo de classe para obter o número total de contas criadas.
        """

        return cls._total_contas

    def depositar(self, valor : float):
        if valor > 0:
            self._saldo += valor
            self._historico.append((datetime.now(), f"Depósito de R${valor:.2f}"))
            print(f"Depósitor de R${valor:.2f} realizado com sucesso.")

        else:
            print(f"Valor de depósito inválido.")

    @abstractmethod
    def sacar(self, valor :float):
        """
        Metódo abstrato para sacar um valor. Deve ser implementado pela subclasses.
        """
        pass

    def extrato(self):
        """
        Exibe o extrato da conta
        """
        print(f"\n--- Extrato da Conta Nº {self._numero} ---")
        print(f"Cliente: {self._cliente.nome}")
        print(f"Saldo atual: {self._saldo:.2f}")
        print(f"Histórico de transações:")

        if not self._historico:
            print(f"Nenhuma transação registrada.")

        for data, transaçao in self._historico:
            print(f"- {data.strftime('%d/%m/%Y %H:%M:%S')}: {transaçao}")
        print(f"-------------------------------------------\n")

class ContaCorrente(Conta):
    """
    Subclasse que representa uma conta corrente.
    Demonstar Polimorfismo ao sobescrever o método sacar.
    """

    def __init__(self, numero : int, cliente, limite : float = 500.0):
        super().__init__(numero, cliente)
        self.limite = limite

    def sacar(self, valor : float):
        if valor <= 0:
            print(f"Valor de um saque inválido.")
            return
        saldo_disponivel = self._saldo + self.limite

        if valor > saldo_disponivel:
            raise SaldoInsuficienteError(saldo_disponivel, valor, "Saldo e limite insuficiente.")

        self._saldo -= valor
        self._historico.append((datetime.now(), f"Saque de R${valor:.2f}"))
        print(f"Saque de {valor:.2f} realizado com sucesso.")

class ContaPoupanca(Conta):
    """
    Subclasse que representa uma conta poupança.
    """

    def __init__(self, numero : int, cliente):
        super().__init__(numero, cliente)

    def sacar(self, valor : float):

        if valor <= 0:
            print(f"Valor de saque inválido")
            return
        if valor > self._saldo:
            raise SaldoInsuficienteError(self._saldo, valor)

        self._saldo -= valor
        self._historico.append((datetime.now(), f"Saque de R${valor:.2f}"))
        print(f"Saque de R${valor:.2f} realizado com sucesso.")