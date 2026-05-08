# AI Demo Script

**Objective:** Demonstrate AI endpoints to a non-technical panel in under 60 seconds.

## Setup
Ensure the Flask service is running (`docker-compose up` or `flask run`).

## Demo 1: AI Recommend
1. **Action:** Go to a created risk event in the UI and click the "AI Recommend" button.
2. **Input:** "Server downtime caused by a failed network switch, resulting in a 2-hour outage."
3. **Say:** "When we click 'Recommend', our Python microservice securely passes the event text to the Groq LLaMA 3.3 API. In under 2 seconds, it parses the response and returns an actionable JSON array. This saves managers from manually determining mitigation steps."
4. **Expected Output:**
```json
[
  {
    "action_type": "PREVENTIVE",
    "description": "Install redundant network switches to avoid single points of failure.",
    "priority": "HIGH"
  }
]
```

## Demo 2: Generate Report
1. **Action:** Click "Generate Report".
2. **Input:** (Same server downtime event)
3. **Say:** "Next, we generate a comprehensive structured report instantly. The AI translates raw user input into a formal overview with key items and recommendations, formatting it perfectly for executive review."

## Demo 3: Health and Security
1. **Action:** Navigate to `http://localhost:5000/health`.
2. **Say:** "Our microservice is robust. The `/health` endpoint proves we have 100% uptime and verifies which LLaMA model is currently active. Furthermore, all inputs are sanitized. If I attempt prompt injection, the system immediately rejects it with a 400 Bad Request, ensuring security against malicious actors."
