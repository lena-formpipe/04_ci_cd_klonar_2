import pytest


@pytest.mark.integration
# integrationstest: testar interaktionen BankAccount --> Logger
# BankAccount skapas med en riktig Logger
# verifierar att BankAccount faktiskt använder Logger.log
def test_bank_account_deposit(mocker, bank_account1, logger):
    # arrange
    amount1 = 100
    spy = mocker.spy(logger, 'log')
    # act
    bank_account1.deposit(amount1)

    assert bank_account1._balance == amount1
    assert "Deposit:" in logger._entries[-1]
    spy.assert_called_once()


@pytest.mark.integration
# integrationstest: testar interaktionen
# Transaction, BankAccount <-> BankAccount, Logger
# verifierar också Logger
def test_transaction_transfer__not_transfer(
        mocker, bank_account1, bank_account2, logger, transaction
):
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


@pytest.mark.integration
# integrationstest
# testar transaction, bank account, logger
# lägger till en rad för att se att det går pusha till main
def test_transaction_transfer__is_transferred(
        mocker, logger, transaction, bank_account1, bank_account2
):
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
