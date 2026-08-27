from src.uppgift2.member_service import MemberService

def test_add_member(mocker):
    # arrange
    # skapa objekt MemberService och en member
    # skapa en spion till metoden add_member
    member_service_object = MemberService()
    member1 = "Stina"
    spy = mocker.spy(member_service_object, "add_member")
    # act
    member_service_object.add_member(member1)

    assert spy.call_count == 1
    assert member1 in member_service_object.member_list
