from src.uppgift2.event import Event
from src.uppgift2.member_service import MemberService

# integrationstest, medlem finns redan
def test_register_new_member__member_exists():
    # arrange
    event = Event("Utflykt")
    member_service = MemberService()
    member1 = "Stina"
    event.register_new_member(member1, member_service)

    assert member1 in event.members_on_event
    assert member1 in member_service.member_list


# integrationstest, medlem finns inte
def test_register_new_member__member_does_not_exists():
    # arrange
    event = Event("Utflykt")
    member_service = MemberService()
    member1 = "Stina"
    event.register_new_member(member1, member_service)

    assert member1 in event.members_on_event
    assert member1 in member_service.member_list