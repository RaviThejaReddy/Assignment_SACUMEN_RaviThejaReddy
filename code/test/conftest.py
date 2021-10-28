import pytest
from mock import MagicMock


@pytest.fixture
def import_fixture():
    utils_mock_module = MagicMock()
    modules = {
    }
    return modules