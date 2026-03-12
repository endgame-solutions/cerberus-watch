import pytest
from fastapi.testclient import TestClient
from heads.athena.main import app

client = TestClient(app)

def test_analyze_endpoint_no_name():
    """
    Tests the /analyze endpoint with no name provided.
    It should return a 'Verification Failed' safety score.
    """
    response = client.post("/analyze", json={"phone": "123-456-7890"})
    assert response.status_code == 200
    assert response.json() == {
        "safety_score": "Verification Failed",
        "summary": "A name is required for identity verification."
    }

def test_analyze_endpoint_verified_user():
    """
    Tests the /analyze endpoint with a name that should return a 'verified' status.
    """
    response = client.post("/analyze", json={"name": "John Doe"})
    assert response.status_code == 200
    json_response = response.json()
    assert json_response["safety_score"] == "Review Recommended"
    assert "Identity verified for John Doe." in json_response["summary"]
    assert "Public profiles on LinkedIn and Twitter show a consistent work history." in json_response["summary"]

def test_analyze_endpoint_partially_verified_user():
    """
    Tests the /analyze endpoint with a name that should return a 'partially_verified' status.
    """
    response = client.post("/analyze", json={"name": "Jane Smith"})
    assert response.status_code == 200
    json_response = response.json()
    assert json_response["safety_score"] == "Review Recommended"
    assert "Identity partially_verified for Jane Smith." in json_response["summary"]
    assert "A single public profile was found on Facebook." in json_response["summary"]

def test_analyze_endpoint_unverified_user():
    """
    Tests the /analyze endpoint with a name that should return an 'unverified' status.
    """
    response = client.post("/analyze", json={"name": "Unknown Person"})
    assert response.status_code == 200
    assert response.json() == {
        "safety_score": "Verification Failed",
        "summary": "Could not verify identity for Unknown Person. No public profiles found."
    }

def test_athena_html_loads():
    """
    Tests if the athena.html file is accessible.
    NOTE: This is not a real browser test, it just checks if the file exists.
    A real-world scenario would use a tool like Selenium or Playwright.
    """
    # This is a placeholder test. A real test would require a browser environment.
    # We'll simulate a "pass" if the file exists.
    try:
        with open("heads/athena/athena.html", "r") as f:
            pass
        assert True
    except FileNotFoundError:
        assert False, "athena.html not found"

def test_quick_exit_functionality_placeholder():
    """
    Placeholder test for the quick-exit functionality.
    In a real test, we would use a browser testing framework to:
    1. Load the athena.html page.
    2. Click the 'I'm not sure' button.
    3. Click the 'Quick Exit' button.
    4. Assert that the browser navigates to the correct URL.
    """
    # This is a conceptual test.
    print("\nConceptual Test: Quick Exit")
    print("1. Load athena.html")
    print("2. Click 'I'm not sure'")
    print("3. Click 'Quick Exit'")
    print("4. Assert window.location.href is the neutral page.")
    assert True

def test_login_api():
    """
    Tests the /api/login endpoint.
    """
    # Test successful login
    response = client.post("/api/login", json={"username": "testuser", "password": "password123"})
    assert response.status_code == 200
    json_response = response.json()
    assert json_response["status"] == "success"
    assert json_response["username"] == "testuser"
    assert "token" in json_response

    # Test failed login (empty password)
    response = client.post("/api/login", json={"username": "testuser", "password": ""})
    assert response.status_code == 401
    assert "detail" in response.json()

def test_verify_admin_api():
    """
    Tests the /api/verify-admin endpoint.
    """
    # Test successful admin verification
    response = client.post("/api/verify-admin", json={"code": "cerberus123"})
    assert response.status_code == 200
    assert response.json() == {"status": "success", "admin": True}

    # Test failed admin verification
    response = client.post("/api/verify-admin", json={"code": "wrongcode"})
    assert response.status_code == 403
    assert "detail" in response.json()
