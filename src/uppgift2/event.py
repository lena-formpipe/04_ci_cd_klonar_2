"""
Event - beskriver ett arrangemang, och kan registrera nya medlemmar
:param name Medlemmens namn
:param ms MemberService
"""
class Event:
    def __init__(self):
        self.members_on_event = []

    # Registrerar en ny medlem i klubben,
    # OCH skriver upp denna på arrangemanget
    # skapa INTEGRATION TEST: anropar metod i klassen Member_service
    def register_new_member(self, name, ms):
        return


    # Lägger till en medlem på arrangemanget
    # skapa UNIT TEST
    # Strategi:
    def sign_up(self, name):
        self.members_on_event.append(name)