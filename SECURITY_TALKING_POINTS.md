# Security Talking Points

*Use these points to confidently discuss the security measures implemented in our application.*

## 1. Prompt Injection Protection
"One of the biggest vulnerabilities in AI systems today is prompt injection, where a user tries to trick the AI into ignoring instructions or revealing secrets. We implemented a custom middleware layer that actively scans inputs for malicious phrases like 'ignore previous instructions' and blocks them instantly with a 400 error."

## 2. Denial of Service & Rate Limiting
"To prevent an attacker from spamming the Groq API and exhausting our free-tier limits, we integrated `flask-limiter`. The system strictly limits traffic to 30 requests per minute per IP. This guarantees our service remains available."

## 3. Graceful Degradation
"Third-party APIs can go down. If the Groq API becomes unavailable, our application doesn't crash or return a 500 server error. Instead, our 3-retry backoff system attempts recovery, and if it fails, it returns a safe, structured fallback JSON indicating the service is temporarily unavailable. This ensures the frontend doesn't break."

## 4. Environment Variables
"We made sure no API keys were committed to GitHub. All secrets are stored in `.env` files which are securely loaded at runtime, keeping the codebase clean and safe."
