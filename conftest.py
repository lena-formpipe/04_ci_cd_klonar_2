import pytest

from src.transaktioner.bank_account import BankAccount
from src.transaktioner.logger import Logger
from src.transaktioner.transaction import Transaction


@pytest.fixture
def bank_account1(logger):
    bank_account1 = BankAccount("Kalles konto", logger)
    return bank_account1


@pytest.fixture
def bank_account2(logger):
    bank_account2 = BankAccount("Annas konto", logger)
    return bank_account2


@pytest.fixture()
def logger():
    logger = Logger()
    return logger


@pytest.fixture()
def transaction():
    transaction = Transaction()
    return transaction
