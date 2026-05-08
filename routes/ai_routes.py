print("✅ AI_ROUTES FILE LOADED")
print("✅ NEW AI_ROUTES FILE LOADED")
import json
import re
import os
from flask import Blueprint, request, jsonify
from services.groq_client import GroqClient
from services.security import sanitize_input, detect_prompt_injection
from datetime import datetime

ai_bp = Blueprint("ai", __name__)

# ✅ Single client instance
client = GroqClient()

def load_prompt(filename, **kwargs):
    path = os.path.join("prompts", filename)
    with open(path, "r") as f:
        template = f.read()
    return template.format(**kwargs)

def extract_json(text):
    # Try to find JSON array or object
    match = re.search(r"(\[.*\]|\{.*\})", text, re.DOTALL)
    if not match:
        return None
    return match.group(0)

# ------------------ DESCRIBE ------------------
@ai_bp.route("/describe", methods=["POST"])
def describe():
    try:
        data = request.get_json()
        if not data or "text" not in data:
            return jsonify({"error": "Missing input"}), 400

        if detect_prompt_injection(data["text"]):
            return jsonify({"error": "Prompt injection detected"}), 400

        clean = sanitize_input(data["text"])
        prompt = load_prompt("describe_prompt.txt", event_text=clean)
        
        result = client.generate(prompt)
        
        if isinstance(result, dict) and result.get("is_fallback"):
            return jsonify(result)

        return jsonify({
            "generated_at": datetime.now().isoformat(),
            "response": result
        })

    except Exception as e:
        print("🔥 ERROR:", e)
        return jsonify({"error": str(e)}), 500


# ------------------ RECOMMEND ------------------
@ai_bp.route("/recommend", methods=["POST"])
def recommend():
    try:
        data = request.get_json()
        if not data or "text" not in data:
            return jsonify({"error": "Missing input"}), 400

        if detect_prompt_injection(data["text"]):
            return jsonify({"error": "Prompt injection detected"}), 400

        clean = sanitize_input(data["text"])
        prompt = load_prompt("recommend_prompt.txt", event_text=clean)

        raw_result = client.generate(prompt)
        
        if isinstance(raw_result, dict) and raw_result.get("is_fallback"):
            return jsonify(raw_result)

        json_text = extract_json(raw_result)
        if not json_text:
            raise ValueError("No valid JSON found in AI response")

        parsed = json.loads(json_text)

        return jsonify({
            "generated_at": datetime.now().isoformat(),
            "recommendations": parsed
        })

    except Exception as e:
        print("🔥 ERROR:", e)
        return jsonify({"error": str(e)}), 500

# ------------------ REPORT ------------------
@ai_bp.route("/generate-report", methods=["POST"])
def report():
    try:
        data = request.get_json()
        if not data or "text" not in data:
            return jsonify({"error": "Missing input"}), 400

        if detect_prompt_injection(data["text"]):
            return jsonify({"error": "Prompt injection detected"}), 400

        clean = sanitize_input(data["text"])
        prompt = load_prompt("report_prompt.txt", event_text=clean)

        raw_result = client.generate(prompt)

        if isinstance(raw_result, dict) and raw_result.get("is_fallback"):
            return jsonify(raw_result)
        
        json_text = extract_json(raw_result)
        if not json_text:
            parsed = {"raw": raw_result}
        else:
            parsed = json.loads(json_text)

        return jsonify({
            "generated_at": datetime.now().isoformat(),
            "report": parsed
        })

    except Exception as e:
        print("🔥 ERROR:", e)
        return jsonify({"error": str(e)}), 500