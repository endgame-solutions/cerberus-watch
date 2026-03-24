## 2024-03-12 - [Reflected XSS in API Responses via innerHTML]
**Vulnerability:** The frontend code in `heads/athena/athena.html` used `innerHTML` to directly render user-controlled data (`name`, `safety_score`, `summary`) returned by the `/analyze` API. This allows an attacker to execute arbitrary JavaScript if they can manipulate the API response or reflect malicious payload via user inputs.
**Learning:** Even if data comes from an internal API response, it can be unsafe if that API reflects user input back into the payload without proper sanitization.
**Prevention:** Never use `innerHTML` to render dynamic data, especially data originating from user inputs or API responses. Use `textContent` or DOM manipulation functions (e.g., `document.createElement`, `node.appendChild`) to ensure the browser treats the input as data rather than executable code.

## 2024-05-24 - [Hardcoded Admin Secret & Timing Attack Risk]
**Vulnerability:** The backend code in `heads/athena/main.py` hardcoded the admin verification secret (`"cerberus123"`) in plaintext. Additionally, the comparison `request.code == "cerberus123"` was vulnerable to timing attacks, potentially allowing an attacker to guess the secret character by character by measuring the response time.
**Learning:** Hardcoding secrets inside source code is a major security vulnerability as it exposes them to anyone with repository access. Standard string comparisons short-circuit and leak timing information based on how many characters match.
**Prevention:** Store secrets externally in environment variables (e.g., `os.environ.get("ADMIN_CODE")`) or secure vaults. Fail securely if configurations are missing (e.g., return a 500 error). Use constant-time comparison functions like `secrets.compare_digest()` to compare security-sensitive values.
## 2024-05-24 - Missing Security Headers in FastAPI
**Vulnerability:** The FastAPI application lacked standard security headers like `X-Content-Type-Options`, `X-Frame-Options`, and `Strict-Transport-Security`.
**Learning:** This repo lacked a global middleware to enforce these security headers which opens it up to Clickjacking, MIME type sniffing, and potential downgrade attacks. The security convention in memory actually specified that this middleware *should* exist, meaning it was a gap.
**Prevention:** Ensure standard HTTP security headers are enforced globally via middleware in FastAPI apps.

## 2026-03-24 - [Pydantic Unbounded Payload DoS Risk]
**Vulnerability:** The FastAPI endpoints accepted Pydantic models ('AnalysisInput', 'VerifyAdminRequest') where string fields lacked `max_length` constraints. This could allow an attacker to send massive payloads, leading to resource exhaustion and Denial of Service (DoS) attacks.
**Learning:** Default Pydantic string fields do not enforce length limits, meaning a malicious client can upload megabytes of text into a single field, potentially overwhelming memory and CPU during parsing and validation.
**Prevention:** Always use `pydantic.Field(max_length=...)` on all string inputs in API request models to enforce strict bounds and prevent unbounded payload DoS.
