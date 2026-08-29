from src.transaktioner.logger import Logger

# Dependency Injection: BankAccount tar emot en logger istället för att skapa en egen
# På så sätt kan vi få alla bankkonton loggade i samma logger.
class BankAccount:
    def __init__(self, customer_name:str, logger:Logger, balance= 0,  ):
        self._name = customer_name
        self._balance = balance # när konto skapas är det 0 kr i balans
        self._logger = logger


    def deposit(self, amount:float):
        if amount <= 0:
            self._logger.log(f"Deposit: {amount} must higher than 0.")
        elif amount >0:
            self._balance += amount
            # uppgiften: logger ska skriva "deposit: X kr, saldo X kr"
            self._logger.log(f"Deposit: {amount}, saldo after deposit {self._balance} kr.")


    def withdraw(self, amount:float ):
        # gör uttag om pengar finns
        if self._balance >= amount:
            self._balance -= amount
            self._logger.log(f"Withdraw: {amount}, saldo after withdraw {self._balance} kr.")
            return True
        # enbart loggning om pengar inte finns
        else:
            self._logger.log(f"Withdraw: could not withdraw {amount} from account.")
            return False
