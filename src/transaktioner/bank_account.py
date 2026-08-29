
class BankAccount:
    def __init__(self, name, balance ):
        self.id = id
        self.name = name
        self.balance = 0 # när konto skapas är det 0 kr i balans

    # TODO testa denna
    def deposit(self, amount):
        self.balance += amount
        # Logger ska skriva "deposit: X kr, saldo X kr"


    #TODO testa denna
    def withdraw(self, amount ):
        self.balance -= amount
        # Om tillräckligt med pengar finns:
        # - Logger ska skriva "withdraw: X kr, saldo X kr"
        # Annars:
        # - Logger ska skriva "withdraw: kunde inte ta ut X kr från kontot"