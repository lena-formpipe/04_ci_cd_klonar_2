# ●	MemberService - hanterar medlemskap till en förening
class MemberService:
    def __init__(self):
        self.member_list = []

    # skapa UNIT TEST spionera på denna
    def add_member(self, member_name):
        self.member_list.append(member_name)