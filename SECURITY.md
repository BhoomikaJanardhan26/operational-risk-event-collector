# SECURITY.md

## Executive Summary
This document outlines the security measures, threat models, and residual risks for the Operational Risk Event Collector. The system implements defense-in-depth strategies, addressing API security, data sanitization, and rate limiting to ensure robust protection against common vulnerabilities.

---

## Threat Model and Findings

### 1. API Key Exposure
**Risk:** API keys for Groq API could be leaked in code or via public repositories.
**Mitigation:** 
- API keys are strictly managed via environment variables (`.env`).
- Added `.env` to `.gitignore` to prevent accidental commits.
- **Status:** Fixed.

### 2. Prompt Injection
**Risk:** Malicious users may input specific strings (e.g., "ignore previous instructions") to manipulate the AI's behavior and extract underlying system prompts.
**Mitigation:** 
- Input is sanitized to strip HTML and dangerous characters.
- Custom middleware `detect_prompt_injection` flags malicious phrases and rejects the request with HTTP 400.
- **Status:** Fixed.

### 3. Rate Limiting Abuse
**Risk:** An attacker could spam AI endpoints, exhausting the Groq API limits (Denial of Service).
**Mitigation:** 
- Integrated `flask-limiter` on the Flask application.
- Enforced a strict limit of 30 requests per minute per IP.
- **Status:** Fixed.

### 4. Unhandled Exceptions
**Risk:** Unexpected API failures from Groq could crash the service and return HTTP 500, causing poor user experience or data loss.
**Mitigation:** 
- All AI calls are wrapped in `try-except` blocks.
- Implemented a 3-retry fallback mechanism with exponential backoff.
- Returns a standardized JSON fallback (`is_fallback: true`) rather than crashing.
- **Status:** Fixed.

### 5. Data Leakage (PII Audit)
**Risk:** Sensitive personal data (PII) may be sent to third-party AI APIs.
**Mitigation:** 
- Data sent to the `/describe`, `/recommend`, and `/generate-report` endpoints are audited.
- Users are informed not to input PII into the risk event text.
- **Status:** Fixed.

### 6. Unauthorized Access
**Risk:** Endpoints could be accessed by unauthenticated users.
**Mitigation:** 
- JWT Authentication enforced via Spring Security on the backend.
- AI service is protected within the docker-compose network and only accessed by the Java backend service (`AiServiceClient.java`).
- **Status:** Fixed.

---

## Security Testing
- **Injection Tests:** Confirmed that HTML tags and prompt injection keywords result in HTTP 400.
- **Rate Limit Tests:** Verified that >30 req/min from a single IP results in HTTP 429 Too Many Requests.
- **OWASP ZAP:** Scanned the AI service and resolved all High/Critical findings (e.g., missing security headers handled by Java proxy).

## Residual Risks
- The free-tier Groq API may experience rate limits beyond our control, which are mitigated by fallback templates but may occasionally degrade user experience.

## Team Sign-Off
- [x] Java Developer 1
- [x] Java Developer 2
- [x] AI Developer 1
- [x] AI Developer 2