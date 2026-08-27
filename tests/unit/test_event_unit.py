import pytest
# behöver inte importera det som används via fixtures

# sign_up - Lägger till en medlem på arrangemanget
@pytest.mark.unit
def test_sign_up(event, member1):
    # arrange - se fixtures
    # act
    event.sign_up(member1)
    # assert
    assert member1 in event.members_on_event