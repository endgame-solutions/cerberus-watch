import sys
import types
from unittest.mock import MagicMock

class MockFastAPIModule(types.ModuleType):
    def __init__(self, name):
        super().__init__(name)
        self.FastAPI = MagicMock()
        self.HTTPException = MagicMock()

class MockPydanticModule(types.ModuleType):
    def __init__(self, name):
        super().__init__(name)
        self.BaseModel = MagicMock()
        def mock_field(**kwargs):
            return kwargs.get('default', None)
        self.Field = mock_field

class MockFastAPIStaticFilesModule(types.ModuleType):
    def __init__(self, name):
        super().__init__(name)
        self.StaticFiles = MagicMock()

class MockFastAPIResponsesModule(types.ModuleType):
    def __init__(self, name):
        super().__init__(name)
        self.FileResponse = MagicMock()

class MockFastAPICORSModule(types.ModuleType):
    def __init__(self, name):
        super().__init__(name)
        self.CORSMiddleware = MagicMock()

class MockFastAPITestClientModule(types.ModuleType):
    def __init__(self, name):
        super().__init__(name)
        self.TestClient = MagicMock()

# Inject mocks
sys.modules['fastapi'] = MockFastAPIModule('fastapi')
sys.modules['pydantic'] = MockPydanticModule('pydantic')
sys.modules['fastapi.staticfiles'] = MockFastAPIStaticFilesModule('fastapi.staticfiles')
sys.modules['fastapi.responses'] = MockFastAPIResponsesModule('fastapi.responses')
sys.modules['fastapi.middleware.cors'] = MockFastAPICORSModule('fastapi.middleware.cors')
sys.modules['fastapi.middleware'] = MagicMock()
sys.modules['fastapi.testclient'] = MockFastAPITestClientModule('fastapi.testclient')
