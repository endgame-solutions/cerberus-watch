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
            def middleware(self, *args, **kwargs):
                def decorator(func):
                    return func
                return decorator
            def add_middleware(self, *args, **kwargs):
                pass
            def post(self, *args, **kwargs):
                def decorator(func):
                    return func
                return decorator
            def add_middleware(self, *args, **kwargs):
                pass
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
        class BaseModel:
            def __init__(self, **kwargs):
                for k, v in kwargs.items():
                    setattr(self, k, v)
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

sys.modules['fastapi'] = MockFastAPIModule('fastapi')
sys.modules['pydantic'] = MockPydanticModule('pydantic')
sys.modules['fastapi.staticfiles'] = MockFastAPIStaticFilesModule('fastapi.staticfiles')
sys.modules['fastapi.responses'] = MockFastAPIResponsesModule('fastapi.responses')
sys.modules['fastapi.middleware.cors'] = MockFastAPICORSModule('fastapi.middleware.cors')
sys.modules['fastapi.middleware'] = MagicMock()

import os
import asyncio
from heads.athena.main import verify_admin, VerifyAdminRequest
from fastapi import HTTPException

async def run_tests():
    os.environ["ADMIN_CODE"] = "cerberus123"

    # Test valid code
    req = VerifyAdminRequest(code="cerberus123")
    res = await verify_admin(req)
    assert res == {"success": True}
    print("Test valid code passed")

    # Test invalid code
    req = VerifyAdminRequest(code="wrong")
    try:
        await verify_admin(req)
        assert False, "Should have raised HTTPException"
    except HTTPException as e:
        assert e.status_code == 401
        assert e.detail == "Invalid admin code"
        print("Test invalid code passed")

if __name__ == "__main__":
    asyncio.run(run_tests())
