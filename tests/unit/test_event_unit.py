from src.uppgift2.event import Event

# sign_up
# Lägger till en medlem på arrangemanget
def test_sign_up():
    # arrange
    # skapa objekt Event och en member
    event = Event("Utflykt")
    member1 = "Stina"
    # act
    event.sign_up(member1)
    assert member1 in event.members_on_event