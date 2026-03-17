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

## 2025-03-17 - [Frontend-Only Authentication Bypass]
**Vulnerability:** The login form in `assets/js/dashboard.js` verified credentials purely on the frontend (accepting any non-empty input) and then granted access to the dashboard by setting a `localStorage` flag. This is a critical security bypass as anyone could log in without valid credentials.
**Learning:** Frontend authentication checks are fundamentally insecure because the client environment can be manipulated by the user. "Demo purposes" implementations that bypass security can easily leak into production.
**Prevention:** All authentication logic must be enforced on the backend. The frontend should capture credentials, send them to a secure API endpoint (e.g., `/api/login`), and only grant access or redirect upon receiving a successful response from the server.
