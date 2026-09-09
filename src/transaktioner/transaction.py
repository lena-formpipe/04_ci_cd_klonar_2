from src.transaktioner.bank_account import BankAccount


class Transaction:
    # Transaction har ingen __init__ för att inget sparas
    # OM vi vill spara något över tid så behövs en __init__
    # till exempel spara id och time_stamp
    # just nu en statisk metod
    @staticmethod
    def transfer(
            amount: float, from_account: BankAccount, to_account: BankAccount
    ):
        # Överför pengar från ett konto till ett annat,
        # med hjälp av (bank_account) deposit och withdraw,
        # om metoden returnerar True. Får varning om jag skriver ut == True
        if from_account.withdraw(amount):
            to_account.deposit(amount)
