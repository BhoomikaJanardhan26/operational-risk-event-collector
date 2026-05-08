# Tool-66 — Operational Risk Event Collector

## Project Overview
The Operational Risk Event Collector is an AI-powered web application designed to help risk managers capture, analyze, and mitigate operational risk events. It uses an industry-standard tech stack and leverages LLMs for risk description, mitigation recommendations, and report generation.

## Tech Stack
- **Backend:** Java 17, Spring Boot 3.x, PostgreSQL 15, Redis 7, Flyway, Spring Security + JWT
- **AI Service:** Python 3.11, Flask 3.x, Groq API (LLaMA-3.3-70b), flask-limiter
- **Frontend:** React 18, Vite, Tailwind CSS, Axios
- **Infrastructure:** Docker, Docker Compose

## Architecture
```
[Frontend (React)] <--> [Backend (Spring Boot)] <--> [PostgreSQL]
                                |
                                v
                       [AI Service (Flask)] <--> [Groq API]
                                |
                                v
                             [Redis]
```

## Setup Instructions

### Prerequisites
- Docker & Docker Compose
- Groq API Key (from [console.groq.com](https://console.groq.com))

### Environment Setup
1. Clone the repository.
2. Create a `.env` file from `.env.example`:
   ```bash
   cp .env.example .env
   ```
3. Update the `GROQ_API_KEY` and other variables in `.env`.

### Running the Application
1. Start all services using Docker Compose:
   ```bash
   docker-compose up --build
   ```
2. Access the services:
   - Frontend: `http://localhost`
   - Backend: `http://localhost:8080/swagger-ui.html`
   - AI Service Health: `http://localhost:5000/health`

## AI Developer 2 Responsibilities
- GroqClient implementation with retries and fallback.
- Prompt tuning and template management.
- Security review and middleware for sanitization/injection detection.
- AI Documentation and Talking Points.
