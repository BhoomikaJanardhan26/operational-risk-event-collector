import os
import requests
import time
from dotenv import load_dotenv

load_dotenv()

class GroqClient:
    def __init__(self):
        self.api_key = os.getenv("GROQ_API_KEY")

        # 🔥 DEBUG (IMPORTANT)
        print("🔑 GROQ API KEY:", self.api_key)

        if not self.api_key:
            raise ValueError("GROQ_API_KEY not found in .env")

        self.url = "https://api.groq.com/openai/v1/chat/completions"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def generate(self, prompt):
        data = {
            "model": "llama-3.3-70b-versatile",
            "messages": [
                {"role": "user", "content": prompt}
            ]
        }

        retries = 3

        for attempt in range(retries):
            try:
                print(f"🚀 Sending request (Attempt {attempt+1})")

                response = requests.post(self.url, headers=self.headers, json=data)

                print("📡 Status Code:", response.status_code)

                if response.status_code == 200:
                    result = response.json()
                    return result["choices"][0]["message"]["content"]

                else:
                    print("❌ API ERROR:", response.text)

            except Exception as e:
                print(f"🔥 EXCEPTION (Attempt {attempt+1}):", e)

            time.sleep(2 * (attempt + 1))

        return {
            "error": True,
            "message": "AI service unavailable",
            "is_fallback": True
        }