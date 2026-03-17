import sys
import types
from unittest.mock import MagicMock

class MockFastAPIModule(types.ModuleType):
    def __init__(self, name):
        super().__init__(name)
        self.FastAPI = MagicMock()
        self.HTTPException = MagicMock()
        self.Request = MagicMock()

class MockPydanticModule(types.ModuleType):
    def __init__(self, name):
        super().__init__(name)
        class BaseModel:
            def __init__(self, **kwargs):
                for k, v in kwargs.items():
                    setattr(self, k, v)
                if not hasattr(self, 'name'):
                    self.name = None
        self.BaseModel = BaseModel

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
