from src.uppgift2.member_service import MemberService
"""
Event - beskriver ett arrangemang, och kan registrera nya medlemmar
:param name Medlemmens namn
:param ms MemberService
"""
class Event:
    def __init__(self, event_name):
        self.name = event_name
        self.members_on_event = []

    # kontrollerar om medlem existerar
    #  - om inte så registreras en ny medlem i klubben,
   # skriver sedan upp denna medlem på arrangemanget
    def register_new_member(self, member_name, ms):
        # om medlemmen inte finns - lägg till i member_service,
        if member_name not in ms.member_list:
            ms.add_member(member_name)
        if member_name in ms.member_list:
            self.sign_up(member_name)


    # Skriver upp en medlem på arrangemanget
    def sign_up(self, member_name):
        self.members_on_event.append(member_name)
