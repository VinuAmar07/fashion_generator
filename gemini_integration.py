import os
import requests
import base64

# Load Gemini API key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Base URL for Gemini API
TEXT_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent"
IMAGE_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-image:generateImage"

def generate_with_gemini(prompt):
    """Generates text advice from Gemini API"""
    if not GEMINI_API_KEY:
        return "Error: Gemini API key not found."

    headers = {
        "Content-Type": "application/json",
        "x-goog-api-key": GEMINI_API_KEY
    }

    body = {
        "contents": [{"parts": [{"text": prompt}]}]
    }

    try:
        response = requests.post(TEXT_API_URL, headers=headers, json=body)
        response.raise_for_status()
        data = response.json()

        candidates = data.get("candidates", [])
        if candidates:
            parts = candidates[0].get("content", {}).get("parts", [])
            if parts:
                return parts[0].get("text", "No response from Gemini.")
        return "No response from Gemini."

    except Exception as e:
        print("Gemini text API error:", e)
        return "Gemini API request failed."

def generate_fashion_image(prompt):
    """Generates fashion image from Gemini API and returns a data URL"""
    if not GEMINI_API_KEY:
        return None

    headers = {
        "Content-Type": "application/json",
        "x-goog-api-key": GEMINI_API_KEY
    }

    body = {
        "prompt": prompt,
        "size": "512x512",
        "n": 1
    }

    try:
        response = requests.post(IMAGE_API_URL, headers=headers, json=body)
        response.raise_for_status()
        data = response.json()

        # Gemini returns base64-encoded images
        image_b64 = data.get("data", [{}])[0].get("b64_json")
        if image_b64:
            return f"data:image/png;base64,{image_b64}"
        return None

    except Exception as e:
        print("Gemini image API error:", e)
        return None
