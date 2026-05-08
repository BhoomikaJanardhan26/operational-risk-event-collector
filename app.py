from flask import Flask
from routes.ai_routes import ai_bp
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)

limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["30 per minute"],
    storage_uri="memory://"
)

# ✅ THIS LINE IS CRITICAL
app.register_blueprint(ai_bp)

@app.route("/")
def home():
    return {"message": "AI Service Running"}

@app.route("/health")
def health():
    return {"status": "ok", "model": "llama-3.3-70b-versatile", "uptime": "100%"}

if __name__ == "__main__":
    app.run(port=5000, debug=True, use_reloader=False)