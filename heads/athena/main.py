from fastapi import FastAPI, HTTPException, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware
import os
import secrets

app = FastAPI()

app.mount("/static", StaticFiles(directory="heads/athena"), name="static")

@app.get("/")
def read_index():
    # ⚡ Bolt: Offloading synchronous endpoint to a thread pool to prevent blocking the main event loop
    return FileResponse('heads/athena/athena.html')

origins = [
    "http://127.0.0.1:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def add_security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains"
    return response

class AnalysisInput(BaseModel):
    name: Optional[str] = None
    phone: Optional[str] = None
    social: Optional[str] = None
    dating_profile: Optional[str] = None

class VerifyAdminRequest(BaseModel):
    code: str

class AthenaAnalyzer:
    # Mock database of online profiles with richer background info.
    mock_profiles = {
        "john doe": {
            "status": "verified",
            "verified_on": ["LinkedIn", "Twitter"],
            "background_summary": "Public profiles on LinkedIn and Twitter show a consistent work history. No public posts containing aggressive language or concerning affiliations were found."
        },
        "jane smith": {
            "status": "partially_verified",
            "verified_on": ["Facebook"],
            "background_summary": "A single public profile was found on Facebook. The profile is new with limited activity, making a comprehensive background assessment difficult."
        },
    }

    def __init__(self, analysis_input: AnalysisInput):
        self.input = analysis_input
        self.search_name = self.input.name.lower() if self.input.name else None

    def verify_identity(self):
        """
        **Placeholder Implementation**
        This function simulates identity verification by checking against a mock database.
        """
        print("Step 1: Verifying identity...")
        if not self.search_name:
            return {"status": "unverified", "message": "A name is required for identity verification."}

        profile = self.mock_profiles.get(self.search_name)
        if profile:
            message = f"Identity {profile['status']} for {self.input.name}. Found profiles on: {', '.join(profile['verified_on'])}."
            return {"status": profile['status'], "message": message}

        message = f"Could not verify identity for {self.input.name}. No public profiles found."
        return {"status": "unverified", "message": message}

    def gather_background_info(self):
        """
        **Placeholder Implementation**
        This function simulates background info gathering by checking against a mock database.
        """
        print("Step 2: Gathering background information...")
        profile = self.mock_profiles.get(self.search_name)
        if profile:
            return {"background_info": profile["background_summary"]}

        # This case should ideally not be hit if verification runs first.
        return {"background_info": "No background information could be gathered."}

    def analyze_risk(self, background_info):
        """
        **Placeholder Implementation**
        This function is a placeholder for the risk analysis and safety score generation.
        A full implementation would involve:
        - Integrating with the 'Aegis' head to use its LLM capabilities.
        - Creating a sophisticated prompt that instructs the LLM to analyze the gathered information for specific red flags related to safety and coercion, while adhering to the Ethical Charter.
        - Developing a scoring algorithm that translates the LLM's analysis into a clear, probabilistic safety score.
        - Generating a concise, non-alarming summary of the findings.
        """
        print("Step 3: Analyzing risk...")
        print("Risk analysis complete (placeholder).")
        return {
            "safety_score": "Review Recommended",
            "summary": "This is a placeholder risk analysis. A full implementation would use an LLM to analyze the gathered information for potential red flags."
        }

@app.post("/analyze")
def analyze(analysis_input: AnalysisInput):
    """
    Runs the full safety analysis pipeline.

    Data Ephemerality: All data is processed in-memory for the duration of this
    request and is not stored or logged. This adheres to the Cerberus
    Ethical Charter's principle of data ephemerality.
    """
    analyzer = AthenaAnalyzer(analysis_input)

    # Step 1: Identity Verification
    identity_result = analyzer.verify_identity()
    if identity_result["status"] == "unverified":
        return {
            "safety_score": "Verification Failed",
            "summary": identity_result["message"]
        }

    # Step 2: Background Information Gathering
    background_info = analyzer.gather_background_info()

    # Step 3: Risk Analysis & Safety Score
    risk_analysis_result = analyzer.analyze_risk(background_info["background_info"])

    # Combine the verification and background info for the final summary
    risk_analysis_result["summary"] = f"{identity_result['message']} {background_info['background_info']}"

    return risk_analysis_result

@app.post("/api/verify-admin")
def verify_admin(request: VerifyAdminRequest):
    expected_code = os.environ.get("ADMIN_CODE")
    if not expected_code:
        raise HTTPException(status_code=500, detail="Server configuration error")
    if secrets.compare_digest(request.code, expected_code):
        return {"success": True}
    raise HTTPException(status_code=401, detail="Invalid admin code")
