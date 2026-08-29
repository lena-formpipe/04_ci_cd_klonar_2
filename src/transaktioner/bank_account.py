from src.transaktioner.logger import Logger

# Dependency Injection: BankAccount tar emot en logger istället för att skapa en egen
# På så sätt kan vi få alla bankkonton loggade i samma logger.
# om inget belopp skickas med är default 0 kr i balans när konto skapas.
class BankAccount:
    def __init__(self, customer_name:str, logger:Logger, balance= 0,  ):
        self._name = customer_name
        self._balance = balance
        self._logger = logger


    def deposit(self, amount:float):
        if amount <= 0:
            self._logger.log(f"Deposit: {amount} måste vara större än 0.")
        elif amount >0:
            self._balance += amount
            # uppgiften: logger ska skriva "deposit: X kr, saldo X kr"
            self._logger.log(f"Deposit: {amount} kr, saldo efter deposit {self._balance} kr.")


    def withdraw(self, amount:float ):
        # gör uttag om pengar finns
        if self._balance >= amount:
            self._balance -= amount
            self._logger.log(f"Withdraw: {amount} kr, saldo efter uttag {self._balance} kr.")
            return True
        # enbart loggning om pengar inte finns
        else:
            self._logger.log(f"Withdraw: kunde inte ta ut {amount} kr från kontot.")
            return False
