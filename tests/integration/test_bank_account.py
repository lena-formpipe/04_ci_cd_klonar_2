import pytest_mock as mocker

from src.transaktioner.bank_account import BankAccount
from src.transaktioner.transaction import Transaction
from src.transaktioner.logger import Logger


def test_bank_account_deposit(mocker):
    # arrange
    logger = Logger()
    amount1 = 100
    bank_account1 = BankAccount("Kalles konto", logger)
    spy = mocker.spy(logger, 'log')
    # act
    bank_account1.deposit(amount1)

    assert bank_account1._balance == amount1
    assert "Deposit:" in logger._entries[-1]
    spy.assert_called_once()


def test_transaction_transfer__cannot_transfer_amount(mocker):
    # arrange
    logger = Logger()
    transaktion = Transaction()
    spy = mocker.spy(logger, 'log')
    amount1 = 100
    amount_to_transfer = 101
    bank_account1 = BankAccount("Kalles konto", logger, amount1)
    bank_account2 = BankAccount("Annas konto", logger)
    # act
    transaktion.transfer(amount_to_transfer, bank_account1, bank_account2)
    assert bank_account1._balance == amount1
    assert bank_account2._balance == 0
    spy.assert_called_once()


def test_transaction_transfer__amount_is_transferred(mocker):
    # arrange
    logger = Logger()
    transaktion = Transaction()
    spy = mocker.spy(logger, 'log')
    amount1 = 100
    amount_to_transfer = 91
    bank_account1 = BankAccount("Kalles konto", logger, amount1)
    bank_account2 = BankAccount("Annas konto", logger)
    # act
    transaktion.transfer(amount_to_transfer, bank_account1, bank_account2)
    assert bank_account1._balance == amount1 - amount_to_transfer
    assert bank_account2._balance == amount_to_transfer
    spy.assert_called_once()

# testar logger för sig
def test_logger__spy_logs_transaction(mocker):
    logger = Logger()
    spy = mocker.spy(logger, 'log')

    logger.log("Test")
    assert spy.call_count == 1