class Cliente:

    def __init__(self, nome:str, cpf:str):
        self.nome = nome
        self.cpf = cpf

        self.contas = []

    def adicionar_contas(self, conta):
        self.contas.append(conta)

    def __str__(self):
        return f"Cliente: {self.nome} (CPF: {self.cpf})"