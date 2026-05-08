# AI Summary Card
**Project:** Tool-66 — Operational Risk Event Collector

## Tech Stack
- **Language:** Python 3.11
- **Framework:** Flask 3.x
- **LLM Provider:** Groq API
- **Model:** LLaMA-3.3-70b-versatile
- **Security:** flask-limiter (30 req/min), custom sanitization middleware

## Key Endpoints
1. **POST `/describe`**
   - **Purpose:** Explains raw risk events clearly.
   - **Speed:** ~1-2 seconds.
   
2. **POST `/recommend`**
   - **Purpose:** Generates a JSON array of actionable mitigations (Preventive, Detective, Corrective).
   - **Parsing:** Custom Regex and JSON loads to ensure strict formatting.
   
3. **POST `/generate-report`**
   - **Purpose:** Creates a fully structured executive summary report.
   - **Reliability:** Built-in fallback template triggers if the Groq API fails.

## GitHub Link
https://github.com/tecsxpert/operational-risk-event-collector
