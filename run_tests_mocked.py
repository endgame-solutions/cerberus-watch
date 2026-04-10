import sys
import types
from unittest.mock import MagicMock

class MockFastAPIModule(types.ModuleType):
    def __init__(self, name):
        super().__init__(name)
        class FastAPI:
            def __init__(self, *args, **kwargs):
                self.args = args
                self.kwargs = kwargs
            def mount(self, *args, **kwargs):
                pass
            def get(self, *args, **kwargs):
                def decorator(func):
                    return func
                return decorator
            def post(self, *args, **kwargs):
                def decorator(func):
                    return func
                return decorator
            def add_middleware(self, *args, **kwargs):
                pass
            def middleware(self, *args, **kwargs):
                def decorator(func):
                    return func
                return decorator
        self.FastAPI = FastAPI
        class HTTPException(Exception):
            def __init__(self, status_code, detail):
                self.status_code = status_code
                self.detail = detail
        self.HTTPException = HTTPException
        self.Request = MagicMock()

class MockPydanticModule(types.ModuleType):
    def __init__(self, name):
        super().__init__(name)
        self.BaseModel = MagicMock()

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
