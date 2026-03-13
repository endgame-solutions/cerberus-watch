import sys
import os
from heads.athena.main import app, VerifyAdminRequest, verify_admin
from fastapi import HTTPException
import asyncio

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
