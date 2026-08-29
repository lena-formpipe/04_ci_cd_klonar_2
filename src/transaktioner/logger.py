
class Logger:

    # skriv ut loggen och skriv även loggning till en lista att spara,
    # objektet logger är en lista med rader för transaktionerna
    def __init__(self):
        self._entries = []

    # Uppgiften är att spionera på denna log()
    def log(self, log_message: str):
        print(log_message)
        self._entries.append(log_message)
