import sys
from unittest.mock import MagicMock

sys.modules['fastapi'] = MagicMock()
sys.modules['fastapi.testclient'] = MagicMock()
sys.modules['fastapi.staticfiles'] = MagicMock()
sys.modules['fastapi.responses'] = MagicMock()
sys.modules['fastapi.middleware.cors'] = MagicMock()
sys.modules['pydantic'] = MagicMock()

import pytest

if __name__ == '__main__':
    sys.exit(pytest.main(['heads/athena/test_athena.py']))
