""" Crie a classe Conta, recebendo apenas titular. O saldo inicial deve ser zero.

Implemente:

depositar(valor): aceita somente valores positivos;
sacar(valor): aceita somente valores positivos e menores ou iguais ao saldo;
ambos os métodos retornam Truequando realizam a operação e Falsequando a recusam, preservando o saldo em caso de recusa.
Crie duas contas independentes. Na primeira, deposite 50, saque 20, tente sacar 40e tente depositar -10. A segunda deve permanecer com saldo zero.

Conferência: saldo final da primeira conta 30; retornos True, True, False, False. """
class Conta:
    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            return True
        return False

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            return True
        return False
print("Conta 1:")
conta1 = Conta("Titular 1")
resultados_conta1 = []
resultados_conta1.append(conta1.depositar(50))  # True
resultados_conta1.append(conta1.sacar(20))      # True    