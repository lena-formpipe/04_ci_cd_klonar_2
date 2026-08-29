import pytest

from src.transaktioner.bank_account import BankAccount
from src.transaktioner.transaction import Transaction
from src.transaktioner.logger import Logger


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


def test_bank_account_deposit(mocker, bank_account1, logger):
    # arrange
    amount1 = 100
    spy = mocker.spy(logger, 'log')
    # act
    bank_account1.deposit(amount1)

    assert bank_account1._balance == amount1
    assert "Deposit:" in logger._entries[-1]
    spy.assert_called_once()


def test_transaction_transfer__cannot_transfer_amount(mocker, bank_account1, bank_account2, logger, transaction):
    # arrange
    spy = mocker.spy(logger, 'log')
    amount1 = 100
    amount_to_transfer = 101
    bank_account1.deposit(amount1)
    # act
    transaction.transfer(amount_to_transfer, bank_account1, bank_account2)
    assert bank_account1._balance == amount1
    assert bank_account2._balance == 0
    assert spy.call_count == 2


def test_transaction_transfer__amount_is_transferred(mocker, logger, transaction, bank_account1, bank_account2):
    # arrange
    spy = mocker.spy(logger, 'log')
    amount1 = 100
    bank_account1.deposit(amount1)
    amount_to_transfer = 91
    # act
    transaction.transfer(amount_to_transfer, bank_account1, bank_account2)
    assert bank_account1._balance == amount1 - amount_to_transfer
    assert bank_account2._balance == amount_to_transfer
    assert spy.call_count == 3

# testar logger för sig
def test_logger__spy_logs_transaction(mocker, logger):
    spy = mocker.spy(logger, 'log')
    logger.log("Test")
    assert spy.call_count == 1