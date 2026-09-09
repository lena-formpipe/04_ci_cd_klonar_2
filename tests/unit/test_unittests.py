
import pytest


# Unittest. Testar bara logger mot sig själv
@pytest.mark.unit
def test_logger__spy_logs_transaction(mocker, logger):
    spy = mocker.spy(logger, 'log')
    logger.log("Test")
    assert spy.call_count == 1
