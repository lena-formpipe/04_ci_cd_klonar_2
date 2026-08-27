import pytest
# behöver inte importera det som används via fixtures

@pytest.mark.unit
def test_add_member(mocker, member_service, member1):
    # arrange - se fixtures
    spy = mocker.spy(member_service, "add_member")
    # act
    member_service.add_member(member1)
    # assert
    assert spy.call_count == 1
    assert member1 in member_service.member_list
