import pytest
# behöver inte importera det som används via fixtures

# integrationstest, medlem finns redan
@pytest.mark.integration
def test_register_new_member__member_exists(member_service, event, member1):
    # arrange - se fixtures
    # act
    event.register_new_member(member1, member_service)
    # assert
    assert member1 in event.members_on_event
    assert member1 in member_service.member_list


# integrationstest, medlem finns inte
@pytest.mark.integration
def test_register_new_member__member_does_not_exists(member_service, event, member1):
    # arrange - se fixtures
    # act
    event.register_new_member(member1, member_service)
    # assert
    assert member1 in event.members_on_event
    assert member1 in member_service.member_list