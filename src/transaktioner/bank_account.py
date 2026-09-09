from src.transaktioner.logger import Logger


class BankAccount:
    def __init__(self, customer_name: str, logger: Logger, balance=0):
        self._name = customer_name
        self._balance = balance
        self._logger = logger

    def deposit(self, amount: float):
        if amount <= 0:
            self._logger.log(f"Deposit: {amount} måste vara större än 0.")
        elif amount > 0:
            self._balance += amount
            # uppgiften: logger ska skriva "deposit: X kr, saldo X kr"
            self._logger.log(
                f"Deposit: {amount} kr, saldo efter {self._balance} kr."
            )

    def withdraw(self, amount: float):
        # gör uttag om pengar finns
        if self._balance >= amount:
            self._balance -= amount
            self._logger.log(
                f"Withdraw: {amount} kr, saldo uttag {self._balance} kr."
            )
            return True
        # enbart loggning om pengar inte finns
        else:
            self._logger.log(
                f"Withdraw: kunde inte ta ut {amount} kr från kontot."
            )
            return False
