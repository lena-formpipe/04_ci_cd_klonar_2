import pytest

from src.uppgift2.member_service import MemberService
from src.uppgift2.event import Event


@pytest.fixture
def member_service():
    return MemberService()


@pytest.fixture
def event():
    return Event("Utflykt")

@pytest.fixture
def member1():
    return "Stina"